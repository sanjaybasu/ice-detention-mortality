#!/usr/bin/env python3
import os
import re
import csv
import time
import requests
import pandas as pd

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, '..', 'data')
OUTDIR = os.path.join(BASE, '..', 'verification')
os.makedirs(OUTDIR, exist_ok=True)

df = pd.read_csv(os.path.join(DATA, 'all_272_deaths_detailed.csv'))
recent = df[df['Period'].astype(str).str.contains('FY2018-2025')].copy()

session = requests.Session()
session.headers.update({'User-Agent': 'Waymark-ICE-Verification/1.0'})

def mirror_url(url: str) -> str:
    return 'https://r.jina.ai/http://' + url.replace('https://','')

def fetch_text(url: str) -> str:
    r = session.get(mirror_url(url), timeout=30)
    r.raise_for_status()
    return r.text

def extract_ddr_fields(text: str):
    date = None
    cause_line = None
    for line in text.splitlines():
        l = line.strip()
        if 'Date of Death' in l:
            m = re.search(r'Date of Death:\s*([A-Za-z]+\s+\d{1,2},\s*\d{4})', l)
            if m:
                date = m.group(1)
        if re.search(r'cause of death', l, re.I):
            cl = re.sub(r'^.*[Cc]ause of death\s*:?\s*', '', l)
            if cl:
                cause_line = cl
    return date, cause_line, text

def us_to_iso(s: str) -> str | None:
    import datetime as dt
    for fmt in ('%B %d, %Y','%b %d, %Y'):
        try:
            return dt.datetime.strptime(s, fmt).date().isoformat()
        except Exception:
            pass
    return None

def classify(s: str) -> dict:
    s = (s or '').lower()
    return {
        'suicide': ('suicide' in s) or ('hanging' in s),
        'covid': ('covid' in s) or ('sars' in s),
        'pending': ('pending' in s) or ('not stated' in s) or ('undetermined' in s),
        'cardio': any(k in s for k in ['cardio','cardiac','myocard','coronary','atherosclero','hypertens','arrhythm','asystole','mi '])
    }

rows=[]
for _, r in recent.iterrows():
    name = r['Name']
    url = str(r['PDF_URL'])
    ds_date = pd.to_datetime(r['Date_of_Death']).date().isoformat()
    ds_cause = str(r['Cause_of_Death'])
    ddr_iso=None; ddr_cause=None
    http_status=None; error=''
    try:
        text = fetch_text(url)
        ddr_date, ddr_cause, full_text = extract_ddr_fields(text)
        ddr_iso = us_to_iso(ddr_date) if ddr_date else None
        http_status = 200
    except Exception as e:
        error = str(e)
    flags = []
    if ddr_iso and ddr_iso != ds_date:
        flags.append('date_mismatch')
    c_ds = classify(ds_cause)
    # Prefer explicit cause line; otherwise fall back to whole-document keyword search
    c_ddr = classify(ddr_cause or (full_text if http_status == 200 else ''))
    for key in ['suicide','covid','pending']:
        if c_ds.get(key) != c_ddr.get(key):
            flags.append(f'{key}_mismatch')
    # optional cardio flag
    if c_ds.get('cardio') != c_ddr.get('cardio'):
        # only flag if suicide/covid/pending not already raised
        if not any(k in flags for k in ['suicide_mismatch','covid_mismatch','pending_mismatch']):
            flags.append('cardio_mismatch')
    rows.append({
        'Name': name,
        'Date_Dataset': ds_date,
        'Date_DDR': ddr_iso or '',
        'Cause_Dataset': ds_cause,
        'Cause_DDR_Line': ddr_cause or '',
        'URL': url,
        'Flags': ';'.join(flags),
        'HTTP_Status': http_status or '',
        'Error': error,
    })
    time.sleep(0.2)

outcsv = os.path.join(OUTDIR, 'cause_audit_report.csv')
with open(outcsv, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader(); writer.writerows(rows)

flagged = [r for r in rows if r['Flags']]
print(f'Audit complete. Total {len(rows)} FY2018–2025 deaths. Flagged {len(flagged)} entries.')
print(f'Report: {outcsv}')
