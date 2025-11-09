#!/bin/bash
# Quick script to update tomorrow's calendar based on today's progress

cd ~/dsa-mastery

echo "📊 Updating tomorrow's calendar based on your progress..."
python3 scripts/calendar/adaptive_scheduler.py

echo ""
echo "💡 TIP: Run this script after each problem to keep calendar adaptive"
echo "Or add to git pre-commit hook for automatic updates"
