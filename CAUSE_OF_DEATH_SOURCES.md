# Cause of Death Sources Documentation

## Overview

This document explains where the cause of death information comes from for all 272 deaths in the dataset.

---

## Source of Cause of Death Information

### FY2003-2017 Deaths (172 deaths)

**Source:** ICE Master PDF - "List of Deaths in ICE Custody - Data from: 10/01/2003 to 06/05/2017"

**PDF URL:** https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf

**Column in PDF:** "FINAL CAUSE OF DEATH"

**Adjudication Status:** YES - These are listed as "FINAL CAUSE OF DEATH" in the official ICE report, indicating they have been adjudicated by medical examiners or coroners.

**Examples from the data:**
- "Acute Thrombotic Occlusion Left Descending Coronary Artery"
- "Hypertensive Cardiovascular Disease"
- "Brain Tumor Glioblastoma"
- "Asphyxia"
- "AIDS"
- "Cardiac Arrhythmia"

**Data Quality:** The PDF table includes a dedicated column for "FINAL CAUSE OF DEATH" which indicates these are official, adjudicated causes from medical authorities.

---

### FY2018-2025 Deaths (77 deaths)

**Source:** Individual ICE Death Report PDFs

**Base URL:** https://www.ice.gov/doclib/foia/reports/ddr[LastName][FirstName].pdf

**Section in PDF:** "Preliminary Cause of Death" or "Final Cause of Death" (varies by report)

**Adjudication Status:** MIXED
- Some reports list "Preliminary Cause of Death" (pending autopsy/medical examiner report)
- Some reports list final adjudicated causes
- Some reports state "Pending Autopsy and Medical Examiner Report"
- Some reports state "Not stated"

**Examples from the data:**
- "Cardiopulmonary arrest due to complications from HIV, septic shock, anemia, dehydration, and T-cell lymphoma" (detailed)
- "Coronary artery disease" (final)
- "Pending Autopsy and Medical Examiner Report. Preliminary information indicates the death was due to natural causes" (preliminary)
- "Not stated" (no information available)

**Data Quality:** Individual death reports provide varying levels of detail. Some include complete medical examiner findings, while others only have preliminary information.

---

### Public Reporting Updates (CY2025 and January 2026; 23 deaths)

**Source:** Public reporting (Guardian timeline and January 2026 update list)

**URL:** https://www.theguardian.com/us-news/ng-interactive/2026/jan/04/ice-2025-deaths-timeline and https://www.theguardian.com/us-news/2026/jan/28/deaths-ice-2026-

**Cause-of-death detail:** Varies by report; summarized from public reporting and linked source documents.

**Data Quality:** Public reporting provides descriptive summaries and context for cases not yet listed in ICE individual reports. These entries are included to complete CY2025 and January 2026 counts; they are flagged as public reporting updates in the dataset.

---

## Comparison of Data Quality

| Period | Source | Adjudication | Detail Level | Completeness |
|:-------|:-------|:-------------|:-------------|:-------------|
| FY2003-2017 | Master PDF | **Final** (adjudicated) | Moderate | 100% (all 172 have causes) |
| FY2018-2025 | Individual PDFs | **Mixed** (some final, some preliminary) | High (when available) | 100% (all 77 have some information) |
| CY2025 + Jan 2026 | Public reporting | **Mixed/uncertain** | Variable | 100% (all 23 have summarized causes) |

---

## Key Findings

### 1. All 272 Deaths Have Cause Information

Every death in the dataset includes cause of death information, though the level of detail varies.

### 2. FY2003-2017 Causes Are Adjudicated

The ICE master PDF explicitly labels causes as "FINAL CAUSE OF DEATH," indicating these have been officially determined by medical examiners or coroners.

### 3. FY2018-2025 Causes Are Mixed

### 4. Public Reporting Updates Fill Recent Gaps

Public reporting contributes 23 additional deaths (CY2025 and January 2026) with summarized cause-of-death details and linked sources until official ICE reports are released.

Individual death reports include:
- **Final causes:** Officially adjudicated by medical examiners
- **Preliminary causes:** Initial determinations pending full autopsy
- **Pending:** Cases where autopsy results are not yet available
- **Not stated:** Cases where cause information is not provided in the report

### 4. Detail Level Varies

- **FY2003-2017:** Concise medical terminology (e.g., "Cardiac Arrhythmia," "AIDS")
- **FY2018-2025:** Often more detailed (e.g., "Cardiopulmonary arrest due to complications from HIV, septic shock, anemia, dehydration, and T-cell lymphoma")

---

## Verification Process

### To Verify FY2003-2017 Causes

1. Download the master PDF: https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf
2. Open the PDF and locate the death record
3. Check the "FINAL CAUSE OF DEATH" column
4. Compare with the cause listed in `all_272_deaths_detailed.csv`

### To Verify FY2018-2025 Causes

1. Open `all_272_deaths_detailed.csv`
2. Find the death of interest
3. Copy the URL from the "PDF URL" column
4. Open the PDF in a browser
5. Locate the "Cause of Death" section in the report
6. Compare with the cause listed in the CSV

---

## Limitations

### 1. Preliminary vs. Final Determinations

Some FY2018-2025 deaths have preliminary causes that may be updated when final autopsy results are available.

### 2. "Not Stated" Cases

A small number of deaths (primarily in FY2018-2025) have "Not stated" as the cause, indicating ICE did not provide this information in the public report.

### 3. Varying Detail Levels

The level of medical detail varies significantly between deaths and time periods, making standardized categorization challenging.

### 4. Pending Autopsies

Some recent deaths list "Pending Autopsy" as the cause, meaning the final determination is not yet available.

---

## Recommendations for Medical Review

### 1. Prioritize Final Causes

When analyzing causes of death, prioritize deaths with final adjudicated causes over preliminary determinations.

### 2. Verify Recent Deaths

For FY2018-2025 deaths, check the individual PDFs to determine whether the cause is preliminary or final.

### 3. Request Updates

For deaths with "Pending" causes, consider requesting updated information from ICE to obtain final determinations.

### 4. Standardize Carefully

When categorizing causes (e.g., "cardiovascular," "suicide"), review the actual PDF reports to ensure accurate classification, especially for complex or multi-factorial causes.

---

## Data Files

**Primary Data:** `all_272_deaths_detailed.csv`
- Column: "Cause_of_Death"
- All 272 deaths included
- Source PDFs listed in "PDF_URL" column

**Source PDFs:**
- FY2003-2017: Single master PDF (included in package)
- FY2018-2025: 77 individual PDFs (to be downloaded)

---

## Conclusion

The cause of death information in this dataset comes directly from official ICE reports:

- **FY2003-2017:** Final adjudicated causes from ICE master PDF
- **FY2018-2025:** Mix of final and preliminary causes from individual death reports

All causes are verifiable by accessing the source PDFs listed in the dataset. Medical reviewers should be aware that some FY2018-2025 causes are preliminary and may be subject to change pending final autopsy results.

---

**Last Updated:** November 15, 2025
**Total Deaths:** 272
**Causes Available:** 272 (100%)
**Final Adjudicated:** 172 (FY2003-2017) + unknown number from FY2018-2025
