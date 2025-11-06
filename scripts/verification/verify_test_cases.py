#!/usr/bin/env python3
"""
Script to verify the test cases were added correctly
"""
import sys
from pathlib import Path

# Add parent directory to path to import common utilities
sys.path.insert(0, str(Path(__file__).parent.parent))

from common.excel_utils import (
    load_excel_safely,
    get_excel_path,
    print_section_header,
    print_separator
)


def verify_test_cases(excel_path: Path):
    """
    Verify test cases in the Excel file.

    Args:
        excel_path: Path to the Excel file

    Returns:
        bool: True if verification passed, False otherwise
    """
    print_section_header("VERIFICATION REPORT", "=", 60)

    try:
        wb = load_excel_safely(excel_path)
    except Exception as e:
        print(f"Error: Failed to load Excel file: {e}", file=sys.stderr)
        return False

    # Check specific sheets
    sheets_to_check = {
        'Admin Onboard': ['AO013', 'AO014', 'AO015', 'AO027', 'AO028', 'AO039'],
        'Teacher - Email': ['TE051', 'TE052', 'TE058', 'TE059', 'TE070'],
        'Security Testing': ['SEC001', 'SEC002', 'SEC015'],
        'Negative Scenarios': ['NEG001', 'NEG002', 'NEG010']
    }

    for sheet_name, test_ids in sheets_to_check.items():
        print(f"\n{'='*60}")
        print(f"Sheet: {sheet_name}")
        print(f"{'='*60}")

        if sheet_name not in wb.sheetnames:
            print(f"ERROR: Sheet '{sheet_name}' not found!")
            continue

        ws = wb[sheet_name]
        print(f"Total rows: {ws.max_row}")

        # Count test cases
        found_ids = []
        for row in range(2, ws.max_row + 1):
            test_id = ws.cell(row, 1).value
            if test_id:
                found_ids.append(str(test_id))

        print(f"Total test cases: {len(found_ids)}")

        if found_ids:
            print(f"First test case: {found_ids[0]}")
            print(f"Last test case: {found_ids[-1]}")

        # Check for specific test IDs
        print(f"\nChecking for new test cases:")
        for test_id in test_ids:
            if test_id in found_ids:
                # Get the row for this test ID
                for row in range(2, ws.max_row + 1):
                    if str(ws.cell(row, 1).value) == test_id:
                        title = ws.cell(row, 3).value
                        print(f"  [OK] {test_id}: {title}")
                        break
            else:
                print(f"  [MISSING] {test_id}: NOT FOUND")

    # Summary of all sheets
    print(f"\n{'='*60}")
    print("SUMMARY OF ALL SHEETS")
    print(f"{'='*60}")

    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        # Count rows with data
        test_count = 0
        for row in range(2, ws.max_row + 1):
            if ws.cell(row, 1).value:
                test_count += 1

        if test_count > 0:
            print(f"{sheet_name}: {test_count} test cases")

    wb.close()

    print_separator("=", 60)
    print("Verification complete!")
    print_separator("=", 60)

    return True


def main():
    """Main entry point."""
    file_path = get_excel_path()

    if not file_path.exists():
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        sys.exit(1)

    success = verify_test_cases(file_path)

    if not success:
        print("Verification failed.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
