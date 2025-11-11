# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Hello Britannica QA Test Management System - Excel-based test case management with Python automation for analysis, formatting, verification, and professional EOD report generation with Google Drive integration.

## Essential Commands

### Environment Setup
```bash
# Validate environment before starting work
python3 scripts/check_environment.py

# Install dependencies (pinned versions)
pip3 install -r requirements.txt
```

### Common Development Tasks
```bash
# Run all EOD generator unit tests
python3 scripts/tests/test_eod_generator.py

# Analyze Excel test cases
python3 scripts/analysis/analyze_excel.py

# Generate EOD report from YAML
python3 scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml

# Preview EOD report without saving
python3 scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml --dry-run

# Upload EOD to Google Drive (simple method - Windows/WSL only)
./scripts/reporting/upload_eod_simple.sh

# Upload EOD to Google Drive (OAuth method - cross-platform)
python3 scripts/reporting/upload_to_gdrive.py --upload documentation/reports/EOD_file.docx

# Generate bug report (creates DOCX and uploads to Google Drive)
# Note: Use Windows Python launcher for WSL environments
/mnt/c/Windows/py.exe scripts/reporting/create_bug_report.py
```

## Architecture Overview

### Centralized Path Resolution (CRITICAL)
**All scripts MUST use centralized utilities from `scripts/common/` - never hardcode paths.**

The project uses a three-tier path resolution system:

1. **`scripts/common/path_utils.py`** - Core path resolver
   - `get_project_root()` - Returns project root dynamically from any script location
   - Used by both excel_utils and docx_utils

2. **`scripts/common/excel_utils.py`** - Excel-specific paths and operations
   - `get_excel_path()` - Main Excel file in `test_cases/current/`
   - `get_backup_path()` - Backup files in `test_cases/backups/`
   - `load_excel_safely()` / `save_excel_safely()` - Safe operations with error handling

3. **`scripts/common/docx_utils.py`** - DOCX-specific paths and operations
   - `get_template_path()` - Templates in `documentation/templates/`
   - `get_report_output_path()` - Reports in `documentation/reports/`
   - `load_docx_safely()` / `save_docx_safely()` - Safe operations with error handling

**Why this matters**: The project was refactored to eliminate hardcoded Windows paths. Import path resolution from `path_utils`, never duplicate `get_project_root()`.

### Script Import Pattern
All scripts use this pattern to enable imports from `common/`:

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

# Add scripts/ to path for common imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from common.path_utils import get_project_root
from common.excel_utils import load_excel_safely, get_excel_path
```

### Script Categories

**`scripts/analysis/`** - Excel test case analysis
- Parse Excel structure, compare files, add test cases from markdown

**`scripts/formatting/`** - Excel formatting preservation
- Restore formatting using openpyxl while preserving content changes

**`scripts/verification/`** - Test case validation
- Verify test cases added correctly, check test IDs, generate statistics

**`scripts/reporting/`** - EOD report generation, bug report generation, and upload
- `generate_eod_report.py` - YAML → Professional DOCX conversion for EOD reports
- `create_bug_report.py` - Generate Jira-formatted bug reports as DOCX files
- `upload_eod_simple.sh` - Simple Google Drive upload (Windows/WSL with Google Drive for Desktop)
- `upload_to_gdrive.py` - OAuth2-based Google Drive integration (cross-platform)
- Automatic archival and cleanup

**`scripts/common/`** - Shared utilities
- **CRITICAL**: `path_utils.py` - Centralized path resolution
- `excel_utils.py` - Excel operations
- `docx_utils.py` - DOCX operations

**`scripts/tests/`** - Unit tests
- Test coverage for EOD generator (20 test cases)

## EOD Report Workflow

### YAML-Based Input System
EOD reports use structured YAML input (NOT plain text notes):

```yaml
date: "10-11-2025"  # Flexible: DD-MM-YYYY, YYYY-MM-DD, MM/DD/YYYY

product:
  name: "Hello Britannica"
  platforms:
    - "Web (Chrome – Stage)"
    - "iOS App – iPhone 12 Pro Max (version 4.2.7 – Stage)"
  roles_tested: ["Student", "Teacher"]

areas_covered:
  - "Tested student login flow on iOS staging"
  - "Verified dashboard functionality"

bugs: []  # Empty or structured bug list

bug_fixes:
  - title: "Password reset functionality"
    status: "Verified"

next_steps:
  - "Continue regression testing"

status: "Testing completed successfully."
```

### Generation Process
1. Create YAML in `eod_inputs/` (gitignored directory)
2. Run generator: `python3 scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml`
3. Output: `documentation/reports/EOD_YYYY-MM-DD_TesterName.docx`
4. Upload: `./scripts/reporting/upload_eod_simple.sh` (Windows/WSL) or OAuth method

**Key Features**:
- Template validation ensures all 7 sections exist
- Date parsing supports multiple formats
- Tester name auto-detected from git config
- Dry-run mode for preview: `--dry-run`
- Archival: `--archive --days 30`

## Google Drive Integration

### Two Methods Available

**Simple Method** (Windows/WSL with Google Drive for Desktop):
- Direct file copy to `G:\My Drive\Daily reports\` (for EOD reports)
- Direct file copy to `G:\My Drive\Bug Reports\` (for bug reports)
- Script: `./scripts/reporting/upload_eod_simple.sh` (for EOD reports)
- Uses PowerShell commands for bug report uploads
- Automatic cleanup of files older than 7 days
- **Limitation**: Windows-only (requires Google Drive for Desktop installed)

**OAuth Method** (Cross-platform):
- Uses Google Drive API with OAuth2
- Script: `scripts/reporting/upload_to_gdrive.py`
- Requires one-time setup (see `GOOGLE_DRIVE_SETUP.md`)
- Works on any platform
- Can specify custom folders with `--folder` parameter

## Excel File Structure

**Main File**: `test_cases/current/Hello Master test cases.xlsx`

Sheets:
- Admin Onboard (AO### test IDs)
- Teacher - Email (TE### test IDs)
- Security Testing (SEC### test IDs)
- Negative Scenarios (NEG### test IDs)

**IMPORTANT**: Column headers contain typos that MUST be preserved for compatibility:
- `Tittle` (not "Title")
- `Pre-Conditioin` (not "Pre-Condition")
- `Steps to folow` (not "Steps to follow")

Always use exact header names when accessing columns programmatically.

## Error Handling Pattern

All scripts follow this convention:
```python
def main():
    try:
        file_path = get_excel_path()
        wb = load_excel_safely(file_path)
        # ... work ...
        success = save_excel_safely(wb, file_path)
        return 0 if success else 1
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

- Print errors to `sys.stderr`
- Return exit code 1 on failure, 0 on success
- Use specific exception types when possible
- Include stack traces for unexpected errors

## Adding New Scripts

Template:
```python
#!/usr/bin/env python3
"""Brief description of what this script does."""
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent.parent))

from common.excel_utils import load_excel_safely, get_excel_path
from common.docx_utils import print_section_header

def process_data(file_path: Path) -> bool:
    """
    Process data from file.

    Args:
        file_path: Path to file

    Returns:
        True if successful, False otherwise
    """
    try:
        wb = load_excel_safely(file_path)
        # ... logic ...
        wb.close()
        return True
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return False

def main():
    print_section_header("Script Title")
    file_path = get_excel_path()

    if not file_path.exists():
        print(f"Error: File not found", file=sys.stderr)
        sys.exit(1)

    success = process_data(file_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
```

Checklist:
- [ ] Use `#!/usr/bin/env python3` shebang
- [ ] Import from `scripts/common/` utilities
- [ ] Use type hints for parameters and returns
- [ ] Follow error handling pattern
- [ ] Return exit codes (0=success, 1=failure)
- [ ] Place in appropriate category directory
- [ ] Use `verb_noun.py` naming convention

## Important Constraints

1. **Never hardcode paths** - Always use `get_project_root()` or utility functions
2. **Excel/Word files must be closed** - Scripts fail if files are open
3. **Run from project root** - Scripts resolve paths relative to project root
4. **Preserve backups** - Never modify `test_cases/backups/` directory
5. **Python 3.7+** - All shebangs specify python3
6. **Dependencies are pinned** - requirements.txt uses exact versions (==), not ranges (>=)

## Dependencies

Exact versions (pinned for reproducibility):
```
openpyxl==3.1.2
python-docx==1.1.0
PyYAML==6.0.1
google-auth==2.41.1
google-auth-oauthlib==1.2.3
google-auth-httplib2==0.2.1
google-api-python-client==2.187.0
```

**Why pinned?** Prevents "works on my machine" issues. Same versions = same behavior.

## Git Configuration

- User: nico- (Nicolasgz96)
- Email: 96.nicolasgonzalez@gmail.com
- Repository: https://github.com/Nicolasgz96/Proyect-QA-testing.git
- Branch: main

## File Organization Reference

```
Hello_Britannica/
├── eod_inputs/              # YAML input files (gitignored)
├── test_cases/
│   ├── current/             # Working Excel file
│   └── backups/             # Original + backups (NEVER modify)
├── documentation/
│   ├── templates/           # DOCX + YAML templates
│   └── reports/             # Generated EOD reports
│       └── archive/         # Archived reports by month
├── scripts/
│   ├── common/              # Shared utilities (path_utils, excel_utils, docx_utils)
│   ├── analysis/            # Excel analysis scripts
│   ├── formatting/          # Formatting restoration
│   ├── verification/        # Test case verification
│   ├── reporting/           # EOD generation + Google Drive upload
│   └── tests/               # Unit tests
└── data/                    # JSON analysis outputs
```

## Recent Architecture Changes

The codebase recently underwent quality improvements:

1. **Code deduplication** - `get_project_root()` centralized in `path_utils.py`
2. **Dependency pinning** - All versions locked to prevent build issues
3. **Environment validation** - `check_environment.py` verifies setup
4. **Documentation** - python vs python3 standardized to python3

See `CHANGELOG.md` for complete history.

## Specialized Agents

The `.claude/agents/` directory contains specialized agents for QA workflows:

### eod-report-generator
Converts informal testing notes to professional EOD reports with full automation:
- **Input**: Casual testing notes (e.g., "Tested iOS login, found 2 bugs")
- **Process**: YAML creation → DOCX generation → Google Drive upload
- **Output**: Professional EOD report in `documentation/reports/` and Google Drive
- **Key Features**: Auto-detects tester name, supports multiple date formats, automatic cleanup

### jira-bug-writer
Generates Jira-formatted bug reports with natural, professional tone:
- **Input**: Bug description (platform, steps, expected/actual behavior)
- **Process**: Creates Python script → Generates DOCX → Uploads to Google Drive
- **Output**: Jira-ready bug report in `documentation/reports/` and `G:\My Drive\Bug Reports\`
- **Format**: Uses `[Step 1 – description]` format, includes all Jira fields
- **Tone**: Natural, conversational (not robotic), follows Britannica QA standard

### qa-test-planner
Creates comprehensive test plans and test case documentation:
- **Input**: Web application URLs, user journey documents, feature requirements
- **Process**: Analyzes application → Creates test strategy → Generates test cases
- **Output**: Complete test plans with traceability matrices

### brutal-project-auditor
Provides unfiltered, honest code quality analysis:
- **Input**: Request for critical assessment
- **Process**: Analyzes codebase for issues, anti-patterns, technical debt
- **Output**: Brutally honest report with actionable improvements

**Usage**: Invoke agents using `@agent-name` or through the Task tool. All agents have access to this CLAUDE.md and understand the project architecture.

## Bug Report Workflow

Bug reports follow a streamlined automation workflow:

### Process
1. Provide bug information to jira-bug-writer agent (platform, steps, expected/actual behavior)
2. Agent creates Python script at `scripts/reporting/create_bug_report.py`
3. Script generates professional DOCX with Britannica QA formatting
4. File saved to `documentation/reports/BUG_YYYY-MM-DD_Description.docx`
5. Automatically uploaded to `G:\My Drive\Bug Reports\` via PowerShell
6. Upload verified and confirmed

### Bug Report Format
- Title: Short, clear problem summary (60 chars max)
- Priority: Blocker/Critical/High/Medium/Low
- Environment: Platform, version, device, role, date
- Description: What, where, why (conversational tone)
- Steps to Reproduce: `[Step 1 – include URL/credentials]`, `[Step 2 – action]`, etc.
- Expected Behavior: Bullet points of correct behavior
- Actual Behavior: Natural explanation (as if telling a colleague)
- Impact: Educational integrity, user confusion, data tracking
- Suggested Fix: Technical recommendations
- Notes: Video evidence, reproducibility, regression risk
- Jira Field Selections: Project, Work Type, Priority, Components, Labels, etc.

### PowerShell Upload Commands
```bash
# Create folder if needed and upload bug report
powershell.exe -Command "
    if (-not (Test-Path 'G:\\My Drive\\Bug Reports')) {
        New-Item -Path 'G:\\My Drive\\Bug Reports' -ItemType Directory -Force | Out-Null
    }
    Copy-Item 'documentation/reports/BUG_YYYY-MM-DD_Description.docx' -Destination 'G:\\My Drive\\Bug Reports\\BUG_YYYY-MM-DD_Description.docx' -Force
    Write-Host 'Bug report uploaded successfully!'
"

# Verify upload
powershell.exe -Command "
    if (Test-Path 'G:\\My Drive\\Bug Reports\\BUG_YYYY-MM-DD_Description.docx') {
        Get-Item 'G:\\My Drive\\Bug Reports\\BUG_YYYY-MM-DD_Description.docx' | Select-Object Name, Length, LastWriteTime
    }
"
```

## Python Environment Notes

### WSL Environment
- **Python 3 not available in WSL PATH** - Use Windows Python launcher instead
- Command: `/mnt/c/Windows/py.exe` (points to Python 3.13.3)
- All scripts designed to work with Windows Python via WSL filesystem
- File paths automatically converted (WSL paths work with Windows Python)

### Script Execution Examples
```bash
# From WSL, using Windows Python
/mnt/c/Windows/py.exe scripts/reporting/create_bug_report.py
/mnt/c/Windows/py.exe scripts/reporting/generate_eod_report.py eod_inputs/my_eod.yaml

# PowerShell commands work directly in WSL
powershell.exe -Command "Copy-Item 'file.docx' -Destination 'G:\\My Drive\\folder\\file.docx'"
```
