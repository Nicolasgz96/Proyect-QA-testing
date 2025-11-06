# Hello Britannica - QA Test Management Project

This project contains test cases, automation scripts, and documentation for the Hello Britannica application quality assurance process.

## Project Structure

```
Hello_Britannica/
├── test_cases/                  # Excel test case files
│   ├── current/                 # Current working version
│   │   └── Hello Master test cases.xlsx
│   └── backups/                 # Backup versions
│       ├── Hello Master test cases - ORIGINAL.xlsx
│       └── Hello Master test cases_BACKUP.xlsx
│
├── documentation/               # Documentation and reports
│   ├── user_journeys/          # User journey documents
│   │   └── User Journeys - Hello Britannica.docx
│   ├── templates/              # Document templates
│   │   └── Bug Template for Jira.docx
│   ├── reports/                # QA analysis reports
│   │   ├── QA_Test_Coverage_Gap_Analysis_Report.md
│   │   ├── Executive_Summary_QA_Analysis.md
│   │   ├── TEST_CASES_ADDITION_SUMMARY.md
│   │   ├── FORMATTING_RESTORATION_REPORT.md
│   │   └── New_Test_Cases_To_Add.md
│   └── QUICK_REFERENCE.txt
│
├── scripts/                     # Python automation scripts
│   ├── analysis/               # Analysis scripts
│   │   ├── analyze_excel.py
│   │   ├── analyze_excel_files.py
│   │   └── add_test_cases.py
│   ├── formatting/             # Formatting scripts
│   │   ├── restore_formatting.py
│   │   ├── verify_formatting.py
│   │   └── formatting_summary.py
│   └── verification/           # Verification scripts
│       ├── verify_test_cases.py
│       └── detailed_verification.py
│
└── data/                        # JSON and other data files
    └── excel_analysis.json

```

## File Inventory

### Test Cases
- **test_cases/current/Hello Master test cases.xlsx** - Main working test case file
- **test_cases/backups/Hello Master test cases - ORIGINAL.xlsx** - Original unmodified version
- **test_cases/backups/Hello Master test cases_BACKUP.xlsx** - Backup before formatting changes

### Documentation
- **User Journeys** - User journey documentation for Hello Britannica
- **Bug Template** - Jira bug reporting template
- **QA Reports** - Multiple analysis and summary reports

### Python Scripts

#### Analysis Scripts (scripts/analysis/)
- **analyze_excel.py** - Analyzes Excel file structure and generates JSON report
- **analyze_excel_files.py** - Compares original and modified Excel files
- **add_test_cases.py** - Adds new test cases from markdown to Excel

#### Formatting Scripts (scripts/formatting/)
- **restore_formatting.py** - Restores original formatting to modified Excel files
- **verify_formatting.py** - Verifies formatting was properly restored
- **formatting_summary.py** - Provides detailed formatting summary

#### Verification Scripts (scripts/verification/)
- **verify_test_cases.py** - Verifies test cases were added correctly
- **detailed_verification.py** - Detailed verification with statistics

## Usage

### Running Analysis Scripts

From the project root directory:

```bash
# Analyze Excel file structure
python scripts/analysis/analyze_excel.py

# Compare Excel files
python scripts/analysis/analyze_excel_files.py

# Add test cases from markdown
python scripts/analysis/add_test_cases.py
```

### Running Formatting Scripts

```bash
# Restore original formatting
python scripts/formatting/restore_formatting.py

# Verify formatting restoration
python scripts/formatting/verify_formatting.py

# Get formatting summary
python scripts/formatting/formatting_summary.py
```

### Running Verification Scripts

```bash
# Verify test cases
python scripts/verification/verify_test_cases.py

# Detailed verification
python scripts/verification/detailed_verification.py
```

## Key Features

1. **Organized Structure** - Clear separation of test cases, documentation, and scripts
2. **Backup Management** - Separate folders for current and backup files
3. **Automated Scripts** - Python automation for analysis, formatting, and verification
4. **Relative Paths** - All scripts use relative paths for portability
5. **Comprehensive Documentation** - Detailed reports and user journeys

## Script Highlights

### Test Case Management
- Automated addition of test cases from markdown format
- Verification of test case integrity
- Analysis of test coverage gaps

### Formatting Tools
- Restoration of Excel formatting while preserving content
- Verification of formatting accuracy
- Detailed formatting analysis

### Analysis Tools
- Excel structure analysis with JSON output
- File comparison capabilities
- Test case statistics and reporting

## Notes

- All Python scripts are configured to work from any location within the project
- File paths are resolved relative to the script location
- Backup files are preserved for safety
- JSON analysis data is stored in the data/ folder

## Reports Available

1. **QA Test Coverage Gap Analysis Report** - Comprehensive gap analysis
2. **Executive Summary QA Analysis** - High-level summary for stakeholders
3. **Test Cases Addition Summary** - Details of added test cases
4. **Formatting Restoration Report** - Report on formatting operations
5. **New Test Cases To Add** - Proposed test cases in markdown format

## Maintenance

- Keep the current test case file in `test_cases/current/`
- Create backups before major changes in `test_cases/backups/`
- Store analysis output in `data/`
- Document new processes in `documentation/reports/`

## Getting Started

1. Navigate to the project directory: `cd /home/onik/proyects/AI/Hello_Britannica/`
2. Review the test cases: Open `test_cases/current/Hello Master test cases.xlsx`
3. Run analysis: `python scripts/analysis/analyze_excel.py`
4. Check documentation: Review files in `documentation/reports/`

## Dependencies

- Python 3.x
- openpyxl library (for Excel file handling)

Install dependencies:
```bash
pip install openpyxl
```

## Contact

For questions or issues related to this project, please refer to the documentation in the `documentation/` folder.
