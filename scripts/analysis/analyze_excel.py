#!/usr/bin/env python3
"""
Script to analyze the existing Excel file structure
"""
import sys
from pathlib import Path

# Add parent directory to path to import common utilities
sys.path.insert(0, str(Path(__file__).parent.parent))

from common.excel_utils import (
    load_excel_safely,
    get_excel_path,
    get_data_path,
    print_section_header
)
import json


def analyze_excel_file(file_path: Path):
    """
    Analyze the structure of the Excel file.

    Args:
        file_path: Path to the Excel file

    Returns:
        dict: Analysis results
    """
    try:
        # Load the workbook
        wb = load_excel_safely(file_path)

        # Get sheet names
        print(f"Total sheets: {len(wb.sheetnames)}")
        print(f"Sheet names: {wb.sheetnames}\n")

        analysis = {}

        # Analyze each sheet
        for sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            print(f"\n{'='*60}")
            print(f"Sheet: {sheet_name}")
            print(f"{'='*60}")

            # Get dimensions
            max_row = ws.max_row
            max_col = ws.max_column
            print(f"Dimensions: {max_row} rows x {max_col} columns")

            # Get header row (assuming row 1 is header)
            headers = []
            for col in range(1, max_col + 1):
                cell_value = ws.cell(1, col).value
                headers.append(cell_value)

            print(f"\nHeaders: {headers}")

            # Get sample data (first 3 rows after header)
            print(f"\nSample data (first 3 rows):")
            for row in range(2, min(5, max_row + 1)):
                row_data = []
                for col in range(1, max_col + 1):
                    cell_value = ws.cell(row, col).value
                    row_data.append(cell_value)
                print(f"Row {row}: {row_data}")

            # Find last test case ID
            test_case_ids = []
            for row in range(2, max_row + 1):
                test_id = ws.cell(row, 1).value  # Assuming first column is Test ID
                if test_id:
                    test_case_ids.append(str(test_id))

            if test_case_ids:
                print(f"\nFirst Test Case ID: {test_case_ids[0]}")
                print(f"Last Test Case ID: {test_case_ids[-1]}")
                print(f"Total test cases in sheet: {len(test_case_ids)}")

            analysis[sheet_name] = {
                'max_row': max_row,
                'max_col': max_col,
                'headers': headers,
                'test_case_count': len(test_case_ids),
                'first_id': test_case_ids[0] if test_case_ids else None,
                'last_id': test_case_ids[-1] if test_case_ids else None
            }

        wb.close()

        # Save analysis to JSON
        output_path = get_data_path('excel_analysis.json')

        try:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w') as f:
                json.dump(analysis, f, indent=2)

            print(f"\n{'='*60}")
            print(f"Analysis complete! Saved to {output_path}")
            print(f"{'='*60}")
        except Exception as save_error:
            print(f"Error saving analysis to {output_path}: {save_error}", file=sys.stderr)
            return None

        return analysis

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error analyzing Excel file: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return None


def main():
    """Main entry point."""
    print_section_header("Excel File Analysis")

    file_path = get_excel_path()
    print(f"Analyzing: {file_path}\n")

    if not file_path.exists():
        print(f"Error: File not found at {file_path}", file=sys.stderr)
        sys.exit(1)

    result = analyze_excel_file(file_path)

    if result is None:
        print("Analysis failed.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
