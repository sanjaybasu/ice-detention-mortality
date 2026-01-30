# How to Access Death Report PDFs

## Important Note

All source PDFs (FOIA 2003-2017 master file and 77 individual FY2018-2025 reports) have been downloaded to this folder for offline verification. The URLs remain publicly accessible in case new versions are posted. Public reporting updates for CY2025 and January 2026 are linked in the data files but do not have ICE PDF reports.

---

## Method 1: Access Individual PDFs from the CSV File

### Step 1: Open the Data File

Open `../data/detailed_death_data.csv` in Excel, Google Sheets, or any CSV viewer.

### Step 2: Click the PDF URL

Each row has a "PDF URL" column. Simply click the URL to open the death report in your browser.

**Example URLs:**
- https://www.ice.gov/doclib/foia/reports/ddrMirimanianGourgen.pdf
- https://www.ice.gov/doclib/foia/reports/ddrRomeroRonalFranciscoAkaCruzRonald.pdf
- https://www.ice.gov/doclib/foia/reports/ddrAyalaUribeIsmael.pdf

### Step 3: Save the PDF

Once the PDF opens in your browser:
1. Click the download icon in the PDF viewer
2. Save to your computer
3. Rename if desired

---

## Method 2: Access All PDFs from ICE Website

### For FY2018-2025 Deaths (77 individual reports)

1. Visit: https://www.ice.gov/detain/detainee-death-reporting
2. Click on the fiscal year (e.g., "FY 2025", "FY 2024")
3. Click on the individual's name
4. The death report PDF will open in your browser
5. Download and save

### For FY2003-2017 Deaths (172 deaths in one PDF)

1. Visit: https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf
2. The master PDF will open (35 pages)
3. Download and save
4. All 172 deaths are listed in a table format

---

## What's in Each Death Report?

### FY2018-2025 Individual Reports

Each PDF contains:

1. **General Demographic/Background Information**
   - Date of Birth
   - Date of Death
   - Age
   - Sex
   - Country of Citizenship
   - Marital Status
   - Children

2. **Immigration History**
   - Entry information
   - Visa status
   - Removal proceedings
   - Detention timeline

3. **Criminal History**
   - Arrests
   - Convictions
   - Sentences

4. **Medical History** ← **CAUSE OF DEATH IS HERE**
   - Pre-existing conditions
   - Medical care in detention
   - **Preliminary/Final Cause of Death**
   - Autopsy findings (if available)

### FY2003-2017 Master PDF

The master PDF contains a table with columns:
- Name
- Sex
- Date of Birth
- Country
- Date of Death
- Hospital
- Facility
- **FINAL CAUSE OF DEATH** ← Listed in dedicated column

---

## Cause of Death Information

### Is it Adjudicated?

**FY2003-2017:** YES
- Listed as "FINAL CAUSE OF DEATH" in official ICE report
- These are official determinations from medical examiners/coroners

**FY2018-2025:** MIXED
- Some reports list "Final Cause of Death" (adjudicated)
- Some reports list "Preliminary Cause of Death" (pending autopsy)
- Some reports state "Pending Autopsy and Medical Examiner Report"

### Where Does It Come From?

The cause of death information comes from:
1. **Medical Examiner Reports** - Official autopsy findings
2. **Coroner Reports** - Official death investigations
3. **Hospital Records** - For deaths in medical facilities
4. **Preliminary Medical Assessments** - Initial determinations pending full autopsy

---

## Verification Process

### To Verify a Specific Death

1. Open `../data/all_272_deaths_detailed.csv`
2. Find the death of interest
3. Note the "Cause_of_Death" listed
4. Click the "PDF_URL" to open the source document
5. For FY2018-2025: Check the "Medical History" section
6. For FY2003-2017: Check the "FINAL CAUSE OF DEATH" column in the table
7. Verify the cause matches the CSV

### To Verify All Deaths

**FY2003-2017 (172 deaths):**
1. Download: https://www.ice.gov/doclib/foia/reports/detaineedeaths-2003-2017.pdf
2. Compare the "FINAL CAUSE OF DEATH" column with the CSV
3. All 172 deaths should match

**FY2018-2025 (77 deaths):**
1. Visit: https://www.ice.gov/detain/detainee-death-reporting
2. Access each individual death report
3. Check the "Medical History" section for cause of death
4. Compare with the CSV
5. All 77 deaths should match

---

## Why Can't PDFs Be Downloaded Automatically?

The ICE website implements security measures that prevent automated downloading:
- Requires browser session cookies
- May use CAPTCHA or rate limiting
- Designed to prevent bulk scraping

However, **all PDFs are publicly accessible** through a standard web browser.

---

## Bulk Download Instructions

If you need to download all 77 individual PDFs:

### Option 1: Manual Download (Recommended)

1. Open `../data/detailed_death_data.csv`
2. For each row, click the PDF URL
3. Save the PDF with a descriptive filename
4. Estimated time: ~30-45 minutes for all 77

### Option 2: Browser Extension

Use a browser extension like "DownThemAll" or "Tab Save" to:
1. Open all 77 URLs in separate tabs
2. Batch download all PDFs at once
3. Requires: Firefox or Chrome with extension installed

---

## Summary

✓ **All ICE source PDFs (FOIA master + 77 individual reports) are cached locally in this folder**  
✓ **URLs are provided in the CSV files for verification**  
✓ **FY2003-2017: Single PDF with all 172 deaths**  
✓ **FY2018-2025: 77 individual PDF reports**

---

**For Questions:** See `../CAUSE_OF_DEATH_SOURCES.md` for detailed documentation of cause of death sources and adjudication status.
