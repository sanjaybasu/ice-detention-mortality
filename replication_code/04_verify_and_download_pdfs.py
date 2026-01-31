#!/usr/bin/env python3
import os
import csv
import sys
from urllib.parse import urlparse
import requests
import pandas as pd

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, '..', 'data')
PDF_DIR = os.path.join(BASE, '..', 'death_report_pdfs')
SRC_DIR = os.path.join(BASE, '..', 'source_documents')
OUT_DIR = os.path.join(BASE, '..', 'verification')
os.makedirs(OUT_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(SRC_DIR, exist_ok=True)

details_path = os.path.join(DATA, 'all_272_deaths_detailed.csv')
df = pd.read_csv(details_path)

# Verify individual FY2018-2025 PDFs
recent = df[df['Period'].astype(str).str.contains('FY2018-2025')].copy()

records = []
session = requests.Session()
session.headers.update({'User-Agent': 'Waymark-ICE-Verification/1.0'})

for idx, row in recent.iterrows():
    url = str(row['PDF_URL']).strip()
    parsed = urlparse(url)
    fname = os.path.basename(parsed.path)
    local_path = os.path.join(PDF_DIR, fname)
    exists = os.path.exists(local_path)
    status = None
    downloaded = False
    error = ''
    try:
        r = session.head(url, timeout=20, allow_redirects=True)
        status = r.status_code
        if status >= 400:
            # try GET if HEAD blocked
            r = session.get(url, timeout=30, stream=True)
            status = r.status_code
        if (not exists) and status == 200:
            # download
            with session.get(url, timeout=60, stream=True) as resp:
                resp.raise_for_status()
                with open(local_path, 'wb') as f:
                    for chunk in resp.iter_content(chunk_size=65536):
                        if chunk:
                            f.write(chunk)
            downloaded = True
            exists = True
    except Exception as e:
        error = str(e)

    records.append({
        'Name': row.get('Name', ''),
        'Date_of_Death': row.get('Date_of_Death', ''),
        'URL': url,
        'Local_File': fname,
        'Local_Exists': exists,
        'HTTP_Status': status,
        'Downloaded_Now': downloaded,
        'Error': error,
    })

# Ensure FOIA master PDF present in source_documents
foia_url = 'https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf'
foia_local = os.path.join(SRC_DIR, 'foia_detaineedeaths_2003_2017.pdf')
foia_status = None
foia_downloaded = False
foia_error = ''
try:
    resp = session.head(foia_url, timeout=20, allow_redirects=True)
    foia_status = resp.status_code
    if foia_status >= 400:
        resp = session.get(foia_url, timeout=30, stream=True)
        foia_status = resp.status_code
    if (not os.path.exists(foia_local)) and foia_status == 200:
        with session.get(foia_url, timeout=60, stream=True) as r2:
            r2.raise_for_status()
            with open(foia_local, 'wb') as f:
                for chunk in r2.iter_content(chunk_size=65536):
                    if chunk:
                        f.write(chunk)
        foia_downloaded = True
except Exception as e:
    foia_error = str(e)

foia_row = {
    'Name': 'FOIA Master List (2003–2017)',
    'Date_of_Death': '',
    'URL': foia_url,
    'Local_File': os.path.basename(foia_local),
    'Local_Exists': os.path.exists(foia_local),
    'HTTP_Status': foia_status,
    'Downloaded_Now': foia_downloaded,
    'Error': foia_error,
}

report_path = os.path.join(OUT_DIR, 'verification_report.csv')
with open(report_path, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)

with open(os.path.join(OUT_DIR, 'verification_summary.txt'), 'w') as f:
    total = len(records)
    have = sum(1 for r in records if r['Local_Exists'])
    ok_http = sum(1 for r in records if (r['HTTP_Status'] == 200))
    f.write(f"FY2018–2025 deaths: {total}\n")
    f.write(f"Local PDFs present: {have}\n")
    f.write(f"HTTP 200s: {ok_http}\n")
    f.write(f"FOIA local present: {foia_row['Local_Exists']}, status: {foia_row['HTTP_Status']}, downloaded: {foia_row['Downloaded_Now']}\n")

print("Verification complete.")
print(f"Report: {report_path}")
print(f"FOIA status/local: {foia_row['HTTP_Status']}/{foia_row['Local_Exists']}")
