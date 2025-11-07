# Test Case Management Scripts

This directory contains Python scripts for managing test cases in the Hello Britannica project.

## Prerequisites

### Install Python and Dependencies

```bash
# Install Python 3 (if not already installed)
sudo apt install python3 python3-pip python3-venv

# Install required packages
pip3 install -r ../requirements.txt
```

## Directory Structure

```
scripts/
├── common/             # Shared utilities
│   ├── __init__.py
│   ├── excel_utils.py  # Common Excel operations and path management
│   └── docx_utils.py   # Common DOCX operations and path management
├── analysis/           # Analysis and modification scripts
│   ├── analyze_excel.py
│   ├── analyze_excel_files.py
│   └── add_test_cases.py
├── formatting/         # Formatting scripts
│   ├── formatting_summary.py
│   ├── restore_formatting.py
│   └── verify_formatting.py
├── verification/       # Verification scripts
│   ├── verify_test_cases.py
│   └── detailed_verification.py
├── reporting/          # EOD report generation
│   └── generate_eod_report.py
└── tests/              # Unit tests
    └── test_eod_generator.py
```

## Available Scripts

### Analysis Scripts

#### `analysis/analyze_excel.py`
Analyzes the structure of the current Excel test case file.

```bash
python3 scripts/analysis/analyze_excel.py
```

#### `analysis/add_test_cases.py`
Adds new test cases from markdown to the Excel file.

```bash
python3 scripts/analysis/add_test_cases.py
```

### Verification Scripts

#### `verification/verify_test_cases.py`
Quick verification of test cases.

```bash
python3 scripts/verification/verify_test_cases.py
```

#### `verification/detailed_verification.py`
Detailed verification report of all added test cases.

```bash
python3 scripts/verification/detailed_verification.py
```

### Formatting Scripts

#### `formatting/formatting_summary.py`
Generate formatting details summary.

```bash
python3 scripts/formatting/formatting_summary.py
```

#### `formatting/restore_formatting.py`
Restore original formatting while preserving new content.

```bash
python3 scripts/formatting/restore_formatting.py
```

#### `formatting/verify_formatting.py`
Verify that formatting was properly restored.

```bash
python3 scripts/formatting/verify_formatting.py
```

### Reporting Scripts

#### `reporting/generate_eod_report.py`
Generate professional End-of-Day (EOD) reports from structured YAML input.

**Features:**
- YAML-based structured input (replaces manual text editing)
- Automatic tester name detection from git config
- Flexible date parsing (multiple formats supported)
- Dry-run mode for previewing reports
- Automatic archival of old reports
- Full template validation and error handling

**Quick Start:**

```bash
# Create your EOD notes file (YAML format)
cp documentation/templates/eod_input_template.yaml my_eod.yaml
# Edit my_eod.yaml with your testing notes

# Generate the report
python3 scripts/reporting/generate_eod_report.py my_eod.yaml

# Preview without saving (dry-run)
python3 scripts/reporting/generate_eod_report.py my_eod.yaml --dry-run

# Archive old reports (older than 30 days)
python3 scripts/reporting/generate_eod_report.py --archive --days 30
```

**YAML Input Format:**

```yaml
date: "06-11-2025"  # Supports: DD-MM-YYYY, YYYY-MM-DD, MM/DD/YYYY, "Month DD, YYYY"

product:
  name: "Hello Britannica"
  platforms:
    - "Web (Chrome – Stage)"
    - "iOS App – iPhone 12 Pro Max (version 4.2.7 – Stage)"
  roles_tested: ["Student", "Teacher"]

areas_covered:
  - "Completed regression testing on iOS staging version 4.2.7"
  - "Verified overall stability and performance"

bugs: []  # Leave empty if no bugs found

bug_fixes: []  # Leave empty if no fixes verified

requirements: []  # Leave empty if no requirements confirmed

next_steps:
  - "Continue with regression testing"

status: "Regression testing completed successfully. All functionalities appear stable."
```

**Command-line Options:**

```bash
# Generate from YAML
python3 scripts/reporting/generate_eod_report.py <input.yaml>

# Custom output location
python3 scripts/reporting/generate_eod_report.py input.yaml --output custom_report.docx

# Dry-run mode (preview only, don't save)
python3 scripts/reporting/generate_eod_report.py input.yaml --dry-run

# Archive old reports
python3 scripts/reporting/generate_eod_report.py --archive --days 30

# Preview archival without moving files
python3 scripts/reporting/generate_eod_report.py --archive --days 30 --dry-run
```

**Output:**
- Reports are saved to `documentation/reports/`
- Filename format: `EOD_YYYY-MM-DD_TesterName.docx`
- Archived reports go to `documentation/reports/archive/YYYY-MM/`

## Common Utilities

All scripts use shared utilities for consistency and reliability.

### Excel Utilities (`common/excel_utils.py`)

- **Path Management**: Centralized path resolution (no more hardcoded paths)
- **Error Handling**: Proper exception handling and user feedback
- **Safe Operations**: Safe loading and saving of Excel files
- **Type Hints**: Better code documentation and IDE support

**Key Functions:**
- `get_project_root()` - Get project root directory
- `get_excel_path()` - Get path to main Excel file
- `load_excel_safely()` - Load Excel with error handling
- `save_excel_safely()` - Save Excel with error handling
- `print_section_header()` - Formatted output headers

### DOCX Utilities (`common/docx_utils.py`)

- **Path Management**: Centralized paths for templates and reports
- **Error Handling**: Safe DOCX operations with proper error messages
- **Archive Support**: Path helpers for report archival

**Key Functions:**
- `get_template_path()` - Get path to DOCX templates
- `get_report_output_path()` - Get path for report output
- `get_report_archive_path()` - Get path for archived reports
- `load_docx_safely()` - Load DOCX with error handling
- `save_docx_safely()` - Save DOCX with error handling

## Recent Improvements

### Fixed Issues

1. **Removed Hardcoded Windows Paths** - All scripts now use dynamic path resolution
2. **Consistent Shebangs** - All scripts use `#!/usr/bin/env python3`
3. **Added requirements.txt** - Proper dependency management
4. **Improved Error Handling** - Better error messages and exception handling
5. **Reduced Code Duplication** - Shared utilities in `common/` directory

### Benefits

- **Portable**: Works on any platform (Windows, Linux, macOS)
- **Maintainable**: Common code in one place
- **Reliable**: Proper error handling prevents silent failures
- **Type-safe**: Type hints for better code quality

## Error Handling

All scripts now:
- Check if files exist before processing
- Provide clear error messages to stderr
- Return proper exit codes (0 for success, 1 for failure)
- Include stack traces for debugging

## Example Usage

```bash
# Install dependencies
pip3 install -r requirements.txt

# Analyze current test cases
python3 scripts/analysis/analyze_excel.py

# Verify test cases
python3 scripts/verification/verify_test_cases.py

# Get detailed verification
python3 scripts/verification/detailed_verification.py
```

## Notes

- All scripts expect to be run from the project root or directly via their path
- Excel files should not be open in other applications when running scripts
- Output files are saved to appropriate directories (data/, test_cases/current/, etc.)
