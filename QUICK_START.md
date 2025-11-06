# Quick Start Guide - Hello Britannica Project

## What Changed?

Your project has been reorganized from a flat structure into a clean, organized folder hierarchy. Everything is still here, just better organized!

## Where Are My Files?

### I need to work on test cases
**Location:** `/home/onik/proyects/AI/Hello_Britannica/test_cases/current/Hello Master test cases.xlsx`

### I need to view reports
**Location:** `/home/onik/proyects/AI/Hello_Britannica/documentation/reports/`
All your markdown reports are here.

### I need to run a Python script
**Location:** `/home/onik/proyects/AI/Hello_Britannica/scripts/[category]/`
- Analysis scripts: `scripts/analysis/`
- Formatting scripts: `scripts/formatting/`
- Verification scripts: `scripts/verification/`

### I need backup files
**Location:** `/home/onik/proyects/AI/Hello_Britannica/test_cases/backups/`
Both backup versions are safely stored here.

## Quick Commands

### Navigate to Project
```bash
cd /home/onik/proyects/AI/Hello_Britannica/
```

### View Structure
```bash
ls -la
ls test_cases/current/
ls documentation/reports/
ls scripts/
```

### Run a Script (from project root)
```bash
python scripts/analysis/analyze_excel.py
python scripts/verification/verify_test_cases.py
python scripts/formatting/verify_formatting.py
```

## Common Tasks

### Task 1: Open Test Cases
```bash
# Path to file:
/home/onik/proyects/AI/Hello_Britannica/test_cases/current/Hello Master test cases.xlsx
```

### Task 2: Run Analysis
```bash
cd /home/onik/proyects/AI/Hello_Britannica/
python scripts/analysis/analyze_excel.py
```

### Task 3: Check Reports
```bash
cd /home/onik/proyects/AI/Hello_Britannica/documentation/reports/
ls -la
```

### Task 4: Verify Test Cases
```bash
cd /home/onik/proyects/AI/Hello_Britannica/
python scripts/verification/verify_test_cases.py
```

## Folder Quick Reference

```
Hello_Britannica/
├── test_cases/          → Excel test case files
│   ├── current/         → Working file (use this!)
│   └── backups/         → Safe copies
├── documentation/       → All docs and reports
│   ├── user_journeys/   → User journey docs
│   ├── templates/       → Templates (Jira bug)
│   └── reports/         → Analysis reports
├── scripts/             → Python automation
│   ├── analysis/        → Analysis tools
│   ├── formatting/      → Formatting tools
│   └── verification/    → Verification tools
└── data/                → JSON output files
```

## What's Different?

### Before (Flat Structure)
```
Hello_Britannica/
├── Hello Master test cases.xlsx
├── analyze_excel.py
├── QA_Report.md
├── (everything mixed together)
```

### After (Organized Structure)
```
Hello_Britannica/
├── test_cases/current/Hello Master test cases.xlsx
├── scripts/analysis/analyze_excel.py
├── documentation/reports/QA_Report.md
└── (logically organized!)
```

## Key Benefits

1. **Easy to Find** - Files grouped by type and purpose
2. **Safe Backups** - Separate folder for backup files
3. **Clear Organization** - Scripts categorized by function
4. **Better Workflow** - Follow the folder structure naturally

## Need Help?

1. **README.md** - Comprehensive documentation with all details
2. **ORGANIZATION_SUMMARY.md** - Complete migration details and file map
3. **QUICK_REFERENCE.txt** - Original quick reference (in documentation/)

## Important Notes

- **All files preserved** - Nothing was deleted
- **Scripts updated** - All Python scripts now use relative paths
- **Same functionality** - Everything works the same, just organized better
- **Working from root** - Always run scripts from the project root directory

## Getting Started Checklist

- [ ] Navigate to project directory
- [ ] Open test_cases/current/Hello Master test cases.xlsx
- [ ] Check documentation/reports/ for your reports
- [ ] Try running a verification script
- [ ] Review README.md for complete documentation

## Script Categories Explained

### Analysis Scripts
Use when you want to:
- Analyze Excel file structure
- Compare different versions
- Add new test cases
- Generate JSON reports

### Formatting Scripts
Use when you want to:
- Restore original formatting
- Verify formatting is correct
- Get formatting details

### Verification Scripts
Use when you want to:
- Verify test cases were added correctly
- Get detailed statistics
- Check data integrity

## Pro Tips

1. **Always work from project root** - Scripts expect to be run from there
2. **Use current/ for work** - Keep backups/ untouched
3. **Save reports to documentation/reports/** - Keep them organized
4. **Check README.md** - It has all the details
5. **Scripts are now portable** - They work with relative paths

---

**Ready to go!** Your project is now clean, organized, and ready for efficient QA work.
