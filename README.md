# ICE Detention Mortality Analysis

This package contains comprehensive analysis of 272 in-custody deaths in U.S. Immigration and Customs Enforcement (ICE) detention from fiscal year 2004 through January 19, 2026, with complete cause of death information for every death.

 All 272 deaths cataloged (FY2004–Jan 2026) from official ICE sources and public reporting updates
 
 Cause of death for every death (verbatim from ICE PDFs; preliminary vs. final noted in source docs)
 
 Facility name and type for all deaths; age and facility location fully populated for all 272 deaths (FY2003–2017 and FY2018–2025, with public reporting updates for CY2025 and January 2026)
 
 Source PDFs downloaded to `death_report_pdfs/` for offline verification
 
 Medical review summary - Comprehensive clinical analysis (with noted data gaps)
 

---

## Quick Start

### For Medical Reviewers

Start here: `medical_review/COMPLETE_MEDICAL_REVIEW.md`
- Comprehensive analysis through FY2025 (public reporting updates for January 2026 not yet incorporated)
- Cause of death breakdown
- Facility-specific patterns
- Recommendations for further review

Primary data file: `data/all_272_deaths_detailed.csv`
- All 272 deaths with complete details
- Includes PDF URLs for source verification

### For Researchers

Replication code: `replication_code/` directory
- Complete Python scripts to reproduce all analyses

### For Data Verification

Source documents guide: `source_documents/SOURCE_DOCUMENTS_GUIDE.md`
- Direct download links for all ICE reports
- Instructions for verifying every data point

---

## Package Contents

Data Files (`data/`)

NEW: All 272 Deaths with Complete Details

- all_272_deaths_detailed.csv - PRIMARY DATA FILE
  - All 272 deaths (FY2004–Jan 2026)
  - Columns: Name, Sex, Age, Country, Date of Death, Cause of Death, Facility Name, Facility Location, Facility Type, PDF URL, Period
  - Every death includes cause of death information
  - Every death includes source PDF URL for verification

Supporting Data Files:

- complete_death_records.csv - Basic death records (name, date, fiscal year, administration)
- detailed_death_data.csv - Detailed data for FY2018–2026 (100 deaths)
- average_daily_population.csv - ADP data by fiscal year
- mortality_rates_by_administration.csv - Calculated mortality rates

Replication Code (`replication_code/`)

Complete Python scripts to reproduce all analyses:
- 01_data_extraction.py - Verifies data extraction
- 02_calculate_mortality_rates.py - Calculates mortality rates
- 03_generate_figures.py - Generates figures

Medical Review (`medical_review/`)

- COMPLETE_MEDICAL_REVIEW.md - Comprehensive medical analysis through FY2025 (public reporting updates for January 2026 not yet incorporated)
  - Cause of death analysis
  - Facility-specific patterns
  - Temporal trends
  - Recommendations for review

Source Documents (`source_documents/`)

- SOURCE_DOCUMENTS_GUIDE.md - Complete guide to accessing all source PDFs
  - Download links for ICE 2003-2017 PDF
  - URLs for all 77 individual FY2018–FY2025 death reports (plus public reporting updates for CY2025 and January 2026)
  - ADP data sources


