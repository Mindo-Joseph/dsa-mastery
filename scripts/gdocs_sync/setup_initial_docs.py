#!/usr/bin/env python3
"""
One-Time Setup: Create Google Docs from Markdown

Run this ONCE to create initial Google Docs from your writeups.
After this, you edit the Google Docs and use pull_from_docs.py to sync back.

Workflow:
1. Run this script (creates Google Docs)
2. Script prints URLs
3. You bookmark/save URLs
4. You edit Google Docs
5. Run pull_from_docs.py to sync back
"""

import os
import sys
import json
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
    print("❌ Google API libraries not installed")
    print("\nInstall with:")
    print("  pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Scopes for creating and editing docs
SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive.file'
]


class InitialDocsSetup:
    """One-time setup: Create Google Docs from existing markdown"""

    def __init__(self):
        self.base_dir = Path.home() / 'dsa-mastery'
        self.token_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'token.pickle'
        self.credentials_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'credentials.json'
        self.mapping_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'doc_mappings.json'

        self.docs_service = None
        self.drive_service = None
        self.mappings = {}

    def authenticate(self):
        """Authenticate with Google APIs"""
        creds = None

        if self.token_file.exists():
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_file.exists():
                    print("❌ credentials.json not found!")
                    print("\n📋 Setup Instructions:")
                    print("=" * 60)
                    print("1. Go to: https://console.cloud.google.com/")
                    print("2. Create project: 'DSA-Mastery-Docs'")
                    print("3. Enable APIs:")
                    print("   - Google Docs API")
                    print("   - Google Drive API")
                    print("4. Create OAuth 2.0 credentials (Desktop app)")
                    print("5. Download credentials.json")
                    print(f"6. Save to: {self.credentials_file}")
                    print("=" * 60)
                    sys.exit(1)

                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_file), SCOPES)
                creds = flow.run_local_server(port=0)

            self.token_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)

        self.docs_service = build('docs', 'v1', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)
        return True

    def markdown_to_doc_requests(self, markdown_content):
        """
        Convert markdown to Google Docs API requests
        Simplified version - handles basic formatting
        """
        requests = []
        index = 1

        lines = markdown_content.split('\n')
        in_code_block = False
        code_block_lines = []

        for line in lines:
            # Code block toggle
            if line.strip().startswith('```'):
                if in_code_block:
                    # End of code block - insert it
                    code_text = '\n'.join(code_block_lines) + '\n'
                    requests.append({
                        'insertText': {
                            'location': {'index': index},
                            'text': code_text
                        }
                    })
                    requests.append({
                        'updateTextStyle': {
                            'range': {
                                'startIndex': index,
                                'endIndex': index + len(code_text)
                            },
                            'textStyle': {
                                'weightedFontFamily': {'fontFamily': 'Courier New'},
                                'fontSize': {'magnitude': 10, 'unit': 'PT'},
                                'backgroundColor': {
                                    'color': {'rgbColor': {'red': 0.95, 'green': 0.95, 'blue': 0.95}}
                                }
                            },
                            'fields': 'weightedFontFamily,fontSize,backgroundColor'
                        }
                    })
                    index += len(code_text)
                    code_block_lines = []
                in_code_block = not in_code_block
                continue

            if in_code_block:
                code_block_lines.append(line)
                continue

            # Handle different line types
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
                # H1
                text = line[2:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {'startIndex': index, 'endIndex': index + len(text)},
                        'paragraphStyle': {'namedStyleType': 'HEADING_1'},
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)

            elif line.startswith('## '):
                # H2
                text = line[3:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {'startIndex': index, 'endIndex': index + len(text)},
                        'paragraphStyle': {'namedStyleType': 'HEADING_2'},
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)

            elif line.startswith('### '):
                # H3
                text = line[4:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'updateParagraphStyle': {
                        'range': {'startIndex': index, 'endIndex': index + len(text)},
                        'paragraphStyle': {'namedStyleType': 'HEADING_3'},
                        'fields': 'namedStyleType'
                    }
                })
                index += len(text)

            elif line.startswith('- ') or line.startswith('* '):
                # Bullet list
                text = line[2:].strip() + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                requests.append({
                    'createParagraphBullets': {
                        'range': {'startIndex': index, 'endIndex': index + len(text)},
                        'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
                    }
                })
                index += len(text)

            else:
                # Regular text
                text = line + '\n'
                requests.append({
                    'insertText': {
                        'location': {'index': index},
                        'text': text
                    }
                })
                index += len(text)

        return requests

    def create_doc_from_markdown(self, markdown_path):
        """Create a Google Doc from a markdown file"""
        markdown_path = Path(markdown_path)

        if not markdown_path.exists():
            print(f"❌ File not found: {markdown_path}")
            return None

        # Read markdown
        with open(markdown_path, 'r') as f:
            content = f.read()

        # Extract title from first H1
        title = None
        for line in content.split('\n'):
            if line.startswith('# '):
                title = line[2:].strip()
                break

        if not title:
            title = f"DSA Mastery - {markdown_path.stem.replace('_', ' ').title()}"

        # Create document
        try:
            print(f"📄 Creating: {title}")

            doc = self.docs_service.documents().create(body={'title': title}).execute()
            doc_id = doc['documentId']

            print(f"   ID: {doc_id}")

            # Add content
            requests = self.markdown_to_doc_requests(content)

            if requests:
                # Batch update in chunks (API limit is 500 requests)
                chunk_size = 400
                for i in range(0, len(requests), chunk_size):
                    chunk = requests[i:i + chunk_size]
                    self.docs_service.documents().batchUpdate(
                        documentId=doc_id,
                        body={'requests': chunk}
                    ).execute()

            # Share: Anyone with link can comment
            self.drive_service.permissions().create(
                fileId=doc_id,
                body={
                    'type': 'anyone',
                    'role': 'commenter'  # Can comment, not edit (you control edits)
                }
            ).execute()

            print(f"✅ Created successfully")

            return {
                'doc_id': doc_id,
                'title': title,
                'edit_url': f"https://docs.google.com/document/d/{doc_id}/edit",
                'created': datetime.now().isoformat()
            }

        except HttpError as e:
            print(f"❌ Error creating doc: {e}")
            return None

    def setup_all_writeups(self):
        """Create Google Docs for all writeups"""
        writeups_dir = self.base_dir / 'writeups'

        if not writeups_dir.exists():
            print(f"❌ Writeups directory not found: {writeups_dir}")
            print("   Expected: ~/dsa-mastery/writeups/")
            return

        markdown_files = sorted(writeups_dir.glob('*.md'))

        if not markdown_files:
            print(f"❌ No markdown files found in {writeups_dir}")
            return

        print(f"\n📚 Found {len(markdown_files)} writeups\n")
        print("=" * 60)

        created_docs = []

        for md_file in markdown_files:
            print()
            doc_info = self.create_doc_from_markdown(md_file)

            if doc_info:
                # Save mapping
                rel_path = str(md_file.relative_to(self.base_dir))
                self.mappings[rel_path] = doc_info

                created_docs.append({
                    'markdown': md_file.name,
                    'title': doc_info['title'],
                    'url': doc_info['edit_url'],
                    'doc_id': doc_info['doc_id']
                })

        # Save mappings
        self.mapping_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.mapping_file, 'w') as f:
            json.dump(self.mappings, f, indent=2)

        # Print summary
        print("\n" + "=" * 60)
        print(f"✨ Created {len(created_docs)} Google Docs!")
        print("\n📋 YOUR DOCUMENTS:")
        print("=" * 60)

        for doc in created_docs:
            print(f"\n📄 {doc['title']}")
            print(f"   {doc['url']}")

        print("\n" + "=" * 60)
        print("\n🎯 NEXT STEPS:")
        print("=" * 60)
        print("\n1. Bookmark these URLs (or create a folder in Google Drive)")
        print("\n2. Edit the Google Docs as you learn:")
        print("   - Add insights, examples, clarifications")
        print("   - Reorganize sections")
        print("   - Add your own notes")
        print("\n3. Periodically pull changes back:")
        print("   python3 scripts/gdocs_sync/pull_from_docs.py")
        print("\n4. Commit and push:")
        print("   git add writeups/ docs/")
        print("   git commit -m 'Synced from Google Docs'")
        print("   git push")
        print("\n" + "=" * 60)

        # Create a shortcuts file
        shortcuts_file = self.base_dir / 'GOOGLE_DOCS_LINKS.md'
        with open(shortcuts_file, 'w') as f:
            f.write("# Your DSA Mastery Google Docs\n\n")
            f.write("**Edit these documents as you learn. They are the source of truth.**\n\n")
            f.write("---\n\n")
            for doc in created_docs:
                f.write(f"## {doc['title']}\n\n")
                f.write(f"**Edit:** {doc['url']}\n\n")
                f.write(f"**Doc ID:** `{doc['doc_id']}`\n\n")
                f.write("---\n\n")
            f.write("\n## Sync Workflow\n\n")
            f.write("```bash\n")
            f.write("# Pull your edits from Google Docs\n")
            f.write("python3 scripts/gdocs_sync/pull_from_docs.py\n\n")
            f.write("# Commit\n")
            f.write("git add .\n")
            f.write("git commit -m 'Updated from Google Docs'\n")
            f.write("git push\n")
            f.write("```\n")

        print(f"\n💾 Saved links to: {shortcuts_file}")
        print()


def main():
    """Main execution"""
    print("🚀 DSA Mastery - Initial Google Docs Setup")
    print("=" * 60)
    print("\nThis creates Google Docs from your markdown writeups.")
    print("Run this ONCE, then edit the Google Docs going forward.\n")

    setup = InitialDocsSetup()

    print("🔐 Authenticating with Google...")
    if not setup.authenticate():
        sys.exit(1)

    print("✅ Authenticated successfully\n")

    setup.setup_all_writeups()


if __name__ == "__main__":
    main()
