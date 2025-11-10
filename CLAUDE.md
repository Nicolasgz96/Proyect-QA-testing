# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a QA test case management system for the Hello Britannica application. The project manages Excel-based test cases with Python automation scripts for analysis, formatting restoration, verification, and EOD report generation.

## Development Setup

### Prerequisites
```bash
# Install Python 3 and dependencies
sudo apt install python3 python3-pip python3-venv

# Install required packages
pip3 install -r requirements.txt
```

### Running Scripts
All scripts must be run from the project root directory:

```bash
# Analysis
python3 scripts/analysis/analyze_excel.py
python3 scripts/analysis/add_test_cases.py

# Verification
python3 scripts/verification/verify_test_cases.py
python3 scripts/verification/detailed_verification.py

# Formatting
python3 scripts/formatting/restore_formatting.py
python3 scripts/formatting/verify_formatting.py
python3 scripts/formatting/formatting_summary.py

# EOD Report Generation
python3 scripts/reporting/generate_eod_report.py my_eod.yaml
python3 scripts/reporting/generate_eod_report.py my_eod.yaml --dry-run
python3 scripts/reporting/generate_eod_report.py --archive --days 30

# Google Drive Upload - Simple Method (File Stream)
./scripts/reporting/upload_eod_simple.sh  # Uploads latest EOD and cleans up old files

# Google Drive Upload - OAuth Method (Advanced - see GOOGLE_DRIVE_SETUP.md)
python3 scripts/reporting/upload_to_gdrive.py --upload documentation/reports/EOD_2025-11-10_nico.docx
python3 scripts/reporting/upload_to_gdrive.py --upload EOD_file.docx --delete-yesterday --tester nico
python3 scripts/reporting/upload_to_gdrive.py --list

# Unit Tests
python3 scripts/tests/test_eod_generator.py
```

## Architecture

### Centralized Path Resolution System
**Critical**: All scripts use centralized path resolution via `scripts/common/` utilities. This provides dynamic path resolution relative to the project root.

**Excel utilities** (`scripts/common/excel_utils.py`):
- `get_project_root()` - Resolves to project root from `scripts/common/`
- `get_excel_path()` - Returns path to main Excel file in `test_cases/current/`
- `get_backup_path()` - Returns path to backup files in `test_cases/backups/`
- `get_data_path()` - Returns path to data files in `data/`
- `load_excel_safely()` / `save_excel_safely()` - Safe Excel operations with error handling

**DOCX utilities** (`scripts/common/docx_utils.py`):
- `get_template_path()` - Returns path to DOCX templates in `documentation/templates/`
- `get_report_output_path()` - Returns path for report output in `documentation/reports/`
- `get_report_archive_path()` - Returns path for archived reports
- `load_docx_safely()` / `save_docx_safely()` - Safe DOCX operations with error handling

**Why this matters**: The project was refactored to eliminate hardcoded Windows paths. All new scripts MUST use these utility functions for path resolution, not hardcoded paths or manual path construction.

### Script Categories

**Analysis scripts** (`scripts/analysis/`):
- Parse and analyze Excel test case files
- Add test cases from markdown format to Excel
- Generate JSON analysis reports to `data/`

**Formatting scripts** (`scripts/formatting/`):
- Restore original Excel formatting while preserving content
- Use `openpyxl` to copy cell styles, borders, fonts, fills, alignments
- Compare original vs modified workbooks

**Verification scripts** (`scripts/verification/`):
- Verify test cases were added correctly
- Check specific test IDs exist in expected sheets
- Generate verification statistics

**Reporting scripts** (`scripts/reporting/`):
- Generate professional End-of-Day (EOD) reports from YAML input
- YAML-based structured input with validation
- Automatic archival of old reports
- Dry-run mode for previewing reports
- Upload EOD reports to Google Drive with OAuth2 authentication
- Automatic deletion of previous day's EOD reports from Google Drive

**Tests** (`scripts/tests/`):
- Unit tests for EOD report generator
- Run with: `python3 scripts/tests/test_eod_generator.py`

### Common Utilities Pattern
All scripts follow this pattern:

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from common.excel_utils import (
    load_excel_safely,
    save_excel_safely,
    get_excel_path,
    print_section_header
)

def main():
    file_path = get_excel_path()  # NOT hardcoded
    wb = load_excel_safely(file_path)  # With error handling
    # ... work ...
    save_excel_safely(wb, file_path)  # Safe save

if __name__ == "__main__":
    main()
```

### Error Handling Convention
All scripts use consistent error handling:
- Print errors to `sys.stderr`
- Return exit code 1 on failure, 0 on success
- Check file existence before processing
- Provide clear, actionable error messages
- Include stack traces when helpful

Example:
```python
try:
    wb = load_excel_safely(file_path)
except FileNotFoundError:
    print(f"Error: File not found at {file_path}", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)
```

## EOD Report Generation (YAML-Based)

### Quick Start
```bash
# Create EOD notes file from template
cp documentation/templates/eod_input_template.yaml my_eod.yaml

# Edit my_eod.yaml with your testing notes

# Generate report
python3 scripts/reporting/generate_eod_report.py my_eod.yaml

# Preview without saving (dry-run)
python3 scripts/reporting/generate_eod_report.py my_eod.yaml --dry-run

# Archive old reports (older than 30 days)
python3 scripts/reporting/generate_eod_report.py --archive --days 30
```

### YAML Input Structure
EOD reports use structured YAML input for flexibility and validation:

```yaml
date: "06-11-2025"  # Supports multiple formats

product:
  name: "Hello Britannica"
  platforms:
    - "Web (Chrome – Stage)"
    - "iOS App – iPhone 12 Pro Max (version 4.2.7 – Stage)"
  roles_tested: ["Student", "Teacher"]

areas_covered:
  - "Completed regression testing on iOS staging version 4.2.7"

bugs: []  # Structured bug reports or empty

bug_fixes: []  # Verified fixes or empty

requirements: []  # Confirmed requirements or empty

next_steps:
  - "Continue with regression testing"

status: "Regression testing completed successfully."
```

### Key Features
- **Content Replacement**: Properly replaces template content (does not append)
- **Flexible Date Parsing**: Supports DD-MM-YYYY, YYYY-MM-DD, MM/DD/YYYY, "Month DD, YYYY"
- **Dynamic Tester Name**: Automatically detects from git config
- **Template Validation**: Validates all required sections exist
- **Archival System**: Automatically archives old reports by month
- **Dry-run Mode**: Preview reports before generating

### Report Output
- Saved to: `documentation/reports/`
- Filename format: `EOD_YYYY-MM-DD_TesterName.docx`
- Archived to: `documentation/reports/archive/YYYY-MM/`

## File Organization

**Main Excel file**: `test_cases/current/Hello Master test cases.xlsx`
- Working copy with sheets: Admin Onboard, Teacher - Email, Security Testing, Negative Scenarios

**Backup files**: `test_cases/backups/`
- `Hello Master test cases - ORIGINAL.xlsx` - Original unmodified version
- `Hello Master test cases_BACKUP.xlsx` - Pre-modification backup

**EOD Templates**: `documentation/templates/`
- `Reports end of the day highlights.docx` - EOD report template (DOCX)
- `eod_input_template.yaml` - YAML input template with examples

**EOD Reports**: `documentation/reports/`
- Generated EOD reports: `EOD_YYYY-MM-DD_TesterName.docx`
- Archived reports: `archive/YYYY-MM/`

**Markdown test case input**: `documentation/reports/New_Test_Cases_To_Add.md`
- Used by `add_test_cases.py` to add new test cases

**Analysis output**: `data/excel_analysis.json`
- Generated by `analyze_excel.py`

## Adding New Scripts

When creating new scripts:

1. **Use the common utilities** - Import from `scripts/common/excel_utils.py` or `scripts/common/docx_utils.py`
2. **Follow the naming convention** - `verb_noun.py` (e.g., `verify_test_cases.py`)
3. **Place in correct category** - analysis/, formatting/, verification/, or reporting/
4. **Add to scripts/README.md** - Document the new script
5. **Use type hints** - Include parameter and return types
6. **Handle errors properly** - Use try/except with stderr output
7. **Return exit codes** - 0 for success, 1 for failure

Template for new scripts:
```python
#!/usr/bin/env python3
"""
Script description here
"""
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from common.excel_utils import (
    load_excel_safely,
    get_excel_path,
    print_section_header
)


def your_function(file_path: Path) -> bool:
    """
    Function description.

    Args:
        file_path: Path to Excel file

    Returns:
        True if successful, False otherwise
    """
    try:
        wb = load_excel_safely(file_path)
        # Your logic here
        wb.close()
        return True
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False


def main():
    """Main entry point."""
    print_section_header("Your Script Title")

    file_path = get_excel_path()

    if not file_path.exists():
        print(f"Error: File not found", file=sys.stderr)
        sys.exit(1)

    success = your_function(file_path)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## Excel File Structure

The main Excel file has these sheets:
- **Admin Onboard** - Admin and teacher onboarding test cases
- **Teacher - Email** - Teacher email functionality tests
- **Security Testing** - Security-related test cases
- **Negative Scenarios** - Negative test scenarios

Each sheet has these columns:
1. `#` - Test case ID (e.g., AO001, TE001, SEC001, NEG001)
2. `Module` - Module name
3. `Tittle` - Test case title (note: typo exists in actual header)
4. `Pre-Conditioin` - Prerequisites (note: typo exists)
5. `Steps to folow` - Test steps (note: typo exists)
6. `Expected results` - Expected outcomes
7. `Pass/Failed` - Test execution result
8. `Notes` - Additional notes

**Important**: When working with Excel headers, use the exact spelling as it appears (including typos) for compatibility.

## Test Case ID Patterns

Test IDs follow these prefixes:
- `AO###` - Admin Onboard
- `TE###` - Teacher Email
- `SEC###` - Security Testing
- `NEG###` - Negative Scenarios

When adding test cases, maintain sequential numbering within each category.

## Git Configuration

Repository is configured for:
- User: nico- (or Nicolasgz96)
- Email: 96.nicolasgonzalez@gmail.com
- Remote: https://github.com/Nicolasgz96/Proyect-QA-testing.git
- Branch: main

## Important Constraints

1. **Never use hardcoded absolute paths** - Always use utilities from `scripts/common/`
2. **Excel files must be closed** - Scripts will fail if files are open in Excel/Word
3. **Run from project root** - Scripts expect to be run from project root directory
4. **Preserve backups** - Never modify files in `test_cases/backups/`
5. **Python 3 only** - All shebangs use `#!/usr/bin/env python3`
6. **Dependencies** - openpyxl (Excel), python-docx (Word), PyYAML (EOD reports)

## Testing Scripts

### Run Unit Tests
```bash
# EOD generator tests (20 test cases)
python3 scripts/tests/test_eod_generator.py
```

### Test Path Resolution
```bash
# Should work without errors
python3 scripts/analysis/analyze_excel.py

# Test error handling (temporarily rename file)
mv "test_cases/current/Hello Master test cases.xlsx" "test_cases/current/backup.xlsx"
python3 scripts/analysis/analyze_excel.py  # Should show clear error
mv "test_cases/current/backup.xlsx" "test_cases/current/Hello Master test cases.xlsx"
```

### Test Verification Scripts
```bash
python3 scripts/verification/verify_test_cases.py
python3 scripts/verification/detailed_verification.py
```

## Architecture Evolution

The codebase has evolved through these major improvements:

1. **Eliminated hardcoded paths** - Created `scripts/common/excel_utils.py` and `scripts/common/docx_utils.py`
2. **Standardized shebangs** - All scripts use `#!/usr/bin/env python3`
3. **Added dependency management** - Created `requirements.txt`
4. **Improved error handling** - Comprehensive try/except blocks with specific exceptions
5. **Added EOD reporting** - YAML-based structured input with validation and archival
6. **Added unit tests** - Test coverage for critical functionality
7. **Created reporting category** - `scripts/reporting/` for EOD report generation

When reviewing old commits, be aware that the architecture has significantly changed from the original flat structure with hardcoded paths to the current organized, portable structure with centralized utilities.
