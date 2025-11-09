#!/usr/bin/env python3
"""
Pull Updates from Google Docs

Converts Google Docs back to markdown and updates both writeups/ and docs/
This is the main workflow script - run it periodically to sync your edits.

Workflow:
1. Edit Google Doc in browser
2. Run this script
3. Script downloads doc as markdown
4. Updates writeups/ and docs/
5. Commit and push

Usage:
    python3 scripts/gdocs_sync/pull_from_docs.py           # Pull all docs
    python3 scripts/gdocs_sync/pull_from_docs.py <doc_id>  # Pull specific doc
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
    import io
except ImportError:
    print("❌ Google API libraries not installed")
    print("\nInstall with:")
    print("  pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Scopes for Docs and Drive (read + export)
SCOPES = [
    'https://www.googleapis.com/auth/documents.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]


class GoogleDocsPuller:
    """Pull updates from Google Docs to local markdown"""

    def __init__(self):
        self.base_dir = Path.home() / 'dsa-mastery'
        self.token_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'token.pickle'
        self.credentials_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'credentials.json'
        self.mapping_file = self.base_dir / 'scripts' / 'gdocs_sync' / 'doc_mappings.json'

        self.docs_service = None
        self.drive_service = None
        self.mappings = self.load_mappings()

    def load_mappings(self):
        """Load markdown <-> Google Doc ID mappings"""
        if self.mapping_file.exists():
            with open(self.mapping_file, 'r') as f:
                return json.load(f)
        return {}

    def save_mappings(self):
        """Save markdown <-> Google Doc ID mappings"""
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
                    print("\nGet it from: https://console.cloud.google.com/")
                    print(f"Save to: {self.credentials_file}")
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

    def export_doc_as_markdown(self, doc_id):
        """Export Google Doc as markdown using Drive API"""
        try:
            # Export as plain text (closest to markdown)
            # Google Docs doesn't have native markdown export, so we get plain text
            # and preserve structure
            request = self.drive_service.files().export_media(
                fileId=doc_id,
                mimeType='text/plain'
            )

            content = request.execute().decode('utf-8')

            # Get document structure from Docs API to preserve formatting
            doc = self.docs_service.documents().get(documentId=doc_id).execute()

            # Convert to markdown with structure preserved
            markdown = self.gdocs_to_markdown(doc, content)

            return markdown

        except HttpError as e:
            print(f"❌ Error exporting doc {doc_id}: {e}")
            return None

    def gdocs_to_markdown(self, doc, plain_text):
        """
        Convert Google Docs structure to markdown

        This analyzes the document structure and converts:
        - Headings → # ## ###
        - Bold → **text**
        - Italic → *text*
        - Code → `code`
        - Lists → - item or 1. item
        - Links → [text](url)
        """
        markdown_lines = []

        content = doc.get('body', {}).get('content', [])

        for element in content:
            if 'paragraph' in element:
                paragraph = element['paragraph']
                para_style = paragraph.get('paragraphStyle', {})
                named_style = para_style.get('namedStyleType', 'NORMAL_TEXT')

                # Get text elements
                text_elements = paragraph.get('elements', [])
                line_text = ''

                for text_elem in text_elements:
                    if 'textRun' in text_elem:
                        text_run = text_elem['textRun']
                        content_text = text_run.get('content', '')
                        text_style = text_run.get('textStyle', {})

                        # Apply formatting
                        formatted_text = content_text

                        # Bold
                        if text_style.get('bold'):
                            formatted_text = f"**{formatted_text.strip()}**"

                        # Italic
                        if text_style.get('italic'):
                            formatted_text = f"*{formatted_text.strip()}*"

                        # Code (using Courier or monospace font as indicator)
                        font_family = text_style.get('weightedFontFamily', {}).get('fontFamily', '')
                        if 'Courier' in font_family or 'Mono' in font_family or 'Consolas' in font_family:
                            formatted_text = f"`{formatted_text.strip()}`"

                        # Link
                        if 'link' in text_style:
                            url = text_style['link'].get('url', '')
                            formatted_text = f"[{formatted_text.strip()}]({url})"

                        line_text += formatted_text

                # Apply heading styles
                if named_style == 'HEADING_1':
                    line_text = f"# {line_text.strip()}"
                elif named_style == 'HEADING_2':
                    line_text = f"## {line_text.strip()}"
                elif named_style == 'HEADING_3':
                    line_text = f"### {line_text.strip()}"
                elif named_style == 'HEADING_4':
                    line_text = f"#### {line_text.strip()}"

                markdown_lines.append(line_text)

            elif 'table' in element:
                # Tables - convert to markdown table
                # (simplified - just show it's a table)
                markdown_lines.append("\n[Table - view in Google Doc]\n")

        return '\n'.join(markdown_lines)

    def pull_doc(self, doc_id, markdown_path=None):
        """Pull a single Google Doc and update markdown files"""

        # Get document metadata
        try:
            doc_metadata = self.drive_service.files().get(
                fileId=doc_id,
                fields='name,modifiedTime'
            ).execute()

            doc_title = doc_metadata['name']
            modified_time = doc_metadata['modifiedTime']

            print(f"📥 Pulling: {doc_title}")
            print(f"   Last modified: {modified_time}")

        except HttpError as e:
            print(f"❌ Could not get doc metadata: {e}")
            return False

        # Export as markdown
        markdown_content = self.export_doc_as_markdown(doc_id)

        if not markdown_content:
            return False

        # Determine file path
        if not markdown_path:
            # Find in mappings
            for path, info in self.mappings.items():
                if info['doc_id'] == doc_id:
                    markdown_path = self.base_dir / path
                    break

            if not markdown_path:
                # Create new file
                safe_title = doc_title.lower().replace(' ', '_').replace('-', '_')
                # Extract pattern number if present
                if 'two pointer' in doc_title.lower():
                    filename = '01_two_pointers.md'
                elif 'sliding window' in doc_title.lower():
                    filename = '02_sliding_window.md'
                # ... add more patterns
                else:
                    filename = f"{safe_title}.md"

                markdown_path = self.base_dir / 'writeups' / filename

        # Write to writeups/
        markdown_path.parent.mkdir(parents=True, exist_ok=True)
        with open(markdown_path, 'w') as f:
            f.write(markdown_content)

        print(f"✅ Updated: {markdown_path}")

        # Also update docs/ for GitHub Pages
        rel_path = markdown_path.relative_to(self.base_dir / 'writeups')
        gh_pages_path = self.base_dir / 'docs' / 'patterns' / rel_path

        # Create GitHub Pages version with embedded doc
        edit_url = f"https://docs.google.com/document/d/{doc_id}/edit"
        published_url = f"https://docs.google.com/document/d/e/{doc_id}/pub?embedded=true"

        gh_pages_content = f"""---
layout: default
title: {doc_title}
---

# {doc_title}

<a href="{edit_url}" class="gdocs-link">📝 Edit in Google Docs</a>

---

## Live Document

<iframe
  src="{published_url}"
  class="gdocs-embed"
  frameborder="0"
></iframe>

---

## Markdown Version

{markdown_content}

---

*Last synced from Google Docs: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        gh_pages_path.parent.mkdir(parents=True, exist_ok=True)
        with open(gh_pages_path, 'w') as f:
            f.write(gh_pages_content)

        print(f"✅ Updated GitHub Pages: {gh_pages_path}")

        # Update mappings
        rel_path_str = str(markdown_path.relative_to(self.base_dir))
        self.mappings[rel_path_str] = {
            'doc_id': doc_id,
            'title': doc_title,
            'last_synced': datetime.now().isoformat(),
            'modified_time': modified_time
        }
        self.save_mappings()

        return True

    def pull_all_docs(self):
        """Pull all tracked Google Docs"""
        if not self.mappings:
            print("❌ No documents tracked yet")
            print("\nRun setup first:")
            print("  python3 scripts/gdocs_sync/setup_initial_docs.py")
            return

        print(f"\n📚 Pulling {len(self.mappings)} documents...\n")

        success_count = 0
        for markdown_path, info in self.mappings.items():
            doc_id = info['doc_id']
            print("─" * 60)

            if self.pull_doc(doc_id, self.base_dir / markdown_path):
                success_count += 1

            print()

        print("═" * 60)
        print(f"✨ Successfully pulled {success_count}/{len(self.mappings)} documents")
        print("\nNext steps:")
        print("  git add writeups/ docs/")
        print("  git commit -m 'Synced from Google Docs'")
        print("  git push")


def main():
    """Main execution"""
    print("📥 Pull Updates from Google Docs")
    print("=" * 60)

    puller = GoogleDocsPuller()

    print("\n🔐 Authenticating...")
    if not puller.authenticate():
        sys.exit(1)

    print("✅ Authenticated\n")

    # Check if specific doc ID provided
    if len(sys.argv) > 1:
        doc_id = sys.argv[1]
        print(f"📄 Pulling single document: {doc_id}\n")
        print("─" * 60)

        if puller.pull_doc(doc_id):
            print("\n✨ Success!")
            print("\nCommit changes:")
            print("  git add writeups/ docs/")
            print("  git commit -m 'Updated from Google Docs'")
            print("  git push")
    else:
        # Pull all docs
        puller.pull_all_docs()


if __name__ == "__main__":
    main()
