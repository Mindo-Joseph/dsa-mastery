#!/bin/bash
# Morning automation - runs at 4:30 AM Kenyan time

REPO_DIR="$HOME/dsa-mastery"
cd "$REPO_DIR"

# Load environment
source "$HOME/.venv/bin/activate"
export GEMINI_API_KEY='AIzaSyAYYc7FtOnneziaD7xHtvMIigO8FrUzswI'

# Log file
LOG_FILE="$REPO_DIR/logs/morning_$(date +%Y%m%d).log"
mkdir -p "$REPO_DIR/logs"

{
    echo "=========================================="
    echo "🌅 Morning Automation - $(date)"
    echo "=========================================="

    # Generate daily content
    echo ""
    echo "📚 Generating today's content..."
    python3 scripts/daily_automation.py

    # Get current pattern
    PATTERN=$(python3 -c "import json; d=json.load(open('progress/daily_progress.json')); print('Two Pointers')")

    # Create GitHub issues for problems
    echo ""
    echo "📋 Creating GitHub issues..."
    python3 scripts/create_problem_issues.py "$PATTERN"

    # Publish to GitHub Pages
    echo ""
    echo "📤 Publishing to GitHub Pages..."
    python3 scripts/publish_to_pages.py

    # Commit and push
    echo ""
    echo "💾 Committing changes..."
    git add .
    git commit -m "🤖 Daily automation: $(date +%Y-%m-%d)" || true
    git push origin master

    echo ""
    echo "✅ Morning automation complete!"
    echo "🎯 Check your GitHub issues for today's problems"
    echo ""

} >> "$LOG_FILE" 2>&1

# Send notification (optional - requires notify-send)
if command -v notify-send &> /dev/null; then
    notify-send "DSA Mastery" "Morning automation complete! Check GitHub issues for today's problems."
fi
