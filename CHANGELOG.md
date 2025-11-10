# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Environment check script (`scripts/check_environment.py`) to validate Python and dependencies
- Centralized path resolution in `scripts/common/path_utils.py`
- Comprehensive CHANGELOG.md for tracking all project changes
- Test file for Google Drive integration verification
- Complete documentation for Google Drive setup (both OAuth and File Stream methods)

### Changed
- **BREAKING**: Unified `get_project_root()` function into `path_utils.py` module
  - Both `excel_utils.py` and `docx_utils.py` now import from `path_utils`
  - Eliminates code duplication
- Pinned all Google Drive API dependencies to specific tested versions
  - `google-auth==2.41.1` (was `>=2.0.0`)
  - `google-auth-oauthlib==1.2.3` (was `>=1.0.0`)
  - `google-auth-httplib2==0.2.1` (was `>=0.1.0`)
  - `google-api-python-client==2.187.0` (was `>=2.0.0`)
- Updated eod-report-generator agent with complete YAML workflow documentation
- Organized YAML input files into `eod_inputs/` directory
- Enhanced `.gitignore` to protect sensitive files and generated reports

### Fixed
- Removed obsolete `scripts/generate_eod_report.py.OLD` file (336 lines of dead code)
- Cleaned up Zone.Identifier files from repository
- Fixed requirements.txt to include all necessary dependencies

### Documentation
- Created `GOOGLE_DRIVE_SIMPLE.md` for File Stream upload method
- Updated `GOOGLE_DRIVE_SETUP.md` for OAuth method
- Updated `README.md` with current features and workflows
- Updated `CLAUDE.md` with latest project architecture

## [1.0.0] - 2025-11-06

### Added
- Initial release of Hello Britannica QA Test Management System
- Excel-based test case management with Python automation
- Test case analysis scripts (`analyze_excel.py`, `analyze_excel_files.py`)
- Test case addition from markdown (`add_test_cases.py`)
- Excel formatting restoration tools
- Test case verification scripts
- **EOD Report Generation System**
  - YAML-based structured input (`eod_input_template.yaml`)
  - Professional DOCX report generation
  - Automatic date parsing (multiple formats supported)
  - Template validation
  - Dry-run mode for preview
  - Report archival system (by month)
- **Google Drive Integration**
  - OAuth2 method with `upload_to_gdrive.py`
  - Simple File Stream method with `upload_eod_simple.sh`
  - Automatic upload to `G:\My Drive\Daily reports\`
  - Automatic cleanup of old files (7+ days)
- **Centralized Utilities**
  - `excel_utils.py` - Excel file handling and path resolution
  - `docx_utils.py` - DOCX file handling and path resolution
- **Testing Infrastructure**
  - Unit tests for EOD report generator (20 test cases)
  - Test coverage for YAML parsing, date formatting, and section generation
- **Documentation**
  - Comprehensive README with usage examples
  - CLAUDE.md for development guidelines
  - Setup guides for Git, GitHub Desktop, and Google Drive
  - YAML template with examples

### Project Structure
```
Hello_Britannica/
├── test_cases/          # Excel test case files
│   ├── current/         # Working version
│   └── backups/         # Backup versions
├── documentation/
│   ├── templates/       # DOCX and YAML templates
│   └── reports/         # Generated EOD reports
├── scripts/
│   ├── common/          # Shared utilities
│   ├── analysis/        # Analysis scripts
│   ├── formatting/      # Formatting scripts
│   ├── verification/    # Verification scripts
│   ├── reporting/       # EOD reporting scripts
│   └── tests/           # Unit tests
├── eod_inputs/          # YAML input files for EOD reports
└── data/                # JSON analysis outputs
```

### Dependencies
- Python 3.7+
- openpyxl 3.1.2 (Excel handling)
- python-docx 1.1.0 (Word documents)
- PyYAML 6.0.1 (YAML parsing)
- Google API Client libraries (optional, for Google Drive)

### Features
- **Organized Structure**: Clear separation of test cases, documentation, and scripts
- **Backup Management**: Separate folders for current and backup files
- **Automated Scripts**: Python automation for analysis, formatting, and verification
- **YAML-Based EOD Reports**: Structured input with validation and error handling
- **Google Drive Integration**: Two methods (OAuth and File Stream) for maximum flexibility
- **Centralized Utilities**: Dynamic path resolution for cross-platform compatibility
- **Comprehensive Testing**: Unit tests for critical functionality
- **Professional Documentation**: Detailed guides for setup and usage

---

## Release Notes

### How to Update

From previous versions, update to latest:

```bash
# Pull latest changes
git pull origin main

# Install/update dependencies
pip3 install -r requirements.txt

# Check environment
python3 scripts/check_environment.py
```

### Breaking Changes in Unreleased

- `get_project_root()` is no longer defined in `excel_utils.py` or `docx_utils.py`
  - Import from `scripts.common.path_utils` instead
  - Example: `from scripts.common.path_utils import get_project_root`

### Migration Guide

If you have custom scripts using the old `excel_utils.py` or `docx_utils.py`:

**Before:**
```python
from common.excel_utils import get_project_root, get_excel_path
```

**After:**
```python
from common.path_utils import get_project_root
from common.excel_utils import get_excel_path
```

---

## Support

For issues, questions, or contributions:
- Check documentation in `documentation/` folder
- Review `CLAUDE.md` for development guidelines
- Run environment check: `python3 scripts/check_environment.py`

## License

This project is for internal QA use at Encyclopaedia Britannica.
