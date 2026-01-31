#!/usr/bin/env python3
import os
import pandas as pd

BASE_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
deaths = pd.read_csv(os.path.join(BASE_DIR, "complete_death_records.csv"))

def assign_fiscal_year(date_str):
    date = pd.to_datetime(date_str)
    return date.year + 1 if date.month >= 10 else date.year

def assign_administration(date_str):
    date = pd.to_datetime(date_str)
    if date < pd.to_datetime('2009-01-20'): return 'Bush'
    if date < pd.to_datetime('2017-01-20'): return 'Obama'
    if date < pd.to_datetime('2021-01-20'): return 'Trump 1'
    if date < pd.to_datetime('2025-01-20'): return 'Biden'
    return 'Trump 2'

deaths['fy_check'] = deaths['date_of_death'].apply(assign_fiscal_year)
deaths['admin_check'] = deaths['date_of_death'].apply(assign_administration)

fy_mismatches = deaths[deaths['fiscal_year'] != deaths['fy_check']]
admin_mismatches = deaths[deaths['administration'] != deaths['admin_check']]

print(f"Fiscal year mismatches: {len(fy_mismatches)}")
print(f"Administration mismatches: {len(admin_mismatches)}")
