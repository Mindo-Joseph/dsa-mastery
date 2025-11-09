#!/bin/bash
# Setup script for Gemini File Search integration

set -e

echo "========================================="
echo "Gemini File Search Setup for DSA Mastery"
echo "========================================="
echo ""

# Check if API key is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "Error: GEMINI_API_KEY environment variable not set"
    echo ""
    echo "Get your API key from: https://aistudio.google.com/apikey"
    echo ""
    echo "Then set it:"
    echo "  export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    echo "Add to ~/.bashrc for persistence:"
    echo "  echo 'export GEMINI_API_KEY=\"your-api-key-here\"' >> ~/.bashrc"
    exit 1
fi

# Check Python dependencies
echo "Checking Python dependencies..."
if ! python3 -c "import google.genai" 2>/dev/null; then
    echo "Installing google-genai package..."
    pip3 install --user google-genai
fi

echo "✓ Dependencies installed"
echo ""

# Create the file search store
echo "Creating file search store..."
python3 scripts/gemini_file_search.py setup

echo ""
echo "========================================="
echo "✓ Setup Complete!"
echo "========================================="
echo ""
echo "Next steps:"
echo ""
echo "1. Upload your DSA content:"
echo "   python3 scripts/gemini_file_search.py upload --dir ."
echo ""
echo "2. Query your knowledge base:"
echo "   python3 scripts/gemini_file_search.py query --question \"Explain two pointers pattern\""
echo ""
echo "3. Filter by category:"
echo "   python3 scripts/gemini_file_search.py query --question \"Show me tree problems\" --filter \"category=patterns\""
echo ""
