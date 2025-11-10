#!/usr/bin/env python3
"""
Path resolution utilities for Hello Britannica project.

This module provides centralized path resolution to avoid code duplication.
All path-related utilities should use these functions.
"""
from pathlib import Path


def get_project_root() -> Path:
    """
    Get the project root directory dynamically.

    This function resolves the project root by going up from the
    scripts/common/ directory to the project root.

    Returns:
        Path: Project root directory (parent of scripts/)

    Example:
        >>> root = get_project_root()
        >>> print(root / "README.md")
        /path/to/Hello_Britannica/README.md
    """
    # Get directory containing this file (scripts/common/)
    script_dir = Path(__file__).resolve().parent

    # Go up two levels: scripts/common/ -> scripts/ -> project_root/
    project_root = script_dir.parent.parent

    return project_root
