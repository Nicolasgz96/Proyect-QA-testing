#!/usr/bin/env python3
"""
Common DOCX utilities for EOD report generation
"""
import sys
from pathlib import Path
from typing import Optional
from docx import Document


def get_project_root() -> Path:
    """
    Get the project root directory dynamically.

    Returns:
        Path: Project root directory
    """
    script_dir = Path(__file__).resolve().parent
    # Go up from scripts/common/ to project root
    project_root = script_dir.parent.parent
    return project_root


def get_template_path(filename: str = "Reports end of the day highlights.docx") -> Path:
    """
    Get the full path to a template file in documentation/templates/.

    Args:
        filename: Name of the template file

    Returns:
        Path: Full path to the template file
    """
    project_root = get_project_root()
    return project_root / "documentation" / "templates" / filename


def get_report_output_path(filename: str) -> Path:
    """
    Get the full path to a report file in documentation/reports/.

    Args:
        filename: Name of the report file

    Returns:
        Path: Full path to the report file
    """
    project_root = get_project_root()
    return project_root / "documentation" / "reports" / filename


def get_report_archive_path(filename: str, year_month: str) -> Path:
    """
    Get the full path to an archived report file.

    Args:
        filename: Name of the report file
        year_month: Year-month string (e.g., "2025-11")

    Returns:
        Path: Full path to the archived report file
    """
    project_root = get_project_root()
    return project_root / "documentation" / "reports" / "archive" / year_month / filename


def load_docx_safely(file_path: Path) -> Optional[Document]:
    """
    Safely load a DOCX file with error handling.

    Args:
        file_path: Path to the DOCX file

    Returns:
        Document object if successful, None otherwise
    """
    try:
        if not file_path.exists():
            print(f"Error: File not found at {file_path}", file=sys.stderr)
            return None

        doc = Document(str(file_path))
        return doc

    except PermissionError:
        print(f"Error: Permission denied. Is the file open in Word? {file_path}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error loading document: {e}", file=sys.stderr)
        return None


def save_docx_safely(doc: Document, file_path: Path) -> bool:
    """
    Safely save a DOCX file with error handling.

    Args:
        doc: Document object to save
        file_path: Path where to save the file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Save the document
        doc.save(str(file_path))
        return True

    except PermissionError:
        print(f"Error: Permission denied. Is the file open in Word? {file_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error saving document: {e}", file=sys.stderr)
        return False


def print_section_header(title: str) -> None:
    """
    Print a formatted section header.

    Args:
        title: Header title to print
    """
    separator = "=" * 60
    print(f"\n{separator}")
    print(f"{title}")
    print(f"{separator}\n")
