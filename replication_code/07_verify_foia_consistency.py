#!/usr/bin/env python3
import os
import re
import csv
import pandas as pd

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, '..', 'data')
OUT = os.path.join(BASE, '..', 'verification')
os.makedirs(OUT, exist_ok=True)

all_df = pd.read_csv(os.path.join(DATA, 'all_272_deaths_detailed.csv'))
foia_df = pd.read_csv(os.path.join(DATA, '_extracted_foia_2003_2017.csv'))

# Subset to FOIA-era in our main dataset
main = all_df[all_df['Period'].astype(str).str.contains('FY2003-2017')].copy()

def normalize_name(s: str) -> str:
    s = s or ''
    s = s.upper()
    s = re.sub(r'\s+', ' ', s)
    s = s.replace('‐','-').replace('–','-').replace('—','-')
    s = re.sub(r'[,]', '', s)
    s = re.sub(r'[^A-Z0-9\-\s]', '', s)
    # normalize spaces around hyphens
    s = re.sub(r'\s*-\s*', '-', s)
    s = s.strip()
    return s

def norm_cause(s: str) -> str:
    s = (s or '').lower()
    s = s.replace('\u00A0',' ')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

main['name_norm'] = main['Name'].apply(normalize_name)
main['date_iso'] = pd.to_datetime(main['Date_of_Death']).dt.date
main['cause_norm'] = main['Cause_of_Death'].apply(norm_cause)

foia_df['name_norm'] = foia_df['name'].apply(normalize_name)
foia_df['date_iso'] = pd.to_datetime(foia_df['date_of_death']).dt.date
foia_df['cause_norm'] = foia_df['cause'].apply(norm_cause)

# Build index by (name_norm, date_iso)
main_idx = {(r['name_norm'], r['date_iso']): r for _, r in main.iterrows()}

rows = []
for _, fr in foia_df.iterrows():
    key = (fr['name_norm'], fr['date_iso'])
    ds = main_idx.get(key)
    if ds is None:
        rows.append({
            'Status': 'MISSING_IN_MAIN',
            'FOIA_Name': fr['name'],
            'FOIA_Date': fr['date_of_death'],
            'FOIA_Cause': fr['cause'],
            'Main_Name': '',
            'Main_Date': '',
            'Main_Cause': '',
        })
        continue
    # Compare cause keywords
    cause_flag = ''
    f = fr['cause_norm']
    m = ds['cause_norm']
    # check key categories
    def flag_eq(k):
        return (k in f) == (k in m)
    diffs = []
    for k in ['suicide', 'covid', 'pending', 'cardiac', 'coronary', 'myocard', 'tuberculosis', 'pneumonia']:
        if not flag_eq(k):
            diffs.append(k)
    if diffs:
        cause_flag = ';'.join(diffs)
    rows.append({
        'Status': 'OK' if not diffs else 'CAUSE_MISMATCH',
        'FOIA_Name': fr['name'],
        'FOIA_Date': fr['date_of_death'],
        'FOIA_Cause': fr['cause'],
        'Main_Name': ds['Name'],
        'Main_Date': ds['Date_of_Death'],
        'Main_Cause': ds['Cause_of_Death'],
        'Cause_Flags': cause_flag,
    })

outcsv = os.path.join(OUT, 'foia_consistency_report.csv')
with open(outcsv, 'w', newline='') as f:
    fieldnames = ['Status','FOIA_Name','FOIA_Date','FOIA_Cause','Main_Name','Main_Date','Main_Cause','Cause_Flags']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader(); writer.writerows(rows)

print(f'FOIA consistency audit complete. {len(rows)} records processed.')
print(f'Report: {outcsv}')
