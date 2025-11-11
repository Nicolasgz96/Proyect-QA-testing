#!/usr/bin/env python3
"""Check that the development environment is properly configured."""
import sys
import importlib.util


def check_python_version():
    """Check Python version is 3.7+."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - UNSUPPORTED")
        print(f"  ERROR: Python 3.7+ required")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_module(module_name: str, display_name: str = None):
    """Check if a Python module is installed."""
    if display_name is None:
        display_name = module_name

    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print(f"✗ {display_name} - NOT INSTALLED")
        return False
    print(f"✓ {display_name}")
    return True


def main():
    """Run all environment checks."""
    print("=" * 60)
    print("Hello Britannica QA - Environment Check")
    print("=" * 60)
    print()

    all_ok = True

    # Check Python version
    print("Python Version:")
    if not check_python_version():
        all_ok = False
    print()

    # Check required modules
    print("Required Python packages:")
    required = [
        ('openpyxl', 'openpyxl (Excel handling)'),
        ('docx', 'python-docx (Word documents)'),
        ('yaml', 'PyYAML (YAML parsing)'),
    ]
    for module, display in required:
        if not check_module(module, display):
            all_ok = False
    print()

    # Check optional modules
    print("Optional packages (for Google Drive):")
    optional = [
        ('google.auth', 'google-auth'),
        ('google_auth_oauthlib', 'google-auth-oauthlib'),
        ('google_auth_httplib2', 'google-auth-httplib2'),
        ('googleapiclient', 'google-api-python-client'),
    ]
    optional_ok = True
    for module, display in optional:
        if not check_module(module, display):
            optional_ok = False

    if not optional_ok:
        print("  Note: Google Drive features will not work without these packages")
    print()

    print("=" * 60)
    if all_ok:
        print("✓ Environment is properly configured!")
        print()
        print("You can now:")
        print("  - Generate EOD reports: python3 scripts/reporting/generate_eod_report.py")
        print("  - Analyze test cases: python3 scripts/analysis/analyze_excel.py")
        print("  - Run tests: python3 scripts/tests/test_eod_generator.py")
        if optional_ok:
            print("  - Upload to Google Drive: ./scripts/reporting/upload_eod_simple.sh")
        return 0
    else:
        print("✗ Environment check FAILED")
        print()
        print("Install missing packages:")
        print("  pip3 install -r requirements.txt")
        print()
        print("Or install Python 3.7+ if needed:")
        print("  sudo apt update && sudo apt install python3 python3-pip")
        return 1


if __name__ == '__main__':
    sys.exit(main())
