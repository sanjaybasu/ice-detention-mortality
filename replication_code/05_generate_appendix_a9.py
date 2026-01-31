#!/usr/bin/env python3
import os
import pandas as pd

BASE = os.path.dirname(__file__)
DATA = os.path.join(BASE, '..', 'data')
OUT = os.path.join(BASE, '..', 'manuscript', 'APPENDIX_A9_INDEX.md')

df = pd.read_csv(os.path.join(DATA, 'all_272_deaths_detailed.csv'))

cols = [
    'Name','Sex','Age','Country','Date_of_Death',
    'Facility_Name','Facility_Location','Facility_Type','Cause_of_Death','PDF_URL'
]
df = df[cols].copy()

# Sort by Date_of_Death
df['Date_of_Death'] = pd.to_datetime(df['Date_of_Death'])
df = df.sort_values('Date_of_Death')

with open(OUT, 'w') as f:
    f.write('# Appendix A9 Index: Per-Death Primary-Source URLs\n\n')
    f.write(f'This table lists every death (N = {len(df)}) with key details and the primary official source URL.\n\n')
    # Header
    f.write('| Name | Sex | Age | Country | Date of Death | Facility | Location | Type | Cause of Death | Source URL |\n')
    f.write('| :--- | :-- | --: | :------ | :------------ | :------ | :------- | :--- | :------------- | :--------- |\n')
    for _, r in df.iterrows():
        f.write('| {Name} | {Sex} | {Age} | {Country} | {Date} | {Fac} | {Loc} | {Typ} | {Cause} | {URL} |\n'.format(
            Name=str(r['Name']).replace('|','/'),
            Sex=str(r['Sex']),
            Age=('' if pd.isna(r['Age']) else int(r['Age'])),
            Country=str(r['Country']),
            Date=r['Date_of_Death'].date().isoformat(),
            Fac=str(r['Facility_Name']).replace('|','/'),
            Loc=str(r['Facility_Location']).replace('|','/'),
            Typ=str(r['Facility_Type']),
            Cause=str(r['Cause_of_Death']).replace('|','/'),
            URL=str(r['PDF_URL'])
        ))

print(f"Wrote {OUT}")
