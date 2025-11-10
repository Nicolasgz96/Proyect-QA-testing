#!/usr/bin/env python3
"""
Unit tests for EOD report generator.

Run tests:
    python -m pytest scripts/tests/test_eod_generator.py -v

Or run without pytest:
    python scripts/tests/test_eod_generator.py
"""

import sys
from pathlib import Path
import unittest
from datetime import datetime

# Add parent directories to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "reporting"))

from reporting.generate_eod_report import (
    parse_date_flexible,
    format_product_section,
    format_areas_section,
    format_bugs_section,
    format_bug_fixes_section,
    format_requirements_section,
    format_next_steps_section,
    get_user_fullname
)


class TestDateParsing(unittest.TestCase):
    """Test flexible date parsing."""

    def test_parse_dd_mm_yyyy(self):
        """Test DD-MM-YYYY format."""
        date = parse_date_flexible("06-11-2025")
        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 6)

    def test_parse_yyyy_mm_dd(self):
        """Test YYYY-MM-DD format."""
        date = parse_date_flexible("2025-11-06")
        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 6)

    def test_parse_mm_dd_yyyy(self):
        """Test MM/DD/YYYY format."""
        date = parse_date_flexible("11/06/2025")
        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 6)

    def test_parse_month_dd_yyyy(self):
        """Test 'Month DD, YYYY' format."""
        date = parse_date_flexible("November 6, 2025")
        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 6)

    def test_parse_dd_month_yyyy(self):
        """Test 'DD Month YYYY' format."""
        date = parse_date_flexible("6 November 2025")
        self.assertEqual(date.year, 2025)
        self.assertEqual(date.month, 11)
        self.assertEqual(date.day, 6)

    def test_parse_invalid_date(self):
        """Test invalid date raises ValueError."""
        with self.assertRaises(ValueError):
            parse_date_flexible("invalid-date")


class TestFormatProduct(unittest.TestCase):
    """Test product section formatting."""

    def test_format_basic_product(self):
        """Test basic product formatting."""
        data = {
            'product': {
                'name': 'Test App',
                'platforms': ['Web', 'iOS'],
                'roles_tested': ['Student', 'Teacher']
            }
        }
        result = format_product_section(data)
        self.assertIn('Product: Test App', result)
        self.assertIn('Environments:', result)
        self.assertIn('Web', result)
        self.assertIn('iOS', result)
        self.assertIn('Roles Tested: Student, Teacher', result)

    def test_format_minimal_product(self):
        """Test product with minimal data."""
        data = {'product': {}}
        result = format_product_section(data)
        self.assertIn('Product: Hello Britannica', result)


class TestFormatAreas(unittest.TestCase):
    """Test areas covered section formatting."""

    def test_format_areas_with_data(self):
        """Test areas with data."""
        data = {
            'areas_covered': [
                'Regression testing',
                'Login verification'
            ]
        }
        result = format_areas_section(data)
        self.assertEqual(len(result), 2)
        self.assertIn('Regression testing', result)
        self.assertIn('Login verification', result)

    def test_format_areas_empty(self):
        """Test areas with no data (uses fallback)."""
        data = {}
        result = format_areas_section(data)
        self.assertEqual(len(result), 1)
        self.assertIn('Regression and exploratory testing', result[0])


class TestFormatBugs(unittest.TestCase):
    """Test bugs section formatting."""

    def test_format_bugs_empty(self):
        """Test with no bugs."""
        data = {'bugs': []}
        result = format_bugs_section(data)
        self.assertEqual(len(result), 1)
        self.assertIn('No new bugs', result[0])

    def test_format_bugs_simple_strings(self):
        """Test with simple string bugs."""
        data = {
            'bugs': [
                'Login issue',
                'Dashboard crash'
            ]
        }
        result = format_bugs_section(data)
        self.assertEqual(len(result), 2)
        self.assertIn('Login issue', result)

    def test_format_bugs_structured(self):
        """Test with structured bug data."""
        data = {
            'bugs': [
                {
                    'title': 'Login redirect issue',
                    'severity': 'High',
                    'description': 'Wrong redirect after login'
                }
            ]
        }
        result = format_bugs_section(data)
        self.assertTrue(any('[High]' in line for line in result))
        self.assertTrue(any('Login redirect issue' in line for line in result))


class TestFormatBugFixes(unittest.TestCase):
    """Test bug fixes section formatting."""

    def test_format_fixes_empty(self):
        """Test with no fixes."""
        data = {'bug_fixes': []}
        result = format_bug_fixes_section(data)
        self.assertEqual(len(result), 1)
        self.assertIn('No previously reported bugs', result[0])

    def test_format_fixes_structured(self):
        """Test with structured fix data."""
        data = {
            'bug_fixes': [
                {
                    'bug_id': 'HB-1234',
                    'title': 'Fixed login delay',
                    'status': 'Verified'
                }
            ]
        }
        result = format_bug_fixes_section(data)
        self.assertTrue(any('HB-1234' in line for line in result))
        self.assertTrue(any('Fixed login delay' in line for line in result))


class TestFormatRequirements(unittest.TestCase):
    """Test requirements section formatting."""

    def test_format_reqs_empty(self):
        """Test with no requirements."""
        data = {'requirements': []}
        result = format_requirements_section(data)
        self.assertEqual(len(result), 1)
        self.assertIn('No new requirements', result[0])

    def test_format_reqs_structured(self):
        """Test with structured requirement data."""
        data = {
            'requirements': [
                {
                    'story_id': 'HB-5678',
                    'title': 'User can export PDF',
                    'status': 'Confirmed'
                }
            ]
        }
        result = format_requirements_section(data)
        self.assertTrue(any('HB-5678' in line for line in result))
        self.assertTrue(any('User can export PDF' in line for line in result))


class TestFormatNextSteps(unittest.TestCase):
    """Test next steps section formatting."""

    def test_format_next_steps_with_data(self):
        """Test next steps with data."""
        data = {
            'next_steps': [
                'Continue regression testing',
                'Start exploratory testing'
            ]
        }
        result = format_next_steps_section(data)
        self.assertEqual(len(result), 2)
        self.assertIn('Continue regression testing', result)

    def test_format_next_steps_empty(self):
        """Test next steps empty (uses fallback)."""
        data = {}
        result = format_next_steps_section(data)
        self.assertEqual(len(result), 1)
        self.assertIn('Continue with regression', result[0])


class TestUserName(unittest.TestCase):
    """Test user name detection."""

    def test_get_user_fullname(self):
        """Test getting user name (either from git or system)."""
        name = get_user_fullname()
        self.assertIsInstance(name, str)
        self.assertGreater(len(name), 0)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDateParsing))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatProduct))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatAreas))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatBugs))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatBugFixes))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatRequirements))
    suite.addTests(loader.loadTestsFromTestCase(TestFormatNextSteps))
    suite.addTests(loader.loadTestsFromTestCase(TestUserName))

    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Return exit code
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(run_tests())
