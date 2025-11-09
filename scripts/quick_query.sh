#!/bin/bash
# Quick query interface for Gemini File Search

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ -z "$GEMINI_API_KEY" ]; then
    echo "Error: GEMINI_API_KEY not set"
    exit 1
fi

if [ -z "$1" ]; then
    echo "Usage: $0 \"your question here\""
    echo ""
    echo "Examples:"
    echo "  $0 \"Explain the two pointers pattern\""
    echo "  $0 \"What are common tree traversal techniques?\""
    echo "  $0 \"Show me examples of sliding window\""
    exit 1
fi

python3 "$SCRIPT_DIR/gemini_file_search.py" query --question "$1"
