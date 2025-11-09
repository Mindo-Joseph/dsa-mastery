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
