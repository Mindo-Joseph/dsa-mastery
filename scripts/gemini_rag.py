#!/usr/bin/env python3
"""
Gemini RAG Integration for DSA Mastery
Uses direct file uploads for RAG (simpler, works immediately)
"""

import os
import json
import time
from pathlib import Path
from typing import List, Optional
from google import genai


class GeminiRAG:
    """Manage Gemini RAG with direct file uploads"""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize Gemini client"""
        api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        self.client = genai.Client(api_key=api_key)
        self.files_db = Path("progress/uploaded_files.json")
        self.uploaded_files = self._load_files_db()

    def _load_files_db(self):
        """Load database of uploaded files"""
        if self.files_db.exists():
            with open(self.files_db) as f:
                return json.load(f)
        return {}

    def _save_files_db(self):
        """Save database of uploaded files"""
        self.files_db.parent.mkdir(exist_ok=True)
        with open(self.files_db, 'w') as f:
            json.dump(self.uploaded_files, f, indent=2)

    def upload_file(self, file_path: str, display_name: Optional[str] = None):
        """
        Upload a file to Gemini

        Args:
            file_path: Path to file
            display_name: Display name for file

        Returns:
            Uploaded file object
        """
        display_name = display_name or Path(file_path).name

        print(f"📤 Uploading: {display_name}...", end=' ', flush=True)

        try:
            # Upload file
            uploaded_file = self.client.files.upload(file=file_path)

            # Wait for processing
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(2)
                uploaded_file = self.client.files.get(name=uploaded_file.name)

            if uploaded_file.state.name == "FAILED":
                print(f"❌ Failed")
                return None

            # Store in database
            self.uploaded_files[display_name] = {
                'file_name': uploaded_file.name,
                'display_name': display_name,
                'uri': uploaded_file.uri,
                'upload_time': time.time()
            }
            self._save_files_db()

            print(f"✅")
            return uploaded_file

        except Exception as e:
            print(f"❌ Error: {e}")
            return None

    def get_file(self, display_name: str):
        """Get uploaded file by display name"""
        if display_name not in self.uploaded_files:
            return None

        file_info = self.uploaded_files[display_name]

        try:
            # Check if file still exists
            file_obj = self.client.files.get(name=file_info['file_name'])
            return file_obj
        except:
            # File expired (48 hour limit)
            print(f"⚠️  File '{display_name}' expired, please re-upload")
            del self.uploaded_files[display_name]
            self._save_files_db()
            return None

    def list_files(self):
        """List all uploaded files"""
        print("\n📚 Uploaded Files:")
        print("=" * 60)

        if not self.uploaded_files:
            print("No files uploaded yet")
            return

        for display_name, info in self.uploaded_files.items():
            age_hours = (time.time() - info['upload_time']) / 3600
            status = "✅ Active" if age_hours < 48 else "⚠️  Expired (re-upload needed)"
            print(f"{display_name}")
            print(f"  Status: {status}")
            print(f"  Age: {age_hours:.1f} hours")
            print()

    def query(self, question: str, use_files: List[str] = None, model: str = "gemini-2.0-flash-exp"):
        """
        Query with RAG using uploaded files

        Args:
            question: Question to ask
            use_files: List of file display names to query (None = all files)
            model: Model to use

        Returns:
            Response text
        """
        # Get files to use
        files_to_use = use_files if use_files else list(self.uploaded_files.keys())

        if not files_to_use:
            print("⚠️  No files available for querying")
            return None

        print(f"\n🔍 Querying: {question}")
        print(f"📚 Using files: {', '.join(files_to_use)}\n")

        # Get file objects
        file_objects = []
        for display_name in files_to_use:
            file_obj = self.get_file(display_name)
            if file_obj:
                file_objects.append(file_obj)

        if not file_objects:
            print("❌ No valid files available (may have expired)")
            return None

        try:
            # Query with files
            response = self.client.models.generate_content(
                model=model,
                contents=[question] + file_objects
            )

            return response.text

        except Exception as e:
            print(f"❌ Query failed: {e}")
            return None

    def query_and_print(self, question: str, use_files: List[str] = None):
        """Query and print result"""
        result = self.query(question, use_files)

        if result:
            print("📝 Answer:")
            print("=" * 60)
            print(result)
            print("=" * 60)

        return result


def main():
    """CLI interface"""
    import argparse

    parser = argparse.ArgumentParser(description='Gemini RAG for DSA Mastery')
    parser.add_argument('action', choices=['upload', 'query', 'list'],
                        help='Action to perform')
    parser.add_argument('--file', help='File to upload')
    parser.add_argument('--name', help='Display name for file')
    parser.add_argument('--question', '-q', help='Question to ask')
    parser.add_argument('--use-files', nargs='+', help='Specific files to query')

    args = parser.parse_args()

    try:
        rag = GeminiRAG()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\nSet your API key:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        return 1

    if args.action == 'upload':
        if not args.file:
            print("❌ Error: --file required for upload")
            return 1
        rag.upload_file(args.file, args.name)

    elif args.action == 'query':
        if not args.question:
            print("❌ Error: --question required for query")
            return 1
        rag.query_and_print(args.question, args.use_files)

    elif args.action == 'list':
        rag.list_files()

    return 0


if __name__ == '__main__':
    exit(main())
