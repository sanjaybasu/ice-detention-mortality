#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt


def main():
    base_dir = os.path.join(os.path.dirname(__file__), "..")
    data_path = os.path.join(base_dir, "manuscript", "revision", "Figure1_annual_source_data.csv")
    out_path = os.path.join(base_dir, "manuscript", "revision", "Figure1_ResearchLetter.png")

    df = pd.read_csv(data_path).sort_values("fiscal_year")
    years = df["fiscal_year"].astype(int).values

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, (ax_a, ax_b, ax_c) = plt.subplots(3, 1, figsize=(9, 11), sharex=True)

    # Policy markers requested by coauthors/reviewers.
    policy_events = {
        2005: {
            "label": "2005: Increased adoption\nof expedited removal",
            "color": "#6C757D",
            "style": ":",
            "width": 1.1,
        },
        2008: {
            "label": "2008: PBNDS introduced",
            "color": "#4C78A8",
            "style": "--",
            "width": 1.2,
        },
        2025: {
            "label": "2025: Detention expansion,\noversight termination,\nreported care disruption",
            "color": "#7A3E48",
            "style": "--",
            "width": 1.4,
        },
    }

    for ax in (ax_a, ax_b, ax_c):
        for year, spec in policy_events.items():
            ax.axvline(year, color=spec["color"], linestyle=spec["style"], linewidth=spec["width"], alpha=0.8, zorder=1)
        ax.grid(axis="y", alpha=0.25)
        ax.grid(axis="x", alpha=0.10)
        ax.set_xlim(years.min() - 0.5, years.max() + 1.2)

    # Panel A: ADP.
    ax_a.plot(years, df["adp"], color="#111111", marker="o", linewidth=2.0, markersize=4.5)
    ax_a.set_title("A. ICE average daily population (FY2004-FY2026*)", fontsize=12, pad=8)
    ax_a.set_ylabel("Average Daily Population", fontsize=10)
    ax_a.set_ylim(bottom=0)
    ax_a.plot(years[-1], df["adp"].iloc[-1], marker="*", color="black", markersize=10, zorder=5)

    # Panel B: annual deaths.
    ax_b.bar(years, df["deaths"], color="#1F77B4", edgecolor="#1F4B73", linewidth=0.6)
    ax_b.set_title("B. ICE in-custody deaths by fiscal year", fontsize=12, pad=8)
    ax_b.set_ylabel("Deaths", fontsize=10)
    ax_b.set_ylim(bottom=0)
    ax_b.plot(years[-1], df["deaths"].iloc[-1], marker="*", color="black", markersize=9, zorder=5)

    # Panel C: mortality rates.
    ax_c.plot(years, df["rate"], color="#D62728", marker="s", linewidth=2.0, markersize=4.5)
    ax_c.set_title("C. ICE mortality rate by fiscal year", fontsize=12, pad=8)
    ax_c.set_ylabel("Rate per 100,000 person-years", fontsize=10)
    ax_c.set_ylim(bottom=0)
    ax_c.plot(years[-1], df["rate"].iloc[-1], marker="*", color="#A81818", markersize=10, zorder=5)

    # Shared x-axis and annotation.
    ax_c.set_xticks(years)
    ax_c.set_xticklabels([str(y) for y in years], rotation=45, ha="right", fontsize=9)
    # Keep the asterisk marker on FY2026; explanation is provided in the figure caption.

    fig.tight_layout()
    fig.savefig(out_path, dpi=300, bbox_inches="tight")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
