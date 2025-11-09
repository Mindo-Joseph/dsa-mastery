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
# Step 2: Create GitHub issues for problems
echo ""
echo "📋 Step 2: Creating GitHub issues for today's problems..."

# Get current pattern
PATTERN=$(python3 -c "
import json
from pathlib import Path
if Path('progress/daily_progress.json').exists():
    with open('progress/daily_progress.json') as f:
        data = json.load(f)
    print('Two Pointers')  # Default for now
else:
    print('Two Pointers')
")

python3 scripts/create_problem_issues.py "$PATTERN" || echo "Issue creation skipped (may need gh auth)"

echo ""
echo "========================================"
echo "✅ DAILY SETUP COMPLETE"
echo "========================================"
echo ""
echo "📋 Your problems are now GitHub issues!"
echo ""
echo "View issues:"
echo "  gh issue list --label problem"
echo ""
echo "📖 Next steps:"
echo "1. Read writeup: https://mindo-joseph.github.io/dsa-mastery/patterns/two-pointers.html"
echo "2. Pick an issue: gh issue list --label problem"
echo "3. Solve problem in Rust"
echo "4. Submit: ./scripts/submit.sh <problem_file.rs>"
echo "   (This will automatically close the issue!)"
echo ""
