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
│   ├── reporting/              # EOD reporting scripts
│   │   ├── generate_eod_report.py
│   │   └── upload_to_gdrive.py
│   ├── verification/           # Verification scripts
│   │   ├── verify_test_cases.py
│   │   └── detailed_verification.py
│   ├── common/                 # Shared utilities
│   │   ├── excel_utils.py
│   │   └── docx_utils.py
│   └── tests/                  # Unit tests
│       └── test_eod_generator.py
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

#### Reporting Scripts (scripts/reporting/)
- **generate_eod_report.py** - Generates professional EOD reports from YAML input
- **upload_to_gdrive.py** - Uploads EOD reports to Google Drive with OAuth2

#### Verification Scripts (scripts/verification/)
- **verify_test_cases.py** - Verifies test cases were added correctly
- **detailed_verification.py** - Detailed verification with statistics

#### Common Utilities (scripts/common/)
- **excel_utils.py** - Centralized Excel file handling and path resolution
- **docx_utils.py** - Centralized DOCX file handling and path resolution

#### Tests (scripts/tests/)
- **test_eod_generator.py** - Unit tests for EOD report generator

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

### Generating EOD Reports

```bash
# Create EOD input file from template
cp documentation/templates/eod_input_template.yaml eod_inputs/my_eod.yaml

# Edit eod_inputs/my_eod.yaml with your testing notes

# Generate report
python scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml

# Preview without saving (dry-run)
python scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml --dry-run

# Archive old reports (older than 30 days)
python scripts/reporting/generate_eod_report.py --archive --days 30
```

### Uploading to Google Drive

**Note:** Requires one-time setup - see [GOOGLE_DRIVE_SETUP.md](GOOGLE_DRIVE_SETUP.md)

```bash
# Upload EOD report to Google Drive
python scripts/reporting/upload_to_gdrive.py --upload documentation/reports/EOD_2025-11-10_nico.docx

# Upload and delete yesterday's EOD
python scripts/reporting/upload_to_gdrive.py \
    --upload documentation/reports/EOD_2025-11-10_nico.docx \
    --delete-yesterday \
    --tester nico

# List files in Google Drive
python scripts/reporting/upload_to_gdrive.py --list
```

## Key Features

1. **Organized Structure** - Clear separation of test cases, documentation, and scripts
2. **Backup Management** - Separate folders for current and backup files
3. **Automated Scripts** - Python automation for analysis, formatting, and verification
4. **EOD Report Generation** - YAML-based professional EOD reports with automatic archival
5. **Google Drive Integration** - OAuth2-authenticated upload with automatic cleanup
6. **Centralized Utilities** - Dynamic path resolution for cross-platform compatibility
7. **Comprehensive Testing** - Unit tests for critical functionality
8. **Comprehensive Documentation** - Detailed guides for setup and usage

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

1. **Clone and Setup**
   ```bash
   cd /home/onik/proyects/AI/Hello_Britannica/
   pip install -r requirements.txt
   ```

2. **Review Test Cases**
   - Open `test_cases/current/Hello Master test cases.xlsx`

3. **Run Analysis**
   ```bash
   python scripts/analysis/analyze_excel.py
   ```

4. **Generate EOD Report**
   ```bash
   # Copy template
   cp documentation/templates/eod_input_template.yaml eod_inputs/my_eod.yaml

   # Edit my_eod.yaml with your testing notes

   # Generate report
   python scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml
   ```

5. **Setup Google Drive (Optional)**
   - Follow the guide in [GOOGLE_DRIVE_SETUP.md](GOOGLE_DRIVE_SETUP.md)
   - Upload EOD reports automatically to your Google Drive

## Dependencies

- Python 3.7 or higher
- openpyxl (Excel file handling)
- python-docx (Word document handling)
- PyYAML (YAML parsing)
- Google API client libraries (for Google Drive integration)

Install all dependencies:
```bash
# Install Python 3 (if not already installed)
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Install project dependencies
pip install -r requirements.txt
```

## Contact

For questions or issues related to this project, please refer to the documentation in the `documentation/` folder.
