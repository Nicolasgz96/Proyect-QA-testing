#!/usr/bin/env python3
"""
Script to create detailed verification of added test cases
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


def detailed_verification(excel_path: Path):
    """
    Create detailed verification report.

    Args:
        excel_path: Path to the Excel file

    Returns:
        bool: True if all tests verified successfully
    """
    print_section_header("DETAILED VERIFICATION OF ADDED TEST CASES")

    try:
        wb = load_excel_safely(excel_path)
    except Exception as e:
        print(f"Error: Failed to load Excel file: {e}", file=sys.stderr)
        return False

    # Define the new test case ranges
    new_test_cases = {
        'Admin Onboard': {
            'range': ['AO013', 'AO014', 'AO015', 'AO016', 'AO017', 'AO018', 'AO019', 'AO020',
                     'AO021', 'AO022', 'AO023', 'AO024', 'AO025', 'AO026', 'AO027',
                     'AO028', 'AO029', 'AO030', 'AO031', 'AO032', 'AO033', 'AO034',
                     'AO035', 'AO036', 'AO037', 'AO038', 'AO039']
        },
        'Teacher - Email': {
            'range': ['TE051', 'TE052', 'TE053', 'TE054', 'TE055', 'TE056', 'TE057', 'TE058',
                     'TE059', 'TE060', 'TE061', 'TE062', 'TE063', 'TE064', 'TE065', 'TE066',
                     'TE067', 'TE068', 'TE069', 'TE070']
        },
        'Security Testing': {
            'range': ['SEC001', 'SEC002', 'SEC003', 'SEC004', 'SEC005', 'SEC006', 'SEC007',
                     'SEC008', 'SEC009', 'SEC010', 'SEC011', 'SEC012', 'SEC013', 'SEC014', 'SEC015']
        },
        'Negative Scenarios': {
            'range': ['NEG001', 'NEG002', 'NEG003', 'NEG004', 'NEG005', 'NEG006', 'NEG007',
                     'NEG008', 'NEG009', 'NEG010']
        }
    }

    total_verified = 0
    total_missing = 0

    for sheet_name, data in new_test_cases.items():
        print(f"\n{'='*80}")
        print(f"SHEET: {sheet_name}")
        print(f"{'='*80}")

        if sheet_name not in wb.sheetnames:
            print(f"ERROR: Sheet not found!")
            continue

        ws = wb[sheet_name]

        # Get all test IDs from the sheet
        all_test_ids = []
        test_id_to_title = {}
        for row in range(2, ws.max_row + 1):
            test_id = ws.cell(row, 1).value
            if test_id:
                all_test_ids.append(str(test_id))
                title = ws.cell(row, 3).value
                test_id_to_title[str(test_id)] = title

        expected = data['range']
        found = 0
        missing = 0

        print(f"\nExpected to add: {len(expected)} test cases")
        print(f"\nVerification Results:")
        print("-" * 80)

        for test_id in expected:
            if test_id in all_test_ids:
                title = test_id_to_title.get(test_id, 'N/A')
                print(f"[OK] {test_id}: {title[:60]}...")
                found += 1
                total_verified += 1
            else:
                print(f"[MISSING] {test_id}: NOT FOUND IN SHEET")
                missing += 1
                total_missing += 1

        print("-" * 80)
        print(f"Summary: {found} found, {missing} missing")

    # Final summary
    print_section_header("OVERALL SUMMARY")
    print(f"Total test cases verified: {total_verified}/72")
    print(f"Total missing: {total_missing}")

    if total_missing == 0:
        print("\n[SUCCESS] All 72 test cases have been successfully added!")
    else:
        print(f"\n[WARNING] {total_missing} test cases are missing!")

    print_separator()

    # Additional statistics
    print("\nADDITIONAL STATISTICS")
    print_separator()

    for sheet_name in ['Admin Onboard', 'Teacher - Email', 'Security Testing', 'Negative Scenarios']:
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            test_count = sum(1 for row in range(2, ws.max_row + 1) if ws.cell(row, 1).value)
            print(f"{sheet_name}: {test_count} total test cases")

    wb.close()

    return total_missing == 0


def main():
    """Main entry point."""
    file_path = get_excel_path()

    if not file_path.exists():
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        sys.exit(1)

    success = detailed_verification(file_path)

    if not success:
        print("Verification failed - some test cases are missing.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
