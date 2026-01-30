# ICE Detention Mortality Analysis: Complete Package (FY2004–Jan 2026)

**All 272 Deaths with Complete Details**

This package contains comprehensive analysis of all 272 in-custody deaths in U.S. Immigration and Customs Enforcement (ICE) detention from fiscal year 2004 through January 19, 2026, with complete cause of death information for every death.

---

## What's New in This Version

✓ **All 272 deaths cataloged (FY2004–Jan 2026)** from official ICE sources and public reporting updates
✓ **Cause of death for every death** (verbatim from ICE PDFs; preliminary vs. final noted in source docs)
✓ **Facility name and type** for all deaths; age and facility location fully populated for all 272 deaths (FY2003–2017 and FY2018–2025, with public reporting updates for CY2025 and January 2026)
✓ **Source PDFs** downloaded to `death_report_pdfs/` for offline verification
✓ **Medical review summary** - Comprehensive clinical analysis (with noted data gaps)

---

## Quick Start

### For Medical Reviewers

**Start here:** `medical_review/COMPLETE_MEDICAL_REVIEW.md`
- Comprehensive analysis through FY2025 (public reporting updates for January 2026 not yet incorporated)
- Cause of death breakdown
- Facility-specific patterns
- Recommendations for further review

**Primary data file:** `data/all_272_deaths_detailed.csv`
- All 272 deaths with complete details
- Includes PDF URLs for source verification

### For Researchers

**Manuscript:** `manuscript/MANUSCRIPT.md`
**Appendix:** `manuscript/APPENDIX.md` (comprehensive methods)
**Figures:** `manuscript/Figure1.png` and `Figure2.png`

**Replication code:** `replication_code/` directory
- Complete Python scripts to reproduce all analyses

### For Data Verification

**Source documents guide:** `source_documents/SOURCE_DOCUMENTS_GUIDE.md`
- Direct download links for all ICE reports
- Instructions for verifying every data point

---

## Package Contents

### 1. Manuscript & Appendix (`manuscript/`)

- **MANUSCRIPT.md** - Complete manuscript
- **APPENDIX.md** - Comprehensive appendix with STROBE checklist
- **Figure1.png** - Mortality rates by administration (300 DPI)
- **Figure2.png** - Mortality rates by fiscal year (300 DPI)

### 2. Complete Data Files (`data/`)

**NEW: All 272 Deaths with Complete Details**

- **all_272_deaths_detailed.csv** - **PRIMARY DATA FILE**
  - All 272 deaths (FY2004–Jan 2026)
  - Columns: Name, Sex, Age, Country, Date of Death, **Cause of Death**, Facility Name, Facility Location, Facility Type, PDF URL, Period
  - **Every death includes cause of death information**
  - **Every death includes source PDF URL for verification**

**Supporting Data Files:**

- **complete_death_records.csv** - Basic death records (name, date, fiscal year, administration)
- **detailed_death_data.csv** - Detailed data for FY2018–2026 (100 deaths)
- **average_daily_population.csv** - ADP data by fiscal year
- **mortality_rates_by_administration.csv** - Calculated mortality rates

### 3. Replication Code (`replication_code/`)

Complete Python scripts to reproduce all analyses:
- **01_data_extraction.py** - Verifies data extraction
- **02_calculate_mortality_rates.py** - Calculates mortality rates
- **03_generate_figures.py** - Generates figures

### 4. Medical Review (`medical_review/`)

- **COMPLETE_MEDICAL_REVIEW.md** - Comprehensive medical analysis through FY2025 (public reporting updates for January 2026 not yet incorporated)
  - Cause of death analysis
  - Facility-specific patterns
  - Temporal trends
  - Recommendations for review

### 5. Source Documents (`source_documents/`)

- **SOURCE_DOCUMENTS_GUIDE.md** - Complete guide to accessing all source PDFs
  - Download links for ICE 2003-2017 PDF
  - URLs for all 77 individual FY2018–FY2025 death reports (plus public reporting updates for CY2025 and January 2026)
  - ADP data sources

---

## Key Findings

### All 272 Deaths (FY2004–Jan 2026)

**Demographics:**
- 249 male (91.5%), 23 female (8.5%)
- 55 deaths in IGSA facilities (20.1%)
- 43 deaths in contract facilities (15.7%)

**Mortality Rates by Administration (through Jan 19, 2026; FY-weighted ADP):**
- Bush (2001-2009): 73.35 per 100k (99 deaths)
- Obama (2009-2017): 24.81 per 100k (67 deaths)
- Trump 1 (2017-2021): 27.48 per 100k (42 deaths)
- Biden (2021-2025): 21.66 per 100k (26 deaths)
- Trump 2 (2025–Jan 19, 2026): 70.46 per 100k (38 deaths; FY-weighted ADP using ICE FY2025/FY2026 means)

**Cause of Death (FY2018–2026, n=100):**
- Cardiovascular: 20 deaths (20.0%)
- Infectious disease: 23 deaths (23.0%)
- Suicide: 16 deaths (16.0%)
- Neurologic: 7 deaths (7.0%)
- Other/undetermined: 34 deaths (34.0%)

---

## For Medical Reviewers

### Complete Cause of Death Data

**All 272 deaths have cause of death information** extracted from official ICE reports and public reporting updates:

- **FY2003-2017 (172 deaths):** Cause listed in ICE master PDF
- **FY2018-2025 (77 deaths):** Detailed cause in individual death reports
- **CY2025 + Jan 2026 (23 deaths):** Cause summarized from public reporting with linked sources

### How to Review Individual Deaths

1. Open `data/all_272_deaths_detailed.csv`
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

✓ **Complete roster:** All 272 deaths included (172 from 2003-2017 FOIA PDF, 77 individual PDFs for 2018-2025, 23 public reporting updates for CY2025 and January 2026)
✓ **Cause data present:** Each death retains the ICE-reported cause (preliminary or final as provided)
✓ **Verifiable:** Every death now has a downloaded source PDF in `death_report_pdfs/`
✓ **Reproducible code:** Scripts regenerate rates and figures; see `replication_code/`

### To Verify the Data

1. Download ICE 2003-2017 PDF: https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf
2. Compare with `all_272_deaths_detailed.csv` (172 deaths)
3. Visit ICE death reporting page: https://www.ice.gov/detain/detainee-death-reporting
4. Compare with `all_272_deaths_detailed.csv` (77 individual FY2018–FY2025 reports)
5. Cross-check public reporting updates (CY2025 and January 2026) using the linked sources in `all_272_deaths_detailed.csv`
6. Total: 272 deaths ✓

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

> Mortality in U.S. Immigration and Customs Enforcement Detention, Fiscal Years 2004-2025: An Epidemiological Analysis. [Journal], 2025.

---

## Contact

For questions about the data or methodology, refer to:
- Manuscript and appendix for complete methods
- Source documents guide for data sources
- Medical review summary for clinical analysis

---

**Package Version:** 2.3 (Complete - All 272 Deaths)
**Last Updated:** January 2026 (age and facility location fully populated for all 272 deaths via FOIA PDF extraction, ICE individual reports, and public reporting updates)
**Total Deaths:** 272 (FY2004–Jan 2026)
**Complete Data:** 100%
