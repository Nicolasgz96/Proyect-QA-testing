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
│   └── excel_utils.py  # Common Excel operations and path management
├── analysis/           # Analysis and modification scripts
│   ├── analyze_excel.py
│   ├── analyze_excel_files.py
│   └── add_test_cases.py
├── formatting/         # Formatting scripts
│   ├── formatting_summary.py
│   ├── restore_formatting.py
│   └── verify_formatting.py
└── verification/       # Verification scripts
    ├── verify_test_cases.py
    └── detailed_verification.py
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

## Common Utilities

All scripts now use shared utilities from `common/excel_utils.py`:

- **Path Management**: Centralized path resolution (no more hardcoded paths)
- **Error Handling**: Proper exception handling and user feedback
- **Safe Operations**: Safe loading and saving of Excel files
- **Type Hints**: Better code documentation and IDE support

### Key Functions

- `get_project_root()` - Get project root directory
- `get_excel_path()` - Get path to main Excel file
- `load_excel_safely()` - Load Excel with error handling
- `save_excel_safely()` - Save Excel with error handling
- `print_section_header()` - Formatted output headers

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
