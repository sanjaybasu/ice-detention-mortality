# ICE Detention Mortality Analysis: Complete Package (FY2004-2025)

**All 250 Deaths with Complete Details**

This package contains comprehensive analysis of all 250 in-custody deaths in U.S. Immigration and Customs Enforcement (ICE) detention from fiscal year 2004 through fiscal year 2025, with complete cause of death information for every death.

---

## Quick Start

### For Medical Reviewers

**Start here:** `medical_review/COMPLETE_MEDICAL_REVIEW.md`
- Comprehensive analysis of all 250 deaths
- Cause of death breakdown
- Facility-specific patterns
- Recommendations for further review

**Primary data file:** `data/all_250_deaths_detailed.csv`
- All 250 deaths with complete details
- Includes PDF URLs for source verification

**Replication code:** `replication_code/` directory
- Complete Python scripts to reproduce all analyses

### For Data Verification

**Source documents guide:** `source_documents/SOURCE_DOCUMENTS_GUIDE.md`
- Direct download links for all ICE reports
- Instructions for verifying every data point

---

## Package Contents

### 1. Complete Data Files (`data/`)

- all_250_deaths_detailed.csv** - **PRIMARY DATA FILE**
  - All 250 deaths (FY2004-2025)
  - Columns: Name, Sex, Age, Country, Date of Death, **Cause of Death**, Facility Name, Facility Location, Facility Type, PDF URL, Period
  - **Every death includes cause of death information**
  - **Every death includes source PDF URL for verification**

**Supporting Data Files:**

- **complete_death_records.csv** - Basic death records (name, date, fiscal year, administration)
- **detailed_death_data.csv** - Detailed data for FY2018-2025 (77 deaths)
- **average_daily_population.csv** - ADP data by fiscal year
- **mortality_rates_by_administration.csv** - Calculated mortality rates

### 2. Replication Code (`replication_code/`)

Complete Python scripts to reproduce all analyses:
- **01_data_extraction.py** - Verifies data extraction
- **02_calculate_mortality_rates.py** - Calculates mortality rates
- **03_generate_figures.py** - Generates figures

### 3. Medical Review (`medical_review/`)

- **COMPLETE_MEDICAL_REVIEW.md** - Comprehensive medical analysis of all 250 deaths
  - Cause of death analysis
  - Facility-specific patterns
  - Temporal trends
  - Recommendations for review

### 4. Source Documents (`source_documents/`)

- **SOURCE_DOCUMENTS_GUIDE.md** - Complete guide to accessing all source PDFs
  - Download links for ICE 2003-2017 PDF
  - URLs for all 77 individual FY2018-2025 death reports
  - ADP data sources

---

## Key Findings

### All 250 Deaths (FY2004-2025)

**Demographics:**
- 226 male (90.4%), 24 female (9.6%)
- 55 deaths in IGSA facilities (22.0%)
- 41 deaths in contract facilities (16.4%)

**Mortality Rates by Administration:**
- Bush (2001-2009): 79.17 per 100k (99 deaths)
- Obama (2009-2017): 25.37 per 100k (68 deaths)
- Trump 1 (2017-2021): 26.54 per 100k (42 deaths)
- Biden (2021-2025): 23.35 per 100k (26 deaths)
- Trump 2 (2025): 25.00 per 100k (15 deaths)

**Cause of Death (FY2018-2025, n=77):**
- Cardiovascular: 35 deaths (45.5%)
- Suicide: 12 deaths (15.6%)
- Infectious disease: 9 deaths (11.7%)
- Other/undetermined: 15 deaths (19.5%)

---

## For Medical Reviewers

### Complete Cause of Death Data

**All 250 deaths have cause of death information** extracted from official ICE reports:

- **FY2003-2017 (173 deaths):** Cause listed in ICE master PDF
- **FY2018-2025 (77 deaths):** Detailed cause in individual death reports

### How to Review Individual Deaths

1. Open `data/all_250_deaths_detailed.csv`
2. Find the death of interest
3. Click the URL in the `PDF_URL` column to access the official ICE death report
4. Review the complete medical information

### Priority Areas for Review

See `medical_review/COMPLETE_MEDICAL_REVIEW.md` for:
- Cardiovascular deaths (leading cause)
- Suicide deaths (preventable)
- Infectious disease deaths
- Facility-specific patterns

---

## Data Quality & Verification

✓ **Complete roster:** All 250 deaths included (173 from 2003-2017 FOIA PDF, 77 individual PDFs for 2018-2025)
✓ **Cause data present:** Each death retains the ICE-reported cause (preliminary or final as provided)
✓ **Verifiable:** Every death now has a downloaded source PDF in `death_report_pdfs/`
✓ **Reproducible code:** Scripts regenerate rates and figures; see `replication_code/`

### To Verify the Data

1. Download ICE 2003-2017 PDF: https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf
2. Compare with `all_250_deaths_detailed.csv` (173 deaths)
3. Visit ICE death reporting page: https://www.ice.gov/detain/detainee-death-reporting
4. Compare with `all_250_deaths_detailed.csv` (77 deaths)
5. Total: 250 deaths ✓

---

## System Requirements

**To run replication code:**
- Python 3.11+
- pandas, numpy, scipy, matplotlib

**To view data:**
- Any CSV viewer (Excel, Google Sheets, etc.)

**To access source PDFs:**
- Web browser with PDF support

---

## Citation

If using this data or analysis, please cite:

> Mortality in U.S. Immigration and Customs Enforcement Detention, Fiscal Years 2004-2025: An Epidemiological Analysis. 2025.


---

**Package Version:** 2.0 (Complete - All 250 Deaths)
**Last Updated:** November 15, 2025 (age and facility location fully populated for all 250 deaths via FOIA PDF extraction and ICE individual reports)
**Total Deaths:** 250 (FY2004-2025)
**Complete Data:** 100%
