#!/usr/bin/env python3
"""
Gemini File Search Integration for DSA Mastery
Replaces NotebookLM with Gemini API's managed RAG system
"""

import os
import time
import sys
from pathlib import Path
from typing import List, Optional
from google import genai
from google.genai import types


class GeminiFileSearch:
    """Manage Gemini File Search for DSA content indexing and querying"""

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize Gemini File Search client

        Args:
            api_key: Gemini API key (defaults to GEMINI_API_KEY env var)
        """
        api_key = api_key or os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        self.client = genai.Client(api_key=api_key)
        self.store_name = None

    def create_store(self, display_name: str = "dsa-mastery-store") -> str:
        """
        Create a new file search store for DSA content

        Args:
            display_name: Human-readable name for the store

        Returns:
            Store name identifier
        """
        print(f"Creating file search store: {display_name}")
        file_search_store = self.client.file_search_stores.create(
            config={'display_name': display_name}
        )
        self.store_name = file_search_store.name
        print(f"✓ Store created: {self.store_name}")
        return self.store_name

    def get_or_create_store(self, display_name: str = "dsa-mastery-store") -> str:
        """
        Get existing store or create new one

        Args:
            display_name: Human-readable name for the store

        Returns:
            Store name identifier
        """
        # List existing stores
        stores = list(self.client.file_search_stores.list())

        # Find store by display name
        for store in stores:
            if store.display_name == display_name:
                self.store_name = store.name
                print(f"✓ Using existing store: {self.store_name}")
                return self.store_name

        # Create new store if not found
        return self.create_store(display_name)

    def upload_file(
        self,
        file_path: str,
        display_name: Optional[str] = None,
        metadata: Optional[dict] = None
    ) -> bool:
        """
        Upload and index a file to the store

        Args:
            file_path: Path to file to upload
            display_name: Display name for file (defaults to filename)
            metadata: Custom metadata dict (e.g., {'category': 'patterns', 'difficulty': 'medium'})

        Returns:
            True if successful
        """
        if not self.store_name:
            raise ValueError("Store not initialized. Call get_or_create_store() first")

        display_name = display_name or Path(file_path).name

        print(f"  Uploading: {display_name}...", end='')

        try:
            # Upload and import in one step (simplified - no custom metadata for now)
            operation = self.client.file_search_stores.upload_to_file_search_store(
                file=file_path,
                file_search_store_name=self.store_name,
                config={
                    'display_name': display_name,
                    'chunking_config': {
                        'white_space_config': {
                            'max_tokens_per_chunk': 300,
                            'max_overlap_tokens': 50
                        }
                    }
                }
            )

            # Wait for operation to complete
            while not operation.done:
                time.sleep(2)
                operation = self.client.operations.get(operation)

            print(" ✓")
            return True

        except Exception as e:
            import traceback
            print(f" ✗ Error: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            return False

    def upload_directory(
        self,
        directory: str,
        extensions: List[str] = ['.md', '.txt', '.rs'],
        metadata_fn = None
    ) -> dict:
        """
        Upload all files in directory matching extensions

        Args:
            directory: Directory path to scan
            extensions: File extensions to include
            metadata_fn: Optional function(filepath) -> dict to generate metadata per file

        Returns:
            Dict with upload statistics
        """
        directory = Path(directory)
        files = []

        # Collect all matching files
        for ext in extensions:
            files.extend(directory.rglob(f'*{ext}'))

        stats = {'total': len(files), 'success': 0, 'failed': 0}

        print(f"\nUploading {stats['total']} files from {directory}")

        for file_path in files:
            # Generate metadata if function provided
            metadata = metadata_fn(str(file_path)) if metadata_fn else None

            # Upload file
            if self.upload_file(str(file_path), metadata=metadata):
                stats['success'] += 1
            else:
                stats['failed'] += 1

        print(f"\n✓ Upload complete: {stats['success']} succeeded, {stats['failed']} failed")
        return stats

    def query(
        self,
        question: str,
        model: str = "gemini-2.0-flash-exp",
        metadata_filter: Optional[str] = None
    ) -> dict:
        """
        Query the file search store

        Args:
            question: Natural language query
            model: Gemini model to use
            metadata_filter: Optional filter string (e.g., "category=patterns")

        Returns:
            Dict with 'answer', 'citations', and 'grounding_metadata'
        """
        if not self.store_name:
            raise ValueError("Store not initialized. Call get_or_create_store() first")

        print(f"\nQuerying: {question}")

        # Build file search tool config
        file_search_tool = types.Tool(
            file_search=types.FileSearch(
                file_search_store_names=[self.store_name]
            )
        )

        # Generate response with file search
        response = self.client.models.generate_content(
            model=model,
            contents=question,
            config=types.GenerateContentConfig(
                tools=[file_search_tool]
            )
        )

        # Extract answer and citations
        answer = response.text
        grounding_metadata = response.candidates[0].grounding_metadata if response.candidates else None

        result = {
            'answer': answer,
            'grounding_metadata': grounding_metadata,
            'citations': []
        }

        # Parse citations if available
        if grounding_metadata and hasattr(grounding_metadata, 'grounding_chunks'):
            for chunk in grounding_metadata.grounding_chunks:
                if hasattr(chunk, 'web'):
                    result['citations'].append({
                        'source': chunk.web.uri if hasattr(chunk.web, 'uri') else 'Unknown',
                        'title': chunk.web.title if hasattr(chunk.web, 'title') else 'Unknown'
                    })

        return result

    def delete_store(self, force: bool = True):
        """Delete the current file search store"""
        if not self.store_name:
            print("No store to delete")
            return

        print(f"Deleting store: {self.store_name}")
        self.client.file_search_stores.delete(
            name=self.store_name,
            config={'force': force}
        )
        print("✓ Store deleted")
        self.store_name = None

    def list_stores(self):
        """List all file search stores"""
        print("\nFile Search Stores:")
        for store in self.client.file_search_stores.list():
            print(f"  - {store.display_name} ({store.name})")


def generate_file_metadata(file_path: str) -> dict:
    """
    Generate metadata for a file based on its path

    Args:
        file_path: Path to the file

    Returns:
        Metadata dictionary
    """
    path = Path(file_path)
    metadata = {}

    # Determine category based on directory
    if 'patterns' in path.parts:
        metadata['category'] = 'pattern'
    elif 'notes' in path.parts:
        metadata['category'] = 'notes'
    elif 'writeups' in path.parts:
        metadata['category'] = 'writeup'
    elif 'implementations' in path.parts:
        metadata['category'] = 'implementation'
    elif 'docs' in path.parts:
        metadata['category'] = 'documentation'

    # Add file type
    if path.suffix == '.rs':
        metadata['filetype'] = 'rust'
    elif path.suffix == '.md':
        metadata['filetype'] = 'markdown'
    elif path.suffix == '.txt':
        metadata['filetype'] = 'text'

    return metadata


def main():
    """CLI interface for Gemini File Search"""
    import argparse

    parser = argparse.ArgumentParser(description='Gemini File Search for DSA Mastery')
    parser.add_argument('action', choices=['setup', 'upload', 'query', 'delete', 'list'],
                        help='Action to perform')
    parser.add_argument('--dir', default='.', help='Directory to upload (for upload action)')
    parser.add_argument('--question', '-q', help='Question to ask (for query action)')
    parser.add_argument('--filter', help='Metadata filter (e.g., category=patterns)')
    parser.add_argument('--model', default='gemini-2.0-flash-exp', help='Model to use')

    args = parser.parse_args()

    # Initialize client
    try:
        fs = GeminiFileSearch()
    except ValueError as e:
        print(f"Error: {e}")
        print("\nSet your API key:")
        print("  export GEMINI_API_KEY='your-api-key-here'")
        sys.exit(1)

    # Execute action
    if args.action == 'setup':
        fs.get_or_create_store()
        print("\n✓ Setup complete. Run 'upload' to index your files.")

    elif args.action == 'upload':
        fs.get_or_create_store()
        fs.upload_directory(args.dir, metadata_fn=generate_file_metadata)

    elif args.action == 'query':
        if not args.question:
            print("Error: --question required for query action")
            sys.exit(1)
        fs.get_or_create_store()
        result = fs.query(args.question, model=args.model, metadata_filter=args.filter)
        print(f"\n{result['answer']}")
        if result['citations']:
            print("\nSources:")
            for citation in result['citations']:
                print(f"  - {citation['title']}: {citation['source']}")

    elif args.action == 'delete':
        fs.get_or_create_store()
        fs.delete_store()

    elif args.action == 'list':
        fs.list_stores()


if __name__ == '__main__':
    main()
