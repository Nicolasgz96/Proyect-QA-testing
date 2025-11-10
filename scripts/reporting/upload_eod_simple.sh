#!/bin/bash
# Simple EOD upload script using Google Drive File Stream
# This script copies EOD files to Google Drive (G:\My Drive\Daily reports)
# and optionally deletes older files

GDRIVE_PATH="G:\\My Drive\\Daily reports"
LOCAL_REPORTS="documentation/reports"
TESTER_NAME="${1:-nico}"
DELETE_DAYS_OLD="${2:-7}"

echo "================================================"
echo "EOD Report Upload to Google Drive"
echo "================================================"
echo ""

# Find the most recent EOD file
LATEST_EOD=$(ls -t "$LOCAL_REPORTS"/EOD_*.docx 2>/dev/null | head -1)

if [ -z "$LATEST_EOD" ]; then
    echo "ERROR: No EOD files found in $LOCAL_REPORTS"
    exit 1
fi

EOD_FILENAME=$(basename "$LATEST_EOD")
echo "Latest EOD file: $EOD_FILENAME"
echo ""

# Copy to Google Drive
echo "Uploading to Google Drive..."
powershell.exe -Command "Copy-Item '$LATEST_EOD' -Destination '$GDRIVE_PATH\\$EOD_FILENAME' -Force"

if [ $? -eq 0 ]; then
    echo "✓ File uploaded successfully to Google Drive!"
    echo "  Location: G:\\My Drive\\Daily reports\\$EOD_FILENAME"
else
    echo "✗ Upload failed!"
    exit 1
fi

echo ""

# Delete old files (older than specified days)
if [ "$DELETE_DAYS_OLD" -gt 0 ]; then
    echo "Cleaning up old EOD files (older than $DELETE_DAYS_OLD days)..."

    CUTOFF_DATE=$(date -d "$DELETE_DAYS_OLD days ago" +%Y-%m-%d 2>/dev/null || date -v-${DELETE_DAYS_OLD}d +%Y-%m-%d)

    powershell.exe -Command "
        Get-ChildItem '$GDRIVE_PATH' -Filter 'EOD_*.docx' |
        Where-Object { \$_.Name -match 'EOD_(\d{4}-\d{2}-\d{2})' -and \$Matches[1] -lt '$CUTOFF_DATE' } |
        ForEach-Object {
            Write-Host \"  Deleting: \$(\$_.Name)\"
            Remove-Item \$_.FullName -Force
        }
    "
    echo "✓ Cleanup complete!"
fi

echo ""
echo "================================================"
echo "Upload Complete!"
echo "================================================"
echo ""
echo "View your file at:"
echo "https://drive.google.com/drive/my-drive"
