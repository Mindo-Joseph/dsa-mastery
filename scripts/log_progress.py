#!/usr/bin/env python3
"""
Progress Logging System

Tracks:
- Problems solved per pattern
- Time taken
- Success rate
- Review schedule (spaced repetition)
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

PROGRESS_FILE = "progress/history.json"
STATS_FILE = "progress/stats.json"

def load_progress():
    """Load existing progress data"""
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {"problems": [], "patterns": {}}

def save_progress(data):
    """Save progress data"""
    os.makedirs("progress", exist_ok=True)
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_problem(pattern, problem_name, difficulty, time_minutes, status, notes=""):
    """Log a completed problem"""
    progress = load_progress()

    entry = {
        "date": datetime.now().isoformat(),
        "pattern": pattern,
        "problem": problem_name,
        "difficulty": difficulty,
        "time_minutes": int(time_minutes),
        "status": status,  # "success", "partial", "failed"
        "notes": notes,
        "next_review": calculate_next_review(status)
    }

    progress["problems"].append(entry)

    # Update pattern stats
    if pattern not in progress["patterns"]:
        progress["patterns"][pattern] = {
            "total": 0,
            "easy": 0,
            "medium": 0,
            "hard": 0,
            "success_rate": 0
        }

    progress["patterns"][pattern]["total"] += 1
    progress["patterns"][pattern][difficulty] += 1

    save_progress(progress)
    print(f"✓ Logged: {problem_name} ({pattern}) - {status}")
    print(f"  Next review: {entry['next_review']}")

    return entry

def calculate_next_review(status):
    """Calculate next review date using spaced repetition"""
    if status == "success":
        days = 7  # Review in 1 week
    elif status == "partial":
        days = 3  # Review in 3 days
    else:  # failed
        days = 1  # Review tomorrow

    next_date = datetime.now() + timedelta(days=days)
    return next_date.strftime("%Y-%m-%d")

def get_due_reviews():
    """Get problems due for review"""
    progress = load_progress()
    today = datetime.now().strftime("%Y-%m-%d")

    due = [p for p in progress["problems"] if p.get("next_review", "") <= today]
    return due

def generate_stats():
    """Generate statistics"""
    progress = load_progress()

    stats = {
        "total_problems": len(progress["problems"]),
        "patterns_mastered": len([p for p, data in progress["patterns"].items() if data["total"] >= 5]),
        "current_streak": calculate_streak(progress),
        "average_time": calculate_avg_time(progress),
        "success_rate": calculate_success_rate(progress),
        "pattern_breakdown": progress["patterns"]
    }

    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

    return stats

def calculate_streak(progress):
    """Calculate current daily streak"""
    if not progress["problems"]:
        return 0

    problems = sorted(progress["problems"], key=lambda x: x["date"], reverse=True)
    streak = 0
    current_date = datetime.now().date()

    for problem in problems:
        problem_date = datetime.fromisoformat(problem["date"]).date()
        if problem_date == current_date or problem_date == current_date - timedelta(days=streak):
            streak += 1
        else:
            break

    return streak

def calculate_avg_time(progress):
    """Calculate average time per problem"""
    if not progress["problems"]:
        return 0

    total_time = sum(p["time_minutes"] for p in progress["problems"])
    return total_time / len(progress["problems"])

def calculate_success_rate(progress):
    """Calculate overall success rate"""
    if not progress["problems"]:
        return 0

    successes = sum(1 for p in progress["problems"] if p["status"] == "success")
    return (successes / len(progress["problems"])) * 100

def show_dashboard():
    """Display progress dashboard"""
    stats = generate_stats()

    print("\n" + "="*50)
    print("DSA MASTERY DASHBOARD")
    print("="*50)
    print(f"Total Problems Solved: {stats['total_problems']}")
    print(f"Patterns Mastered: {stats['patterns_mastered']}/12")
    print(f"Current Streak: {stats['current_streak']} days")
    print(f"Average Time: {stats['average_time']:.1f} minutes")
    print(f"Success Rate: {stats['success_rate']:.1f}%")
    print("\nPattern Breakdown:")

    for pattern, data in stats['pattern_breakdown'].items():
        print(f"  {pattern}: {data['total']} problems (E:{data['easy']} M:{data['medium']} H:{data['hard']})")

    print("\nProblems Due for Review:")
    due = get_due_reviews()
    if due:
        for problem in due[:5]:  # Show next 5
            print(f"  - {problem['problem']} ({problem['pattern']})")
    else:
        print("  None! Great job staying on top of reviews!")

    print("="*50 + "\n")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        show_dashboard()
    elif sys.argv[1] == "log":
        if len(sys.argv) < 6:
            print("Usage: python log_progress.py log <pattern> <problem> <difficulty> <time_minutes> <status> [notes]")
            sys.exit(1)

        pattern = sys.argv[2]
        problem = sys.argv[3]
        difficulty = sys.argv[4]
        time_minutes = sys.argv[5]
        status = sys.argv[6]
        notes = sys.argv[7] if len(sys.argv) > 7 else ""

        log_problem(pattern, problem, difficulty, time_minutes, status, notes)
        show_dashboard()

    elif sys.argv[1] == "reviews":
        due = get_due_reviews()
        print(f"\n{len(due)} problems due for review:")
        for p in due:
            print(f"  - {p['problem']} ({p['pattern']}) - Last: {p['date']}")

    elif sys.argv[1] == "stats":
        show_dashboard()
