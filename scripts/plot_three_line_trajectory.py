"""
plot_three_line_trajectory.py (v2)
Combines sprint speed and SB success rate (already in acuna-acl-recovery)
with a THIRD line: "Jump" (r_sec_minus_prim_lead) -- feet of secondary
lead gained beyond the primary lead, during the pitcher's motion, before
release. This is the closest public proxy to "reaction/reading skill" in
a stolen-base attempt, independent of the runner's raw sprint speed.

DATA SOURCE NOTE: pulled from Baseball Savant's basestealing leaderboard
CSV export by Emerson on 2026-09-29 (confirmed working from his machine;
the automated pull failed with 403 from the sandbox this script was
originally drafted in -- see net_bases_gained_extension.py history).
The leaderboard did NOT expose a field literally named "Net Bases
Gained"; the real column names found were r_primary_lead,
r_secondary_lead, and r_sec_minus_prim_lead -- lead-distance metrics,
not a run-value metric. r_sec_minus_prim_lead is used here as it's the
cleanest "jump" proxy among what was actually returned.

CAVEAT ON n_sb IN THIS LEADERBOARD: this leaderboard's own stolen-base
counts (e.g., 58 for 2023) run well below Acuna's real season totals
(73 in 2023) -- it appears to be scoped to a subset of attempts (likely
1st-to-2nd with no other runners on base, per Baseball Savant's public
documentation for this leaderboard), not full-season attempts. Treat
r_sec_minus_prim_lead as a within-that-subset average, not a
season-complete figure. State this in the README alongside the finding.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import os

EP_NAVY = "#0B1B33"
EP_GOLD = "#D4A53A"
EP_OFFWHITE = "#F5F3EC"
EP_GREEN = "#3D6B4F"

# From the published README tables (main repo's existing findings)
sprint_speed = {
    2019: 29.1, 2020: 29.4, 2021: 28.5, 2022: 28.0,
    2023: 27.7, 2024: 27.9, 2025: 27.0, 2026: 27.0,
}
sb_success_pct = {
    2021: 73.9, 2022: 72.5, 2023: 83.9, 2024: 84.2, 2025: 90.0, 2026: 69.6,
}

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_PATH = os.path.join(_SCRIPT_DIR, "..", "data", "acuna_net_bases_gained.csv")


def load_jump_metric(path: str = _DATA_PATH) -> dict:
    df = pd.read_csv(path)
    return dict(zip(df["season"], df["r_sec_minus_prim_lead"]))


def plot_three_lines(jump: dict, save_as: str = "acuna_jump_trajectory_EN.png"):
    fig, ax1 = plt.subplots(figsize=(11, 7))
    fig.patch.set_facecolor(EP_OFFWHITE)
    ax1.set_facecolor(EP_OFFWHITE)

    years = sorted(sprint_speed.keys())
    ax1.plot(years, [sprint_speed[y] for y in years], color=EP_NAVY, marker='o',
              linewidth=2, label="Sprint Speed (ft/s)")
    ax1.set_ylabel("Sprint Speed (ft/s)", color=EP_NAVY, fontweight='bold')
    ax1.tick_params(axis='y', labelcolor=EP_NAVY)
    ax1.set_xlabel("Season")

    ax2 = ax1.twinx()
    sb_years = sorted(sb_success_pct.keys())
    ax2.plot(sb_years, [sb_success_pct[y] for y in sb_years], color=EP_GOLD, marker='s',
              linewidth=2, label="SB Success Rate (%)")

    jump_years = sorted(jump.keys())
    ax3 = ax1.twinx()
    ax3.spines["right"].set_position(("axes", 1.12))
    ax3.plot(jump_years, [jump[y] for y in jump_years], color=EP_GREEN, marker='^',
              linewidth=2, linestyle='--', label="Jump (ft, sec. lead gained)")
    ax3.set_ylabel("Jump (ft)", color=EP_GREEN, fontweight='bold')
    ax3.tick_params(axis='y', labelcolor=EP_GREEN)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    lines3, labels3 = ax3.get_legend_handles_labels()
    ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3,
               loc='lower center', bbox_to_anchor=(0.5, -0.28), ncol=3, frameon=False)

    plt.title("Acuña: Raw Speed vs. Basestealing Jump — Across Two ACL Surgeries",
               color=EP_NAVY, fontsize=13, fontweight='bold')
    ax1.axvspan(2020.6, 2021.4, color=EP_NAVY, alpha=0.08)  # 2021 ACL #1
    ax1.axvspan(2023.6, 2024.4, color=EP_NAVY, alpha=0.08)  # 2024 ACL #2
    plt.tight_layout()
    plt.savefig(save_as, dpi=200, facecolor=EP_OFFWHITE, bbox_inches="tight")
    print(f"Saved {save_as}")


if __name__ == "__main__":
    jump = load_jump_metric()
    plot_three_lines(jump)
