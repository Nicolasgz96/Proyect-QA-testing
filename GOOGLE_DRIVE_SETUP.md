# Google Drive Integration Setup

This guide explains how to set up Google Drive integration for uploading EOD reports.

## Prerequisites

- Python 3 with pip installed
- Google account (ngonzalez@eb.com or your work account)
- Google Drive API enabled

## Step 1: Install Dependencies

The required packages are already installed:
- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

If you need to reinstall:
```bash
python -m pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Step 2: Create Google Cloud Project and Enable Drive API

### Option A: Using Google Cloud Console (Recommended)

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/

2. **Create or Select a Project**
   - Click on the project dropdown at the top
   - Click "NEW PROJECT"
   - Name: "Hello Britannica EOD Reports" (or any name)
   - Click "CREATE"

3. **Enable Google Drive API**
   - In the search bar, type "Google Drive API"
   - Click on "Google Drive API"
   - Click "ENABLE"

4. **Create OAuth 2.0 Credentials**
   - Go to "APIs & Services" > "Credentials"
   - Click "+ CREATE CREDENTIALS" > "OAuth client ID"
   - If prompted, configure OAuth consent screen:
     - User Type: "Internal" (if using workspace) or "External"
     - App name: "EOD Report Uploader"
     - User support email: Your email
     - Developer contact: Your email
     - Scopes: No need to add scopes here
     - Test users: Add your email (ngonzalez@eb.com)
     - Click "SAVE AND CONTINUE" through the steps
   - Back to "Create OAuth client ID":
     - Application type: "Desktop app"
     - Name: "EOD Report Desktop Client"
     - Click "CREATE"

5. **Download Credentials**
   - Click the download icon (⬇) next to your newly created OAuth client
   - Save the file as `credentials.json`
   - Move it to your project root directory:
     ```
     Hello_Britannica/
     └── credentials.json  <-- Place it here
     ```

### Option B: Quick Setup Link

Visit this direct link (requires Google sign-in):
https://console.cloud.google.com/apis/library/drive.googleapis.com

## Step 3: First-Time Authentication

When you run the upload script for the first time, it will:

1. **Open your browser** automatically
2. **Ask you to sign in** with your Google account (ngonzalez@eb.com)
3. **Request permissions** to access Google Drive
4. **Save authentication token** as `token.pickle` in the project root

This only needs to be done once. The `token.pickle` file will be used for subsequent uploads.

## Step 4: Test the Setup

Create a test document and upload it:

```bash
# Test with the sample document
python scripts/reporting/upload_to_gdrive.py --upload documentation/templates/eod_input_template.yaml

# List files in Google Drive
python scripts/reporting/upload_to_gdrive.py --list
```

## Usage Examples

### Upload an EOD Report

```bash
# Upload specific EOD file
python scripts/reporting/upload_to_gdrive.py --upload documentation/reports/EOD_2025-11-10_nico.docx
```

### Upload and Delete Yesterday's EOD

```bash
# Upload today's report and delete yesterday's
python scripts/reporting/upload_to_gdrive.py \
    --upload documentation/reports/EOD_2025-11-10_nico.docx \
    --delete-yesterday \
    --tester nico
```

### List All EOD Files in Google Drive

```bash
python scripts/reporting/upload_to_gdrive.py --list
```

### Delete a Specific File

```bash
python scripts/reporting/upload_to_gdrive.py --delete "EOD_2025-11-09_nico.docx"
```

## Integrated Workflow

You can integrate this into your EOD workflow:

```bash
# 1. Generate EOD report
python scripts/reporting/generate_eod_report.py eod_2025-11-10.yaml

# 2. Upload to Google Drive and delete yesterday's
python scripts/reporting/upload_to_gdrive.py \
    --upload documentation/reports/EOD_2025-11-10_nico.docx \
    --delete-yesterday \
    --tester nico
```

## Google Drive Folder Structure

The script automatically creates a folder named:
```
EOD Reports - Hello Britannica
```

All EOD files are uploaded to this folder. You can customize the folder name:

```bash
python scripts/reporting/upload_to_gdrive.py \
    --upload EOD_file.docx \
    --folder "My Custom Folder Name"
```

## File Structure After Setup

```
Hello_Britannica/
├── credentials.json        # OAuth credentials (DO NOT COMMIT)
├── token.pickle           # Authentication token (DO NOT COMMIT)
├── scripts/
│   └── reporting/
│       ├── generate_eod_report.py
│       └── upload_to_gdrive.py
└── documentation/
    └── reports/
        └── EOD_*.docx
```

## Important Security Notes

⚠️ **DO NOT commit these files to Git:**
- `credentials.json` - Contains your OAuth client secrets
- `token.pickle` - Contains your authentication tokens

Add them to `.gitignore`:
```bash
echo "credentials.json" >> .gitignore
echo "token.pickle" >> .gitignore
```

## Troubleshooting

### "credentials.json not found"
- Make sure you downloaded credentials from Google Cloud Console
- Place it in the project root directory
- File name must be exactly `credentials.json`

### "Token has been expired or revoked"
- Delete `token.pickle`
- Run the upload script again to re-authenticate

### "Access denied"
- Make sure you're signing in with the correct Google account
- Check that you added your email to "Test users" in OAuth consent screen

### "API not enabled"
- Go to Google Cloud Console
- Search for "Google Drive API"
- Click "ENABLE"

## Support

For issues related to:
- **Google Drive API**: Check Google Cloud Console status
- **Script errors**: Review error messages in terminal
- **Authentication**: Delete `token.pickle` and re-authenticate

## References

- Google Drive API Documentation: https://developers.google.com/drive/api/guides/about-sdk
- OAuth 2.0 Setup: https://developers.google.com/identity/protocols/oauth2
