#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

# Figures will be written next to the manuscript for direct inclusion
output_dir = os.path.join(os.path.dirname(__file__), "..", "manuscript")
os.makedirs(output_dir, exist_ok=True)

base_dir = os.path.join(os.path.dirname(__file__), "..", "data")
mortality_df = pd.read_csv(os.path.join(base_dir, "mortality_rates_by_administration.csv"))
deaths_df = pd.read_csv(os.path.join(base_dir, "complete_death_records.csv"))
adp_df = pd.read_csv(os.path.join(base_dir, "average_daily_population.csv"))
details_df = pd.read_csv(os.path.join(base_dir, "all_272_deaths_detailed.csv"))
cbp_df = pd.read_csv(os.path.join(base_dir, "cbp_deaths_summary.csv"))

# Figure 1
fig, ax = plt.subplots(figsize=(8, 6))
admins = mortality_df["administration"].values
rates = mortality_df["rate_per_100k"].values
ci_lower = mortality_df["ci_lower"].values
ci_upper = mortality_df["ci_upper"].values
yerr_lower = rates - ci_lower
yerr_upper = ci_upper - rates
x_pos = np.arange(len(admins))
ax.bar(x_pos, rates, color="steelblue", alpha=0.8, edgecolor="black", linewidth=0.5)
ax.errorbar(x_pos, rates, yerr=[yerr_lower, yerr_upper], fmt="none", ecolor="black", capsize=5, capthick=1.5, linewidth=1.5)
ax.set_xlabel("Administration", fontsize=12, fontweight="bold", labelpad=10)
ax.set_ylabel("Mortality Rate (per 100,000 person-years)", fontsize=12, fontweight="bold")
ax.set_xticks(x_pos)
ax.set_xticklabels(admins, fontsize=11)
ax.set_ylim(0, max(ci_upper) * 1.1)
ax.yaxis.grid(True, linestyle="--", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "Figure1.png"), dpi=300, bbox_inches="tight")
plt.close()

# Figure 2 (three panels):
#  - Panel A: Average Daily Population (ADP) by fiscal year
#  - Panel B: Death counts by fiscal year
#  - Panel C: Mortality rates by fiscal year
# Build per-year aggregates (FY for historical years; calendar year for 2024–2025)
details_df['Date_of_Death'] = pd.to_datetime(details_df['Date_of_Death'])
analysis_end = datetime(2026, 1, 19)
details_df = details_df[details_df['Date_of_Death'] <= analysis_end].copy()
def fiscal_year_for_plot(d):
    # Use fiscal years for the full series
    return d.year + 1 if d.month >= 10 else d.year
details_df['fiscal_year'] = details_df['Date_of_Death'].apply(fiscal_year_for_plot)
details_df = details_df[details_df['fiscal_year'] >= 2004]
adp_df_fy = adp_df[adp_df['fiscal_year'] >= 2004].copy()

fy_rows = []
for fy in sorted(adp_df_fy['fiscal_year'].unique()):
    adp_row = adp_df_fy[adp_df_fy['fiscal_year'] == fy]
    adp_val = adp_row['adp'].values[0]
    deaths = (details_df['fiscal_year'] == fy).sum()
    rate = (deaths / adp_val) * 100000
    if fy == 2026:
        # Use partial FY2026 person-time through Jan 19, 2026 (Oct 1–Jan 19 = 111 days)
        partial_days = 111
        rate = (deaths / (adp_val * (partial_days / 365))) * 100000
    fy_rows.append({
        'fiscal_year': fy,
        'adp': adp_val,
        'deaths': deaths,
        'rate': rate,
        'administration': adp_row['administration'].values[0],
    })

fy_df = pd.DataFrame(fy_rows).sort_values('fiscal_year')

fig, (axA, axB, axC) = plt.subplots(3, 1, figsize=(12, 12), sharex=True)

# Panel A: ADP
axA.plot(fy_df['fiscal_year'], fy_df['adp'], 'o-', color='black', label='ADP')
axA.set_ylabel('Average Daily Population', fontsize=12, fontweight='bold')
axA.set_title('A. Average Daily Population (ADP)', fontsize=12)
axA.grid(True, linestyle='--', alpha=0.3)
axA.set_axisbelow(True)
axA.set_ylim(bottom=0)
for boundary in [2009, 2017, 2021, 2025]:
    axA.axvline(boundary, color='gray', linestyle=':', linewidth=1)

# Panel B: Death counts
axB.bar(fy_df['fiscal_year'], fy_df['deaths'], color='#1f77b4', alpha=0.8, edgecolor='black', linewidth=0.5)
axB.set_ylabel('Deaths', fontsize=12, fontweight='bold')
axB.set_title('B. Deaths per year', fontsize=12)
axB.grid(True, linestyle='--', alpha=0.3)
axB.set_axisbelow(True)
axB.set_ylim(bottom=0)
for boundary in [2009, 2017, 2021, 2025]:
    axB.axvline(boundary, color='gray', linestyle=':', linewidth=1)

# Panel C: Mortality rate
axC.plot(fy_df['fiscal_year'], fy_df['rate'], 's-', color='#d62728', label='Mortality rate')
axC.set_ylabel('Rate per 100,000 person-years', fontsize=12, fontweight='bold')
axC.set_xlabel('Year', fontsize=12, fontweight='bold')
axC.set_title('C. Mortality rate per fiscal year', fontsize=12)
axC.grid(True, linestyle='--', alpha=0.3)
axC.set_axisbelow(True)
axC.set_ylim(bottom=0)
for boundary in [2009, 2017, 2021, 2025]:
    axC.axvline(boundary, color='gray', linestyle=':', linewidth=1)

axC.set_xticks(fy_df['fiscal_year'])
axC.set_xticklabels(fy_df['fiscal_year'].astype(int), rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Figure2.png'), dpi=300, bbox_inches='tight')
plt.close()

# Figure 3: Cumulative deaths by days into administration
admin_start = {
    'Bush': datetime(2001, 1, 20),
    'Obama': datetime(2009, 1, 20),
    'Trump 1': datetime(2017, 1, 20),
    'Biden': datetime(2021, 1, 20),
    'Trump 2': datetime(2025, 1, 20),
}

deaths_df['date_of_death'] = pd.to_datetime(deaths_df['date_of_death'])
fig, ax = plt.subplots(figsize=(10, 6))
colors = {"Bush": "#d62728", "Obama": "#1f77b4", "Trump 1": "#ff7f0e", "Biden": "#2ca02c", "Trump 2": "#9467bd"}
for admin in ["Bush", "Obama", "Trump 1", "Biden", "Trump 2"]:
    admin_dates = deaths_df.loc[deaths_df['administration'] == admin, 'date_of_death'].sort_values()
    if admin not in admin_start or len(admin_dates) == 0:
        continue
    start = admin_start[admin]
    days = (admin_dates - start).dt.days
    # only include days >= 0 (within admin term window)
    days = days[days >= 0]
    if len(days) == 0:
        continue
    cum = np.arange(1, len(days) + 1)
    ax.step(days, cum, where='post', color=colors[admin], linewidth=2, label=admin)

ax.set_xlabel('Days into administration', fontsize=12, fontweight='bold')
ax.set_ylabel('Cumulative deaths', fontsize=12, fontweight='bold')
ax.legend(frameon=True)
ax.grid(True, linestyle='--', alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Figure3.png'), dpi=300, bbox_inches='tight')
plt.close()

print("All figures generated successfully: Figure1, Figure2 (multi-panel), Figure3 (cumulative)")

# CBP figure: counts by fiscal year (kept separate from ICE)
cbp_df = cbp_df.sort_values("fiscal_year")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex=False)
x = np.arange(len(cbp_df))

# Panel A: total and in-custody stacked
ax1.bar(x, cbp_df["in_custody"], label="In-custody", color="#1f77b4", alpha=0.85)
ax1.bar(x, cbp_df["cbp_involved_non_custody"] + cbp_df["additional_requested"], bottom=cbp_df["in_custody"], label="Other reported", color="#ff7f0e", alpha=0.7)
ax1.set_xticks(x)
ax1.set_xticklabels(cbp_df["fiscal_year"].astype(int), rotation=45)
ax1.set_ylabel("Deaths (count)", fontsize=12, fontweight="bold")
ax1.set_title("A. CBP deaths by category", fontsize=12)
ax1.legend(frameon=True, fontsize=9)
ax1.grid(True, linestyle="--", alpha=0.3)
ax1.set_axisbelow(True)
ax1.set_ylim(bottom=0)

# Panel B: components (in-custody, CBP-involved, additional)
width = 0.25
ax2.bar(x - width, cbp_df["in_custody"], width=width, label="In-custody", color="#1f77b4", alpha=0.85)
ax2.bar(x, cbp_df["cbp_involved_non_custody"], width=width, label="CBP-involved (not in custody)", color="#2ca02c", alpha=0.85)
ax2.bar(x + width, cbp_df["additional_requested"], width=width, label="Additional requested", color="#d62728", alpha=0.75)
ax2.set_xticks(x)
ax2.set_xticklabels(cbp_df["fiscal_year"].astype(int), rotation=45)
ax2.set_ylabel("Deaths (count)", fontsize=12, fontweight="bold")
ax2.set_title("B. CBP reported deaths by type", fontsize=12)
ax2.legend(frameon=True, fontsize=9)
ax2.grid(True, linestyle="--", alpha=0.3)
ax2.set_axisbelow(True)
ax2.set_ylim(bottom=0)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, "Appendix_Figure_A3.png"), dpi=300, bbox_inches="tight")
plt.close()
print("CBP figure generated successfully: Appendix_Figure_A3")
