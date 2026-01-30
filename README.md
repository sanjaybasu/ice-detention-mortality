# ICE Detention Mortality Analysis

This package contains analysis of 272 in-custody deaths in U.S. Immigration and Customs Enforcement (ICE) detention from fiscal year 2004 through January 19, 2026, with cause of death information.


---


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

272 Deaths 

- all_272_deaths_detailed.csv - PRIMARY DATA FILE
  - Columns: Name, Sex, Age, Country, Date of Death, Cause of Death, Facility Name, Facility Location, Facility Type, PDF URL, Period
  - Cause of death information
  - Source PDF URL for verification

Supporting Data Files:

- complete_death_records.csv - Basic death records (name, date, fiscal year, administration)
- detailed_death_data.csv - Detailed data for FY2018–2026 (100 deaths)
- average_daily_population.csv - ADP data by fiscal year
- mortality_rates_by_administration.csv - Calculated mortality rates

Replication Code (`replication_code/`)

Python scripts to reproduce analyses:
- 01_data_extraction.py - Verifies data extraction
- 02_calculate_mortality_rates.py - Calculates mortality rates
- 03_generate_figures.py - Generates figures

Medical Review (`medical_review/`)

- COMPLETE_MEDICAL_REVIEW.md - medical analysis through FY2025 (public reporting updates for January 2026 not yet incorporated)
  - Cause of death analysis
  - Facility-specific patterns
  - Temporal trends
  - Recommendations for review

Source Documents (`source_documents/`)

- SOURCE_DOCUMENTS_GUIDE.md - guide to accessing source PDFs
  - Download links for ICE 2003-2017 PDF
  - URLs for 77 individual FY2018–FY2025 death reports (plus public reporting updates for CY2025 and January 2026)
  - ADP data sources


