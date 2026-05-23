#!/usr/bin/env python3
"""Render the SafeExec 14-week Gantt chart as a PNG for inclusion in the W2 proposal DOCX."""

from datetime import date

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Phases and their colors
PHASE_COLORS = {
    "I":   "#3b6fd4",   # blue   — Launch
    "II":  "#3b8f3b",   # green  — Design
    "III": "#d49a3b",   # orange — Implementation
    "IV":  "#6a3bd4",   # purple — Results & hardening
    "V":   "#c43b8f",   # pink   — Reporting
    "VI":  "#d43b3b",   # red    — Defense
}

# (label, start, end, phase, is_milestone)
TASKS = [
    ("W1  launch packet (graded 90/100)",            date(2026, 5,  9), date(2026, 5, 17), "I",   False),
    ("W2  proposal approval package",                 date(2026, 5, 16), date(2026, 5, 26), "I",   False),
    ("W3  lit synthesis & requirements",              date(2026, 5, 23), date(2026, 5, 29), "II",  False),
    ("W4  design review (arch / threat / eval)",      date(2026, 5, 30), date(2026, 6,  5), "II",  False),
    ("W5  sprint I — Docker baseline",                date(2026, 6,  6), date(2026, 6, 12), "III", False),
    ("W6  sprint II — hardened Docker",               date(2026, 6, 13), date(2026, 6, 19), "III", False),
    ("W7  adversarial taxonomy lock + MIDPOINT",      date(2026, 6, 20), date(2026, 6, 26), "III", False),
    ("W8  sprint III — gVisor back-end",              date(2026, 6, 27), date(2026, 7,  3), "III", False),
    ("W9  results, limitations, impact draft",        date(2026, 7,  4), date(2026, 7, 10), "IV",  False),
    ("W10 artifact hardening & repro test",           date(2026, 7, 11), date(2026, 7, 17), "IV",  False),
    ("W11 FULL DRAFT to supervisor",                  date(2026, 7, 18), date(2026, 7, 24), "V",   False),
    ("W12 revision; deck & demo script",              date(2026, 7, 25), date(2026, 7, 31), "V",   False),
    ("W13 rehearsal + AI-use appendix",               date(2026, 8,  1), date(2026, 8,  7), "VI",  False),
    ("W14 FINAL SUBMISSION + reflection",             date(2026, 8,  8), date(2026, 8, 14), "VI",  False),
]

# Vertical lines for completion gates
GATES = [
    (date(2026, 5, 26), "G1 W2"),
    (date(2026, 6,  5), "G2 W4"),
    (date(2026, 6, 12), "G3 W5"),
    (date(2026, 6, 26), "G4 W7"),
    (date(2026, 7, 24), "G5 W11"),
    (date(2026, 8, 14), "G6 W14"),
]

TODAY = date(2026, 5, 21)


def main(out_path: str = "gantt.png") -> None:
    fig, ax = plt.subplots(figsize=(13, 7))

    labels = [t[0] for t in TASKS]
    y_positions = list(range(len(TASKS)))

    for y, (label, start, end, phase, _) in zip(y_positions, TASKS):
        width = (end - start).days or 1
        ax.barh(
            y,
            width,
            left=mdates.date2num(start),
            height=0.62,
            color=PHASE_COLORS[phase],
            edgecolor="#2a2a2a",
            linewidth=0.6,
            alpha=0.92,
        )

    # gate vertical lines + labels at top
    for gate_date, gate_label in GATES:
        ax.axvline(
            mdates.date2num(gate_date),
            color="#222",
            linestyle="--",
            linewidth=0.8,
            alpha=0.55,
        )
        ax.annotate(
            gate_label,
            xy=(mdates.date2num(gate_date), len(TASKS) - 0.4),
            xytext=(0, 6),
            textcoords="offset points",
            ha="center",
            fontsize=8,
            color="#222",
            weight="bold",
        )

    # "today" marker
    ax.axvline(
        mdates.date2num(TODAY),
        color="#d43b3b",
        linestyle="-",
        linewidth=1.4,
        alpha=0.9,
    )
    ax.annotate(
        f"today: {TODAY.isoformat()}",
        xy=(mdates.date2num(TODAY), -0.8),
        xytext=(4, -2),
        textcoords="offset points",
        ha="left",
        va="top",
        fontsize=8,
        color="#d43b3b",
        weight="bold",
    )

    ax.set_yticks(y_positions)
    ax.set_yticklabels(labels, fontsize=9)
    ax.invert_yaxis()
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO, interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%d"))
    ax.tick_params(axis="x", labelsize=8, rotation=0)
    ax.set_xlim(mdates.date2num(date(2026, 5, 7)), mdates.date2num(date(2026, 8, 16)))
    ax.set_ylim(len(TASKS) - 0.4, -1.0)
    ax.grid(axis="x", linestyle=":", alpha=0.35)
    ax.set_axisbelow(True)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)

    ax.set_title(
        "SafeExec — 14-week milestone map (CISC 699 SU 2026)",
        fontsize=12,
        weight="bold",
        pad=18,
    )

    # phase legend
    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=color, label=f"Phase {k}")
        for k, color in PHASE_COLORS.items()
    ]
    ax.legend(
        handles=legend_handles,
        loc="lower right",
        ncol=3,
        frameon=False,
        fontsize=8,
        bbox_to_anchor=(1.0, -0.18),
    )

    plt.tight_layout()
    plt.savefig(out_path, dpi=200, bbox_inches="tight")
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    import sys

    out = sys.argv[1] if len(sys.argv) > 1 else "gantt.png"
    main(out)
