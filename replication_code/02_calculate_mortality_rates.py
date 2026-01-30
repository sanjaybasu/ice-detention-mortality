import pandas as pd
import numpy as np
from scipy import stats

import os
base_dir = os.path.join(os.path.dirname(__file__), "..", "data")
deaths_df = pd.read_csv(os.path.join(base_dir, "complete_death_records.csv"))
adp_df = pd.read_csv(os.path.join(base_dir, "average_daily_population.csv"))

def calculate_poisson_ci(deaths, person_years, confidence=0.95):
    alpha = 1 - confidence
    lower = 0 if deaths == 0 else stats.chi2.ppf(alpha/2, 2*deaths) / (2 * person_years) * 100000
    upper = stats.chi2.ppf(1 - alpha/2, 2*(deaths+1)) / (2 * person_years) * 100000
    return lower, upper

# Validate that the 'administration' field is assigned by actual date of death
from datetime import datetime, timedelta

cutpoints = [
    ("Bush", datetime(2001, 10, 1), datetime(2009, 1, 19)),
    ("Obama", datetime(2009, 1, 20), datetime(2017, 1, 19)),
    ("Trump 1", datetime(2017, 1, 20), datetime(2021, 1, 19)),
    ("Biden", datetime(2021, 1, 20), datetime(2025, 1, 19)),
    ("Trump 2", datetime(2025, 1, 20), datetime(2026, 1, 19)),
]

def admin_by_date(d):
    for name, start, end in cutpoints:
        if start <= d <= end:
            return name
    return None

deaths_df['date_of_death'] = pd.to_datetime(deaths_df['date_of_death'])
analysis_end = cutpoints[-1][-1]
analysis_df = deaths_df[deaths_df['date_of_death'] <= analysis_end].copy()
analysis_df['admin_by_date'] = analysis_df['date_of_death'].apply(admin_by_date)
if not (analysis_df['admin_by_date'] == analysis_df['administration']).all():
    mismatches = analysis_df.loc[analysis_df['admin_by_date'] != analysis_df['administration'], ['date_of_death','administration','admin_by_date']]
    raise ValueError(f"Administration assignment mismatch for some rows based on date-of-death.\n{mismatches.head()}\nPlease ensure 'administration' is assigned by date of death.")

results = []
fy_month = 10
fy_day = 1

for admin, start_dt, end_dt in cutpoints:
    admin_deaths = analysis_df[analysis_df["administration"] == admin]
    death_count = len(admin_deaths)
    
    fy_start = start_dt.year
    fy_end = end_dt.year
    
    if start_dt >= datetime(start_dt.year, fy_month, fy_day):
      fy_start += 1
    
    if end_dt >= datetime(end_dt.year, fy_month, fy_day):
      fy_end += 1
      
    person_years = 0
    n_days = 0
  
    for fy_year in range(fy_start,fy_end + 1):
      if (adp_df.fiscal_year == (fy_year - 1)).any():
        fy_range = (datetime(fy_year - 1, fy_month, fy_day), datetime(fy_year, fy_month, fy_day) + timedelta(days=-1))
        max_start = max(fy_range[0], start_dt)
        min_end = min(fy_range[1], end_dt)
        n_overlap = max(0, (min_end - max_start).days + 1)
        person_years += adp_df[adp_df["fiscal_year"] == fy_year].adp.mean() * n_overlap / 365
        n_days += n_overlap
    
    rate = (death_count / person_years) * 100000
    ci_lower, ci_upper = calculate_poisson_ci(death_count, person_years)
    
    results.append({
        "administration": admin,
        "deaths": death_count,
        "person_years": person_years,
        "days": n_days,
        "rate_per_100k": rate,
        "ci_lower": ci_lower,
        "ci_upper": ci_upper
    })


results_df = pd.DataFrame(results)
results_df.to_csv(os.path.join(base_dir, "mortality_rates_by_administration.csv"), index=False)
print(results_df.to_string(index=False))
