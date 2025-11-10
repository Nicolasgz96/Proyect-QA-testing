#!/usr/bin/env python3
"""
Upload EOD reports to Google Drive.

This script provides functionality to:
- Authenticate with Google Drive using OAuth2
- Upload EOD reports to a specific Google Drive folder
- Delete old EOD reports from Google Drive
- List EOD files in Google Drive

Usage:
    # Upload a file
    python upload_to_gdrive.py --upload path/to/EOD_file.docx

    # List files in Google Drive
    python upload_to_gdrive.py --list

    # Delete a file by name
    python upload_to_gdrive.py --delete "EOD_2025-11-09_nico.docx"

    # Upload and delete yesterday's EOD
    python upload_to_gdrive.py --upload EOD_2025-11-10_nico.docx --delete-yesterday

Author: QA Team
"""

import sys
import argparse
import pickle
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, List, Dict
import os.path

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from common.docx_utils import (
    get_report_output_path,
    print_section_header
)

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("ERROR: Google API libraries not installed.", file=sys.stderr)
    print("Please run: pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client", file=sys.stderr)
    sys.exit(1)

# Google Drive API scopes
SCOPES = ['https://www.googleapis.com/auth/drive.file']

# Credentials file paths
TOKEN_FILE = 'token.pickle'
CREDENTIALS_FILE = 'credentials.json'

# Google Drive folder name for EOD reports
GDRIVE_FOLDER_NAME = "EOD Reports - Hello Britannica"


def get_credentials() -> Optional[Credentials]:
    """
    Get or create Google Drive API credentials.

    Returns:
        Google credentials object or None if authentication fails
    """
    creds = None

    # Token file stores the user's access and refresh tokens
    if os.path.exists(TOKEN_FILE):
        try:
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        except Exception as e:
            print(f"Warning: Could not load token file: {e}", file=sys.stderr)

    # If no valid credentials, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Refreshing expired credentials...")
                creds.refresh(Request())
            except Exception as e:
                print(f"Error refreshing credentials: {e}", file=sys.stderr)
                creds = None

        if not creds:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERROR: Credentials file '{CREDENTIALS_FILE}' not found.", file=sys.stderr)
                print("\nTo set up Google Drive authentication:", file=sys.stderr)
                print("1. Go to https://console.cloud.google.com/", file=sys.stderr)
                print("2. Create a new project or select existing one", file=sys.stderr)
                print("3. Enable Google Drive API", file=sys.stderr)
                print("4. Create OAuth 2.0 credentials (Desktop app)", file=sys.stderr)
                print("5. Download credentials and save as 'credentials.json' in project root", file=sys.stderr)
                return None

            try:
                print("Starting OAuth2 authentication flow...")
                print("A browser window will open for authentication.")
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as e:
                print(f"ERROR: Authentication failed: {e}", file=sys.stderr)
                return None

        # Save credentials for next run
        try:
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
            print(f"Credentials saved to {TOKEN_FILE}")
        except Exception as e:
            print(f"Warning: Could not save credentials: {e}", file=sys.stderr)

    return creds


def get_or_create_folder(service, folder_name: str) -> Optional[str]:
    """
    Get or create a folder in Google Drive.

    Args:
        service: Google Drive API service instance
        folder_name: Name of the folder

    Returns:
        Folder ID or None if operation fails
    """
    try:
        # Search for existing folder
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        results = service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name)'
        ).execute()

        folders = results.get('files', [])

        if folders:
            folder_id = folders[0]['id']
            print(f"Found existing folder: {folder_name} (ID: {folder_id})")
            return folder_id

        # Create new folder
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = service.files().create(
            body=file_metadata,
            fields='id'
        ).execute()

        folder_id = folder.get('id')
        print(f"Created new folder: {folder_name} (ID: {folder_id})")
        return folder_id

    except HttpError as e:
        print(f"ERROR: Could not get/create folder: {e}", file=sys.stderr)
        return None


def upload_file(service, file_path: Path, folder_id: str) -> Optional[str]:
    """
    Upload a file to Google Drive.

    Args:
        service: Google Drive API service instance
        file_path: Path to file to upload
        folder_id: ID of the folder to upload to

    Returns:
        File ID of uploaded file or None if upload fails
    """
    try:
        file_metadata = {
            'name': file_path.name,
            'parents': [folder_id]
        }

        media = MediaFileUpload(
            str(file_path),
            mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            resumable=True
        )

        print(f"Uploading: {file_path.name}...")

        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id, name, webViewLink'
        ).execute()

        file_id = file.get('id')
        web_link = file.get('webViewLink')

        print(f"SUCCESS: File uploaded!")
        print(f"  Name: {file_path.name}")
        print(f"  ID: {file_id}")
        print(f"  Link: {web_link}")

        return file_id

    except HttpError as e:
        print(f"ERROR: Upload failed: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"ERROR: Unexpected error during upload: {e}", file=sys.stderr)
        return None


def list_files(service, folder_id: str) -> List[Dict]:
    """
    List files in a Google Drive folder.

    Args:
        service: Google Drive API service instance
        folder_id: ID of the folder

    Returns:
        List of file dictionaries with id, name, createdTime
    """
    try:
        query = f"'{folder_id}' in parents and trashed=false"
        results = service.files().list(
            q=query,
            spaces='drive',
            fields='files(id, name, createdTime, modifiedTime, webViewLink)',
            orderBy='createdTime desc'
        ).execute()

        files = results.get('files', [])
        return files

    except HttpError as e:
        print(f"ERROR: Could not list files: {e}", file=sys.stderr)
        return []


def delete_file(service, file_id: str, file_name: str) -> bool:
    """
    Delete a file from Google Drive.

    Args:
        service: Google Drive API service instance
        file_id: ID of file to delete
        file_name: Name of file (for logging)

    Returns:
        True if successful, False otherwise
    """
    try:
        service.files().delete(fileId=file_id).execute()
        print(f"Deleted: {file_name}")
        return True

    except HttpError as e:
        print(f"ERROR: Could not delete file '{file_name}': {e}", file=sys.stderr)
        return False


def find_file_by_name(service, folder_id: str, file_name: str) -> Optional[str]:
    """
    Find a file by name in a folder.

    Args:
        service: Google Drive API service instance
        folder_id: Folder ID to search in
        file_name: Name of file to find

    Returns:
        File ID if found, None otherwise
    """
    files = list_files(service, folder_id)
    for file in files:
        if file['name'] == file_name:
            return file['id']
    return None


def delete_yesterday_eod(service, folder_id: str, tester_name: str) -> bool:
    """
    Delete yesterday's EOD file from Google Drive.

    Args:
        service: Google Drive API service instance
        folder_id: Folder ID containing EOD files
        tester_name: Name of the tester

    Returns:
        True if file was found and deleted, False otherwise
    """
    yesterday = datetime.now() - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")

    # Try multiple possible filenames
    possible_names = [
        f"EOD_{yesterday_date}_{tester_name}.docx",
        f"EOD_{yesterday_date}_{tester_name.replace(' ', '_')}.docx",
    ]

    for file_name in possible_names:
        file_id = find_file_by_name(service, folder_id, file_name)
        if file_id:
            print(f"Found yesterday's EOD: {file_name}")
            return delete_file(service, file_id, file_name)

    print(f"No EOD file found for yesterday ({yesterday_date})")
    return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Upload EOD reports to Google Drive",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Upload a file
  python upload_to_gdrive.py --upload documentation/reports/EOD_2025-11-10_nico.docx

  # List files in Google Drive
  python upload_to_gdrive.py --list

  # Delete a specific file
  python upload_to_gdrive.py --delete "EOD_2025-11-09_nico.docx"

  # Upload today's EOD and delete yesterday's
  python upload_to_gdrive.py --upload EOD_2025-11-10_nico.docx --delete-yesterday --tester nico
        """
    )

    parser.add_argument(
        '--upload',
        type=Path,
        help='Path to file to upload'
    )

    parser.add_argument(
        '--list',
        action='store_true',
        help='List files in Google Drive folder'
    )

    parser.add_argument(
        '--delete',
        type=str,
        help='Delete a file by name'
    )

    parser.add_argument(
        '--delete-yesterday',
        action='store_true',
        help='Delete yesterday\'s EOD file'
    )

    parser.add_argument(
        '--tester',
        type=str,
        default='nico',
        help='Tester name (for finding yesterday\'s file)'
    )

    parser.add_argument(
        '--folder',
        type=str,
        default=GDRIVE_FOLDER_NAME,
        help=f'Google Drive folder name (default: {GDRIVE_FOLDER_NAME})'
    )

    args = parser.parse_args()

    # Validate arguments
    if not any([args.upload, args.list, args.delete, args.delete_yesterday]):
        parser.print_help()
        print("\nERROR: Please specify an action (--upload, --list, --delete, or --delete-yesterday)", file=sys.stderr)
        return 1

    try:
        # Authenticate
        print_section_header("Google Drive Authentication")
        creds = get_credentials()
        if not creds:
            return 1

        # Build service
        service = build('drive', 'v3', credentials=creds)
        print("Successfully connected to Google Drive API")

        # Get or create folder
        print_section_header(f"Accessing Folder: {args.folder}")
        folder_id = get_or_create_folder(service, args.folder)
        if not folder_id:
            return 1

        # Handle actions
        if args.upload:
            print_section_header("Uploading File")

            if not args.upload.exists():
                print(f"ERROR: File not found: {args.upload}", file=sys.stderr)
                return 1

            file_id = upload_file(service, args.upload, folder_id)
            if not file_id:
                return 1

        if args.delete:
            print_section_header(f"Deleting File: {args.delete}")
            file_id = find_file_by_name(service, folder_id, args.delete)
            if not file_id:
                print(f"ERROR: File not found: {args.delete}", file=sys.stderr)
                return 1

            if not delete_file(service, file_id, args.delete):
                return 1

        if args.delete_yesterday:
            print_section_header("Deleting Yesterday's EOD")
            delete_yesterday_eod(service, folder_id, args.tester)

        if args.list:
            print_section_header("Files in Google Drive")
            files = list_files(service, folder_id)

            if not files:
                print("No files found in folder")
            else:
                print(f"Found {len(files)} file(s):\n")
                for file in files:
                    created = file.get('createdTime', 'N/A')
                    print(f"  • {file['name']}")
                    print(f"    ID: {file['id']}")
                    print(f"    Created: {created}")
                    print(f"    Link: {file.get('webViewLink', 'N/A')}")
                    print()

        print_section_header("Operation Complete")
        return 0

    except HttpError as e:
        print(f"ERROR: Google Drive API error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"ERROR: Unexpected error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
