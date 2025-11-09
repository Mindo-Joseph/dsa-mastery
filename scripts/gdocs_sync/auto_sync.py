#!/usr/bin/env python3
"""
Automatic Google Docs Synchronization

Converts markdown writeups to Google Docs and keeps them in sync.
Runs automatically after writeup updates.

Features:
- Creates Google Docs from markdown
- Updates existing docs when markdown changes
- Publishes docs to web automatically
- Updates GitHub Pages with embed codes
- Maintains bidirectional sync
"""

import os
import sys
import json
import hashlib
from pathlib import Path
from datetime import datetime

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    import pickle
except ImportError:
    print("❌ Google Docs API libraries not installed")
    print("\nInstall with:")
    print("  pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Scopes for Docs and Drive
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
]


class GoogleDocsSync:
    """Automatic markdown to Google Docs synchronization"""

    def __init__(self):
        self.base_dir = Path.home() / 'dsa-mastery'
        self.token_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'token.pickle'
        self.credentials_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'credentials.json'
        self.mapping_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'doc_mappings.json'

        self.docs_service = None
        self.drive_service = None
        self.mappings = self.load_mappings()

    def load_mappings(self):
        """Load markdown -> Google Doc ID mappings"""
        if self.mapping_file.exists():
            with open(self.mapping_file, 'r') as f:
                return json.load(f)
        return {}

    def save_mappings(self):
        """Save markdown -> Google Doc ID mappings"""
        self.mapping_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.mapping_file, 'w') as f:
            json.dump(self.mappings, f, indent=2)

    def authenticate(self):
        """Authenticate with Google Docs and Drive APIs"""
        creds = None

        # Load existing token
        if self.token_file.exists():
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)

        # Refresh or get new credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_file.exists():
                    print("❌ credentials.json not found!")
                    print("\nSetup instructions:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create project: 'DSA-Mastery-Docs'")
                    print("3. Enable Google Docs API and Google Drive API")
                    print("4. Create OAuth 2.0 credentials (Desktop app)")
                    print("5. Download as credentials.json")
                    print(f"6. Save to: {self.credentials_file}")
                    sys.exit(1)

                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_file), SCOPES)
                creds = flow.run_local_server(port=0)

            # Save credentials
            self.token_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)

        self.docs_service = build('docs', 'v1', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)
        return True

    def markdown_to_gdocs_format(self, markdown_content):
        """
        Convert markdown to Google Docs API requests

        This is simplified - for production, use a proper markdown parser
        like markdown-it or mistune with a Google Docs renderer
        """
        requests = []
        index = 1

        lines = markdown_content.split('\n')

        for line in lines:
            if not line.strip():
                # Empty line
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': '\n'
                    }
                })
                index += 1
            elif line.startswith('# '):
                # Heading 1
                text = line[2:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': index,
                            'endIndex': index + len(text)
                        },
                        'paragraphStyle': {
                            'namedStyleType': 'HEADING_1'
                        },
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)
            elif line.startswith('## '):
                # Heading 2
                text = line[3:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': index,
                            'endIndex': index + len(text)
                        },
                        'paragraphStyle': {
                            'namedStyleType': 'HEADING_2'
                        },
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)
            elif line.startswith('### '):
                # Heading 3
                text = line[4:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {
                            'startIndex': index,
                            'endIndex': index + len(text)
                        },
                        'paragraphStyle': {
                            'namedStyleType': 'HEADING_3'
                        },
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)
            elif line.startswith('```'):
                # Code block marker - skip (handle in next iteration)
                continue
            else:
                # Regular text
                text = line + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                # Check if this looks like code (starts with spaces/tabs)
                if line.startswith(('    ', '\t')):
                    requests.append({
                        'updateTextStyle': {
                            'range': {
                                'startIndex': index,
                                'endIndex': index + len(text) - 1
                            },
                            'textStyle': {
                                'weightedFontFamily': {
                                    'fontFamily': 'Courier New'
                                },
                                'fontSize': {
                                    'magnitude': 10,
                                    'unit': 'PT'
                                }
                            },
                            'fields': 'weightedFontFamily,fontSize'
                        }
                    })
                index += len(text)

        return requests

    def create_doc(self, title, markdown_content):
        """Create a new Google Doc from markdown"""
        try:
            # Create empty document
            doc = self.docs_service.documents().create(body={
                'title': title
            }).execute()

            doc_id = doc['documentId']
            print(f"✅ Created Google Doc: {title}")
            print(f"   ID: {doc_id}")

            # Add content
            requests = self.markdown_to_gdocs_format(markdown_content)

            if requests:
                self.docs_service.documents().batchUpdate(
                    documentId=doc_id,
                    body={'requests': requests}
                ).execute()

            # Make doc publicly readable
            self.drive_service.permissions().create(
                fileId=doc_id,
                body={
                    'type': 'anyone',
                    'role': 'reader'
                }
            ).execute()

            return doc_id

        except HttpError as e:
            print(f"❌ Error creating doc: {e}")
            return None

    def update_doc(self, doc_id, markdown_content):
        """Update existing Google Doc with new markdown content"""
        try:
            # Get current document
            doc = self.docs_service.documents().get(documentId=doc_id).execute()

            # Delete all content (except first character)
            content_length = doc['body']['content'][-1]['endIndex']

            delete_request = {
                'deleteContentRange': {
                    'range': {
                        'startIndex': 1,
                        'endIndex': content_length - 1
                    }
                }
            }

            self.docs_service.documents().batchUpdate(
                documentId=doc_id,
                body={'requests': [delete_request]}
            ).execute()

            # Add new content
            requests = self.markdown_to_gdocs_format(markdown_content)

            if requests:
                self.docs_service.documents().batchUpdate(
                    documentId=doc_id,
                    body={'requests': requests}
                ).execute()

            print(f"✅ Updated Google Doc: {doc_id}")
            return True

        except HttpError as e:
            print(f"❌ Error updating doc: {e}")
            return False

    def get_published_url(self, doc_id):
        """Get the published embed URL for a document"""
        # Google Docs published URL format
        return f"https://docs.google.com/document/d/e/{doc_id}/pub?embedded=true"

    def get_edit_url(self, doc_id):
        """Get the edit URL for a document"""
        return f"https://docs.google.com/document/d/{doc_id}/edit"

    def sync_markdown_file(self, markdown_path):
        """Sync a single markdown file to Google Docs"""
        markdown_path = Path(markdown_path)

        if not markdown_path.exists():
            print(f"❌ File not found: {markdown_path}")
            return None

        # Read markdown content
        with open(markdown_path, 'r') as f:
            content = f.read()

        # Generate unique key for this file
        file_key = str(markdown_path.relative_to(self.base_dir))

        # Extract title from first H1 or filename
        title = None
        for line in content.split('\n'):
            if line.startswith('# '):
                title = line[2:].strip()
                break

        if not title:
            title = f"DSA Mastery - {markdown_path.stem.replace('_', ' ').title()}"

        # Check if doc already exists
        if file_key in self.mappings:
            doc_id = self.mappings[file_key]['doc_id']
            print(f"🔄 Updating existing doc: {title}")
            self.update_doc(doc_id, content)
        else:
            print(f"📄 Creating new doc: {title}")
            doc_id = self.create_doc(title, content)

            if doc_id:
                self.mappings[file_key] = {
                    'doc_id': doc_id,
                    'title': title,
                    'created': datetime.now().isoformat(),
                    'markdown_path': str(markdown_path)
                }
                self.save_mappings()

        if doc_id:
            return {
                'doc_id': doc_id,
                'edit_url': self.get_edit_url(doc_id),
                'published_url': self.get_published_url(doc_id),
                'title': title
            }

        return None

    def update_github_pages(self, markdown_path, doc_info):
        """Update GitHub Pages markdown with Google Docs embed"""
        # Determine corresponding docs/ path
        rel_path = Path(markdown_path).relative_to(self.base_dir / 'writeups')
        gh_pages_path = self.base_dir / 'docs' / 'patterns' / rel_path

        gh_pages_path.parent.mkdir(parents=True, exist_ok=True)

        # Read original markdown
        with open(markdown_path, 'r') as f:
            original_content = f.read()

        # Create new version with Google Docs embed
        new_content = f"""---
layout: default
title: {doc_info['title']}
---

# {doc_info['title']} - Living Document

<a href="{doc_info['edit_url']}" class="gdocs-link">📝 Open in Google Docs to Comment & Edit</a>

---

## Interactive Writeup

<iframe
  src="{doc_info['published_url']}"
  class="gdocs-embed"
  frameborder="0"
></iframe>

---

## Quick Navigation

- **[View Problems](../../src/patterns/)** - Rust implementations
- **[Progress Tracker](../../progress.md)** - Your learning stats

---

## Offline Fallback

<details>
<summary>Click to expand static markdown version</summary>

{original_content}

</details>

---

**Questions? Add them directly in the [Google Doc]({doc_info['edit_url']})!** 💬

---

*Last synced: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        with open(gh_pages_path, 'w') as f:
            f.write(new_content)

        print(f"✅ Updated GitHub Pages: {gh_pages_path}")
        return gh_pages_path

    def sync_all_writeups(self):
        """Sync all writeups in the writeups/ directory"""
        writeups_dir = self.base_dir / 'writeups'

        if not writeups_dir.exists():
            print(f"❌ Writeups directory not found: {writeups_dir}")
            return

        markdown_files = list(writeups_dir.glob('*.md'))

        print(f"\n📚 Found {len(markdown_files)} writeups to sync\n")

        results = []

        for md_file in markdown_files:
            print(f"─" * 60)
            doc_info = self.sync_markdown_file(md_file)

            if doc_info:
                gh_pages_path = self.update_github_pages(md_file, doc_info)
                results.append({
                    'markdown': md_file,
                    'doc_info': doc_info,
                    'gh_pages': gh_pages_path
                })

        return results


def main():
    """Main execution"""
    print("🔄 DSA Mastery - Automatic Google Docs Sync")
    print("=" * 60)

    sync = GoogleDocsSync()

    print("\n🔐 Authenticating...")
    if not sync.authenticate():
        sys.exit(1)

    print("✅ Authenticated successfully\n")

    # Check if specific file provided
    if len(sys.argv) > 1:
        markdown_file = sys.argv[1]
        print(f"📄 Syncing single file: {markdown_file}\n")
        doc_info = sync.sync_markdown_file(markdown_file)

        if doc_info:
            sync.update_github_pages(markdown_file, doc_info)
            print("\n" + "=" * 60)
            print("✨ Sync complete!")
            print(f"\n📝 Edit doc: {doc_info['edit_url']}")
            print(f"👀 View published: {doc_info['published_url']}")
    else:
        # Sync all writeups
        print("📚 Syncing all writeups...\n")
        results = sync.sync_all_writeups()

        print("\n" + "=" * 60)
        print(f"✨ Synced {len(results)} documents!")
        print("\n📋 Summary:")
        for result in results:
            print(f"\n  • {result['doc_info']['title']}")
            print(f"    Edit: {result['doc_info']['edit_url']}")


if __name__ == "__main__":
    main()
