# Google Drive Upload - Simple Method (File Stream)

This guide is for users who have **Google Drive for Desktop** (File Stream) installed.

## Quick Start

If you have Google Drive File Stream installed (G: drive), you can simply copy files directly to your Google Drive folder - no OAuth setup needed!

## Upload EOD Report

### Method 1: Automatic Script (Recommended)

```bash
# Upload the latest EOD file and clean up old files (7+ days old)
./scripts/reporting/upload_eod_simple.sh

# Upload without cleanup
./scripts/reporting/upload_eod_simple.sh nico 0
```

The script automatically:
- Finds the most recent EOD file in `documentation/reports/`
- Copies it to `G:\My Drive\Daily reports\`
- Deletes EOD files older than 7 days (configurable)

### Method 2: Manual Copy

```bash
# Copy to Google Drive manually
cp documentation/reports/EOD_2025-11-07_nico.docx "/mnt/g/My Drive/Daily reports/"
```

Or use PowerShell:
```bash
powershell.exe -Command "Copy-Item 'documentation/reports/EOD_2025-11-07_nico.docx' -Destination 'G:\My Drive\Daily reports\' -Force"
```

## Complete Workflow

### 1. Generate EOD Report

```bash
# Create your EOD input file
cp documentation/templates/eod_input_template.yaml eod_inputs/today.yaml

# Edit eod_inputs/today.yaml with your testing notes

# Generate the report
python scripts/reporting/generate_eod_report.py eod_inputs/today.yaml
```

### 2. Upload to Google Drive

```bash
# One command to upload and cleanup
./scripts/reporting/upload_eod_simple.sh
```

**Done!** Your EOD report is now in Google Drive at:
`G:\My Drive\Daily reports\`

## View Your Files

### In File Explorer
1. Open File Explorer (Windows + E)
2. Navigate to `G:\My Drive\Daily reports`

### In Web Browser
Visit: https://drive.google.com/drive/my-drive

## Customization

### Change Cleanup Period

```bash
# Keep files for 30 days instead of 7
./scripts/reporting/upload_eod_simple.sh nico 30

# Never delete old files
./scripts/reporting/upload_eod_simple.sh nico 0
```

### Change Google Drive Folder

Edit `scripts/reporting/upload_eod_simple.sh`:
```bash
GDRIVE_PATH="G:\\My Drive\\Your Custom Folder"
```

## Troubleshooting

### "G: drive not found"
- Make sure Google Drive for Desktop is running
- Check the system tray for the Google Drive icon
- Restart Google Drive if needed

### "Permission denied"
- Close any Word documents that might have the file open
- Make sure you have write access to the Google Drive folder

### Script shows "^M: bad interpreter"
```bash
# Fix line endings
sed -i 's/\r$//' scripts/reporting/upload_eod_simple.sh
```

## Comparison: Simple vs OAuth Method

| Feature | Simple (File Stream) | OAuth Method |
|---------|---------------------|--------------|
| Setup Required | None (if Drive installed) | Complex OAuth setup |
| Google Drive Version | File Stream/Desktop | Any |
| Network Required | Yes (syncs in background) | Yes |
| Automation | Easy shell script | Full API access |
| Best For | Daily manual uploads | CI/CD automation |

**Recommendation:** Use the simple method if you have Google Drive for Desktop installed. It's much easier!

## Files in This System

- `scripts/reporting/upload_eod_simple.sh` - Simple upload script (File Stream)
- `scripts/reporting/upload_to_gdrive.py` - Advanced OAuth method (not needed if you use File Stream)
- `GOOGLE_DRIVE_SETUP.md` - OAuth setup guide (only needed for API method)
