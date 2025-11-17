#!/usr/bin/env python3
import os
import re
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "manuscript")
os.makedirs(OUT_DIR, exist_ok=True)

all_path = os.path.join(BASE_DIR, "all_250_deaths_detailed.csv")
detailed_path = os.path.join(BASE_DIR, "detailed_death_data.csv")

all_df = pd.read_csv(all_path)
subset77 = pd.read_csv(detailed_path)

def categorize(text: str) -> str:
    s = str(text).lower()
    if re.search(r"\bsuicide\b|hanging|self[- ]?inflicted|self[- ]?harm", s):
        return "Suicide"
    if re.search(r"covid|sars[- ]?cov|sepsis|septic|pneumonia|tuberculosis|tb\b|meningitis|hiv|aids|influenza|varicella|mumps|infection", s):
        return "Infectious (incl. COVID-19)"
    if re.search(r"cardio|coronary|myocard|arrhythm|hypertens|atheroscler|heart|myocardi", s):
        return "Cardiovascular"
    if re.search(r"stroke|intracran|brain|hemorrhage|subarachnoid|glioblastoma|aneurysm|seizure|epilep", s):
        return "Neurologic"
    if re.search(r"undetermined|pending|not stated|natural", s):
        return "Other/Undetermined"
    return "Other/Undetermined"

all_df["Cause_Category"] = all_df["Cause_of_Death"].apply(categorize)
subset77["Cause_Category"] = subset77["Cause of Death"].apply(categorize)

priv = {"CDF","Contract","USMS CDF"}
gov = {"SPC","ICE-operated","IGSA","DIGSA","BOP","USMS IGA"}
other = {"HOSPITAL","HOLD","STAGING","Not stated"}

def op_group(ft: str) -> str:
    if ft in priv:
        return "Private/Contracted"
    if ft in gov:
        return "Government/Intergov"
    if ft in other:
        return "Other/Unstated"
    return "Other/Unstated"

all_df["Operator_Group"] = all_df["Facility_Type"].apply(op_group)
subset77["Operator_Group"] = subset77["Facility Type"].apply(op_group)

def dist_table(df: pd.DataFrame, col: str) -> pd.DataFrame:
    counts = df[col].value_counts().sort_index()
    total = counts.sum()
    pct = (counts/total*100).round(1)
    return pd.DataFrame({"Category": counts.index, "Count": counts.values, "Percent": pct.values})

# Save distribution CSVs (optional artifacts)
dist_table(all_df, "Cause_Category").to_csv(os.path.join(BASE_DIR, "_cause_distribution_all.csv"), index=False)
dist_table(subset77, "Cause_Category").to_csv(os.path.join(BASE_DIR, "_cause_distribution_2018_2025.csv"), index=False)
dist_table(all_df, "Operator_Group").to_csv(os.path.join(BASE_DIR, "_operator_group_all.csv"), index=False)
dist_table(subset77, "Operator_Group").to_csv(os.path.join(BASE_DIR, "_operator_group_2018_2025.csv"), index=False)

# Build figures
plt.rcParams["figure.dpi"] = 300
plt.rcParams["savefig.dpi"] = 300

# Operator figure
op_all = dist_table(all_df, "Operator_Group").set_index("Category").reindex(["Private/Contracted","Government/Intergov","Other/Unstated"]).fillna({"Count":0,"Percent":0})
op_77 = dist_table(subset77, "Operator_Group").set_index("Category").reindex(["Private/Contracted","Government/Intergov","Other/Unstated"]).fillna({"Count":0,"Percent":0})

import numpy as np
x = np.arange(3)
width = 0.35
fig, ax = plt.subplots(figsize=(8,5))
ax.bar(x - width/2, op_all["Percent"], width, label="All years (N=250)")
ax.bar(x + width/2, op_77["Percent"], width, label="FY2018–2025 (N=77)")
ax.set_xticks(x)
ax.set_xticklabels(["Private/Contracted","Government/Intergov","Other/Unstated"], rotation=15)
ax.set_ylabel("Percent of deaths")
ax.set_title("Facility operator-type distribution")
ax.legend(frameon=False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "Appendix_Figure_A1_operator.png"), bbox_inches="tight")
plt.close(fig)

# Cause-of-death figure
cat_order = ["Cardiovascular","Infectious (incl. COVID-19)","Suicide","Neurologic","Other/Undetermined"]
c_all = dist_table(all_df, "Cause_Category").set_index("Category").reindex(cat_order).fillna({"Count":0,"Percent":0})
c_77 = dist_table(subset77, "Cause_Category").set_index("Category").reindex(cat_order).fillna({"Count":0,"Percent":0})

fig2, ax2 = plt.subplots(figsize=(9,5))
x2 = np.arange(len(cat_order))
ax2.bar(x2 - width/2, c_all["Percent"], width, label="All years (N=250)")
ax2.bar(x2 + width/2, c_77["Percent"], width, label="FY2018–2025 (N=77)")
ax2.set_xticks(x2)
ax2.set_xticklabels(cat_order, rotation=20)
ax2.set_ylabel("Percent of deaths")
ax2.set_title("Cause-of-death distribution (broad categories)")
ax2.legend(frameon=False)
fig2.tight_layout()
fig2.savefig(os.path.join(OUT_DIR, "Appendix_Figure_A2_cause.png"), bbox_inches="tight")
plt.close(fig2)

print("Wrote Appendix_Figure_A1_operator.png and Appendix_Figure_A2_cause.png to manuscript/")

