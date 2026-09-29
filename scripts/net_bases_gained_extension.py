"""
net_bases_gained_extension.py
Extension to acuna-acl-recovery: adds Net Bases Gained (Statcast's
basestealing-skill-above-expected metric) as a third trajectory line,
alongside the sprint speed and SB success rate already in the repo.

WHY THIS METRIC: Net Bases Gained is built from a per-attempt SUCCESS
PROBABILITY MODEL that already accounts for runner sprint speed (plus
pitcher/catcher factors). So a player's Net Bases Gained is roughly
"stolen-base value above what his own speed would predict." If this
stays flat or improves while sprint speed declines, that's direct
evidence the skill/decision layer (jump, reads, situational judgment)
held up independent of the physical tool declining -- the "mechanism"
question Finding 2 of the main repo left untested.

STATUS: the automated Baseball Savant pull below is UNVERIFIED from the
build environment (no network route to baseballsavant.mlb.com from
here -- see the main repo's own Audit Log for the same limitation
pattern on other EP repos). Try it first; if the column names or
response shape have changed, use the manual fallback documented below.
"""

import time
import pandas as pd
import requests

ACUNA_MLBAM_ID = 660670
SEASONS = list(range(2019, 2027))  # 2019-2026; no attempts logged pre-Statcast-tracking outside this range for this study

# Baseball Savant's basestealing leaderboard, one season at a time, CSV export.
# UNVERIFIED: confirm this still returns a CSV and that these are the right
# query params by opening the URL in a browser first (swap season, check it
# downloads a table). Baseball Savant leaderboard URLs are known to change
# their exact parameter names periodically.
LEADERBOARD_URL = "https://baseballsavant.mlb.com/leaderboard/basestealing-run-value"


def fetch_season_csv(season: int) -> pd.DataFrame:
    params = {
        "game_type": "Regular",
        "season_start": season,
        "season_end": season,
        "sortColumn": "n_bases_gained",  # UNVERIFIED exact column name
        "sortDirection": "desc",
        "min": "5",       # min stolen-base opportunities, keeps the file small
        "csv": "true",
    }
    resp = requests.get(LEADERBOARD_URL, params=params, timeout=30)
    resp.raise_for_status()
    from io import StringIO
    return pd.read_csv(StringIO(resp.text))


def pull_acuna_net_bases_gained() -> pd.DataFrame:
    """Automated attempt. Prints the columns it finds so you can spot the
    right one by eye if 'n_bases_gained' below doesn't match."""
    rows = []
    for season in SEASONS:
        try:
            df = fetch_season_csv(season)
            print(f"{season}: columns = {list(df.columns)}")
            player_col = "player_id" if "player_id" in df.columns else "runner_id"
            row = df[df[player_col] == ACUNA_MLBAM_ID]
            if row.empty:
                print(f"  Acuna not found in {season} leaderboard (maybe below the 'min' attempts threshold)")
                continue
            rows.append(row.assign(season=season))
        except Exception as e:
            print(f"{season}: FAILED — {e}")
        time.sleep(1.0)  # courtesy delay

    if not rows:
        raise RuntimeError(
            "Automated pull returned nothing. Use the manual fallback: "
            "open https://baseballsavant.mlb.com/leaderboard/basestealing-run-value "
            "in a browser, set the season, search 'Acuna', and either read the "
            "Net Bases Gained value off the page or use the CSV-download button "
            "if the site has one, one season at a time."
        )
    return pd.concat(rows, ignore_index=True)


def build_manual_entry_template() -> pd.DataFrame:
    """
    Fallback: fill this in by hand from the Baseball Savant leaderboard UI
    (baseballsavant.mlb.com/leaderboard/basestealing-run-value), one row per
    season, searching 'Acuna' and reading off Net Bases Gained. Takes about
    2 minutes for 8 seasons.
    """
    return pd.DataFrame({
        "season": SEASONS,
        "net_bases_gained": [None] * len(SEASONS),  # <-- fill these in by hand
    })


# Path fix: resolve data/ relative to THIS FILE, not to whatever folder
# you happen to run the command from (so it works whether you run it as
# "python scripts/net_bases_gained_extension.py" from the repo root, or
# as "python net_bases_gained_extension.py" from inside scripts/).
import os
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_DIR = os.path.join(_SCRIPT_DIR, "..", "data")
os.makedirs(_DATA_DIR, exist_ok=True)

if __name__ == "__main__":
    try:
        df = pull_acuna_net_bases_gained()
        print(df[["season", "n_bases_gained"] if "n_bases_gained" in df.columns else df.columns])
        out_path = os.path.join(_DATA_DIR, "acuna_net_bases_gained.csv")
        df.to_csv(out_path, index=False)
        print(f"Saved to {out_path}")
    except Exception as e:
        print(f"\nAutomated pull failed: {e}")
        template_path = os.path.join(_DATA_DIR, "acuna_net_bases_gained_TEMPLATE.csv")
        print(f"Falling back to manual template -> {template_path}")
        build_manual_entry_template().to_csv(template_path, index=False)
        print(f"\nOpen that file (it's in the data folder, next to the other .csv files\n"
              f"in this repo) and fill in the net_bases_gained column by hand.")
