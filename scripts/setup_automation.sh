#!/bin/bash
# Setup automated daily workflows with cron
# - 4:30 AM: Generate daily content and create GitHub issues
# - 9:30 PM: Show progress and what to do tomorrow

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"

echo "=========================================="
echo "🤖 Setting Up Daily Automation"
echo "=========================================="
echo ""

# Check if gh CLI is installed
if ! command -v gh &> /dev/null; then
    echo "📦 Installing GitHub CLI..."
    sudo apt update
    sudo apt install -y gh

    echo ""
    echo "🔐 Please authenticate with GitHub:"
    gh auth login
fi

# Verify gh auth
if ! gh auth status &> /dev/null; then
    echo "❌ GitHub CLI not authenticated"
    echo "Run: gh auth login"
    exit 1
fi

echo "✅ GitHub CLI authenticated"
echo ""

# Get Kenyan timezone info
echo "🌍 Setting up for Kenyan time (EAT - UTC+3)"
echo ""

# Create wrapper scripts for cron
echo "📝 Creating cron wrapper scripts..."

# Morning script (4:30 AM)
cat > "$REPO_DIR/scripts/cron_morning.sh" << 'EOF'
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
EOF

# Evening script (9:30 PM)
cat > "$REPO_DIR/scripts/cron_evening.sh" << 'EOF'
#!/bin/bash
# Evening automation - runs at 9:30 PM Kenyan time

REPO_DIR="$HOME/dsa-mastery"
cd "$REPO_DIR"

# Log file
LOG_FILE="$REPO_DIR/logs/evening_$(date +%Y%m%d).log"
mkdir -p "$REPO_DIR/logs"

{
    echo "=========================================="
    echo "🌙 Evening Summary - $(date)"
    echo "=========================================="

    # Show progress
    echo ""
    scripts/next.sh

    # Count problems solved today
    TODAY=$(date +%Y-%m-%d)
    SOLVED_TODAY=$(git log --since="$TODAY 00:00" --until="$TODAY 23:59" --oneline --grep="Solve:" | wc -l)

    echo ""
    echo "📊 Today's Summary:"
    echo "   Problems solved: $SOLVED_TODAY"
    echo "   Target: 2-3 problems/day"
    echo ""

    if [ "$SOLVED_TODAY" -ge 2 ]; then
        echo "🎉 Great work today!"
    elif [ "$SOLVED_TODAY" -eq 1 ]; then
        echo "💪 Good progress! Try for one more tomorrow."
    else
        echo "📚 Don't worry - tomorrow is a new day!"
    fi

    echo ""
    echo "🛌 Rest well. See you at 4:30 AM for tomorrow's content!"
    echo ""

} >> "$LOG_FILE" 2>&1

# Show the output in terminal if running interactively
if [ -t 1 ]; then
    cat "$LOG_FILE"
fi

# Send notification
if command -v notify-send &> /dev/null; then
    if [ "$SOLVED_TODAY" -ge 2 ]; then
        notify-send "DSA Mastery 🎉" "Great work today! $SOLVED_TODAY problems solved."
    else
        notify-send "DSA Mastery" "Daily summary ready. Keep going!"
    fi
fi
EOF

chmod +x "$REPO_DIR/scripts/cron_morning.sh"
chmod +x "$REPO_DIR/scripts/cron_evening.sh"
chmod +x "$REPO_DIR/scripts/create_problem_issues.py"

echo "✅ Created cron wrapper scripts"
echo ""

# Setup cron jobs
echo "⏰ Setting up cron jobs..."
echo ""

# Kenyan time (EAT) is UTC+3
# 4:30 AM EAT = 1:30 AM UTC
# 9:30 PM EAT = 6:30 PM UTC

# Remove existing cron jobs for DSA mastery
crontab -l 2>/dev/null | grep -v "dsa-mastery" > /tmp/crontab_new || true

# Add new cron jobs
cat >> /tmp/crontab_new << EOF

# DSA Mastery - Daily Automation
# Morning: 4:30 AM Kenyan time (1:30 AM UTC)
30 1 * * * $REPO_DIR/scripts/cron_morning.sh

# Evening: 9:30 PM Kenyan time (6:30 PM UTC)
30 18 * * * $REPO_DIR/scripts/cron_evening.sh
EOF

# Install new crontab
crontab /tmp/crontab_new
rm /tmp/crontab_new

echo "✅ Cron jobs installed"
echo ""

# Show installed cron jobs
echo "📋 Installed cron jobs:"
crontab -l | grep -A2 "DSA Mastery"
echo ""

echo "=========================================="
echo "✅ AUTOMATION SETUP COMPLETE!"
echo "=========================================="
echo ""
echo "🌅 Morning (4:30 AM Kenyan time):"
echo "   - Generate writeup from your PDFs"
echo "   - Create GitHub issues for problems"
echo "   - Publish to GitHub Pages"
echo "   - Commit and push"
echo ""
echo "🌙 Evening (9:30 PM Kenyan time):"
echo "   - Show your progress"
echo "   - Daily summary"
echo "   - Motivation for tomorrow"
echo ""
echo "📋 Your workflow:"
echo "   1. Morning: Check GitHub issues (gh issue list)"
echo "   2. Day: Solve problems, submit with ./scripts/submit.sh"
echo "   3. Evening: Review progress with ./scripts/next.sh"
echo ""
echo "🧪 Test the automation now:"
echo "   ./scripts/cron_morning.sh   # Test morning run"
echo "   ./scripts/cron_evening.sh   # Test evening run"
echo ""
echo "📊 Check logs:"
echo "   tail -f logs/morning_*.log"
echo "   tail -f logs/evening_*.log"
echo ""
echo "🎯 View your issues:"
echo "   gh issue list --label problem"
echo ""
echo "🚀 System ready! Your learning is now fully automated."
echo ""
