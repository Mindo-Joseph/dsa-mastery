#!/bin/bash
# Daily DSA Learning - Fully Automated
# Usage: ./scripts/daily.sh

set -e

cd "$(dirname "$0")/.."

echo "========================================"
echo "🚀 DAILY DSA MASTERY - AUTOMATED"
echo "========================================"
echo ""

# Step 1: Generate today's lesson
echo "📚 Step 1: Generating today's lesson from your sources..."
python3 scripts/daily_automation.py

echo ""
echo "========================================"
echo "✅ DAILY SETUP COMPLETE"
echo "========================================"
echo ""
echo "📖 Next steps:"
echo "1. Read writeup in Google Docs (link in GOOGLE_DOCS_LINKS.md)"
echo "2. Add your personal insights and notes"
echo "3. Check daily-problems/ for problems to solve"
echo "4. Solve problems in Rust"
echo "5. Run: ./scripts/submit.sh <problem_file.rs>"
echo ""
