"""
EP-TSP — Acuña ACL Recovery Trajectory
Emerson Performance (EP)

Caso único profundo: la trayectoria de sprint speed de Ronald Acuña Jr.
a través de DOS cirugías de ACL separadas (rodilla derecha, jul 2021;
rodilla izquierda, mayo-jun 2024). El espejo de tj-recovery-trajectory,
pero para lesión de tren inferior en vez de codo.

Uso:
    python scripts/acuna_analysis.py
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from ep_chart_style import *

DATA_DIR = Path(__file__).parent.parent / "data"
OUTPUT_DIR = Path(__file__).parent.parent / "outputs"

# Fechas clave (verificadas por búsqueda web)
INJURY_1 = "2021-07-20"  # rotura ACL derecha
INJURY_2 = "2024-05-26"  # rotura ACL izquierda, cirugía 2024-06-06


def load_data():
    return pd.read_csv(DATA_DIR / "acuna_sprint_speed_trajectory.csv")


def plot_trajectory(df: pd.DataFrame, lang: str) -> None:
    fig, ax = plt.subplots(figsize=(11, 7.5))
    apply_ep_style(fig, ax)

    ax.plot(df["year"], df["sprint_speed"], marker="o", markersize=11,
            color=EP_COLORS["navy"], linewidth=2.5, zorder=3)

    # Marcar los años de lesión
    ax.axvline(2021, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)
    ax.axvline(2024, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)

    peak = df["sprint_speed"].max()
    current = df["sprint_speed"].iloc[-1]

    if lang == "en":
        ax.text(2021, 29.7, "1st ACL tear\n(right knee)", ha="center", fontsize=9.5,
                color=EP_COLORS["red"], fontweight="bold",
                fontproperties=FONT_LABEL if FONT_LABEL else None)
        ax.text(2024, 29.7, "2nd ACL tear\n(left knee)", ha="center", fontsize=9.5,
                color=EP_COLORS["red"], fontweight="bold",
                fontproperties=FONT_LABEL if FONT_LABEL else None)
        style_axis_label(ax, "x", "SEASON")
        style_axis_label(ax, "y", "SPRINT SPEED (ft/s)")
        add_finding_title(fig, ax, "Acuña Went From Elite Speed to League-Average, Across Two ACL Tears",
            f"Peak {peak} ft/s (2020) -> {current} ft/s now, stable for 2 seasons post-2nd surgery")
        add_source(fig, "Source: Baseball Savant Sprint Speed leaderboard, 2019-2026")
        fname = OUTPUT_DIR / "acuna_trajectory_EN.png"
    else:
        ax.text(2021, 29.7, "1ra rotura ACL\n(rodilla derecha)", ha="center", fontsize=9.5,
                color=EP_COLORS["red"], fontweight="bold",
                fontproperties=FONT_LABEL if FONT_LABEL else None)
        ax.text(2024, 29.7, "2da rotura ACL\n(rodilla izquierda)", ha="center", fontsize=9.5,
                color=EP_COLORS["red"], fontweight="bold",
                fontproperties=FONT_LABEL if FONT_LABEL else None)
        style_axis_label(ax, "x", "TEMPORADA")
        style_axis_label(ax, "y", "SPRINT SPEED (ft/s)")
        add_finding_title(fig, ax, "Acuña Pasó de Velocidad Élite a Promedio de Liga, a Través de Dos Roturas de ACL",
            f"Pico {peak} ft/s (2020) -> {current} ft/s ahora, estable por 2 temporadas post-2da cirugía")
        add_source(fig, "Fuente: Leaderboard de Sprint Speed de Baseball Savant, 2019-2026")
        fname = OUTPUT_DIR / "acuna_trajectory_ES.png"

    ax.set_ylim(26, 30.2)
    fig.tight_layout(rect=[0, 0.01, 1, 1])
    plt.savefig(fname, dpi=200, facecolor=EP_COLORS["off_white"])
    plt.close(fig)
    print(f"Guardado: {fname}")


def plot_sb_success_rate(lang: str) -> None:
    df = pd.read_csv(DATA_DIR / "acuna_sb_success_rate.csv")
    fig, ax = plt.subplots(figsize=(11, 7.5))
    apply_ep_style(fig, ax)

    ax.plot(df["year"], df["sb_pct"], marker="o", markersize=11,
            color=EP_COLORS["gold"], linewidth=2.5, zorder=3)
    ax.axvline(2021, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)
    ax.axvline(2024, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)

    if lang == "en":
        style_axis_label(ax, "x", "SEASON")
        style_axis_label(ax, "y", "STOLEN BASE SUCCESS RATE (%)")
        add_finding_title(fig, ax, "Steal Success Didn't Follow the Same Decline as Raw Speed",
            "2025 (post-2nd surgery): career-best 90% success rate, despite career-low sprint speed")
        add_source(fig, "Source: Baseball-Reference, 2018-2026")
        fname = OUTPUT_DIR / "acuna_sb_success_EN.png"
    else:
        style_axis_label(ax, "x", "TEMPORADA")
        style_axis_label(ax, "y", "TASA DE ÉXITO DE ROBO (%)")
        add_finding_title(fig, ax, "El Éxito de Robo No Siguió el Mismo Declive que la Velocidad Cruda",
            "2025 (post-2da cirugía): mejor tasa de su carrera, 90%, pese al sprint speed más bajo de su carrera")
        add_source(fig, "Fuente: Baseball-Reference, 2018-2026")
        fname = OUTPUT_DIR / "acuna_sb_success_ES.png"

    ax.set_ylim(60, 95)
    fig.tight_layout(rect=[0, 0.01, 1, 1])
    plt.savefig(fname, dpi=200, facecolor=EP_COLORS["off_white"])
    plt.close(fig)
    print(f"Guardado: {fname}")


def plot_lead_distance(lang: str) -> None:
    df = pd.read_csv(DATA_DIR / "acuna_lead_distance.csv")
    fig, ax = plt.subplots(figsize=(11, 7.5))
    apply_ep_style(fig, ax)

    ax.plot(df["year"], df["lead_dist_sb_att"], marker="o", markersize=11,
            color=EP_COLORS["green"], linewidth=2.5, zorder=3)
    ax.axvline(2021, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)
    ax.axvline(2024, color=EP_COLORS["red"], linewidth=1.5, linestyle="--", alpha=0.6, zorder=2)

    if lang == "en":
        style_axis_label(ax, "x", "SEASON")
        style_axis_label(ax, "y", "LEAD DISTANCE ON SB ATTEMPTS (ft)")
        add_finding_title(fig, ax, "2026: Acuña's Biggest Lead Ever \u2014 But Not Yet a Confirmed Pattern",
            "13.6 ft avg. in 2026 vs. 12.3 ft in 2023 \u2014 not statistically significant (p=0.425), n=19 attempts")
        add_source(fig, "Source: Baseball Savant Statcast Basestealing, 2018-2026")
        fname = OUTPUT_DIR / "acuna_lead_distance_EN.png"
    else:
        style_axis_label(ax, "x", "TEMPORADA")
        style_axis_label(ax, "y", "DISTANCIA DE LEAD EN INTENTOS DE ROBO (pies)")
        add_finding_title(fig, ax, "2026: El Lead Más Grande de Acuña \u2014 Pero Aún No Confirmado",
            "Prom. 13.6 pies en 2026 vs. 12.3 en 2023 \u2014 no significativo (p=0.425), n=19 intentos")
        add_source(fig, "Fuente: Statcast Basestealing de Baseball Savant, 2018-2026")
        fname = OUTPUT_DIR / "acuna_lead_distance_ES.png"

    ax.set_ylim(10, 14.5)
    fig.tight_layout(rect=[0, 0.01, 1, 1])
    plt.savefig(fname, dpi=200, facecolor=EP_COLORS["off_white"])
    plt.close(fig)
    print(f"Guardado: {fname}")


if __name__ == "__main__":
    df = load_data()
    print(df.to_string(index=False))
    print(f"\nPico: {df['sprint_speed'].max()} ft/s ({df.loc[df['sprint_speed'].idxmax(),'year']})")
    print(f"Actual: {df['sprint_speed'].iloc[-1]} ft/s")
    print(f"Caída total: {df['sprint_speed'].max() - df['sprint_speed'].iloc[-1]:.1f} ft/s")

    OUTPUT_DIR.mkdir(exist_ok=True)
    for lang in ["en", "es"]:
        plot_trajectory(df, lang)
        plot_sb_success_rate(lang)
        plot_lead_distance(lang)
