#!/usr/bin/env python3
"""
Common Excel utilities for test case management
"""
import os
import sys
from pathlib import Path
from typing import Optional
from openpyxl import load_workbook
from openpyxl.workbook import Workbook

from .path_utils import get_project_root


def get_excel_path(filename: str = "Hello Master test cases.xlsx") -> Path:
    """
    Get the full path to the Excel file in test_cases/current/.

    Args:
        filename: Name of the Excel file (default: "Hello Master test cases.xlsx")

    Returns:
        Path: Full path to the Excel file
    """
    project_root = get_project_root()
    return project_root / "test_cases" / "current" / filename


def get_backup_path(filename: str) -> Path:
    """
    Get the full path to a backup Excel file.

    Args:
        filename: Name of the backup file

    Returns:
        Path: Full path to the backup file
    """
    project_root = get_project_root()
    return project_root / "test_cases" / "backups" / filename


def get_data_path(filename: str) -> Path:
    """
    Get the full path to a data file.

    Args:
        filename: Name of the data file

    Returns:
        Path: Full path to the data file
    """
    project_root = get_project_root()
    return project_root / "data" / filename


def get_docs_path(filename: str) -> Path:
    """
    Get the full path to a documentation file.

    Args:
        filename: Name of the documentation file

    Returns:
        Path: Full path to the documentation file
    """
    project_root = get_project_root()
    return project_root / "documentation" / "reports" / filename


def load_excel_safely(file_path: Path, data_only: bool = False) -> Optional[Workbook]:
    """
    Safely load an Excel workbook with proper error handling.

    Args:
        file_path: Path to the Excel file
        data_only: Whether to load only data values (no formulas)

    Returns:
        Workbook object if successful, None if error occurs

    Raises:
        FileNotFoundError: If the file doesn't exist
        Exception: For other errors during loading
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Excel file not found: {file_path}")

    try:
        wb = load_workbook(file_path, data_only=data_only)
        return wb
    except Exception as e:
        print(f"Error loading workbook '{file_path}': {e}", file=sys.stderr)
        raise


def save_excel_safely(workbook: Workbook, file_path: Path) -> bool:
    """
    Safely save an Excel workbook with proper error handling.

    Args:
        workbook: Workbook object to save
        file_path: Path where to save the file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        workbook.save(file_path)
        print(f"Successfully saved: {file_path}")
        return True
    except PermissionError:
        print(f"Error: Permission denied when saving to {file_path}", file=sys.stderr)
        print("Make sure the file is not open in another application.", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error saving workbook to '{file_path}': {e}", file=sys.stderr)
        return False


def print_separator(char: str = "=", length: int = 80):
    """Print a separator line."""
    print(char * length)


def print_section_header(title: str, char: str = "=", length: int = 80):
    """Print a formatted section header."""
    print_separator(char, length)
    print(title)
    print_separator(char, length)
