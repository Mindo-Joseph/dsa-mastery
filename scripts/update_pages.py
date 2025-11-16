#!/usr/bin/env python3

"""
Auto-update GitHub Pages with live progress data
Generates progress.json and updates documentation
"""

import json
import os
from datetime import datetime
from pathlib import Path

def count_problems_solved():
    """Count solved problems from git commits"""
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'log', '--oneline', '--grep', 'Solve:'],
            capture_output=True,
            text=True
        )
        return len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
    except:
        return 0

def count_writeups():
    """Count writeups in docs/patterns/"""
    docs_dir = Path(__file__).parent.parent / 'docs' / 'patterns'
    if docs_dir.exists():
        return len(list(docs_dir.glob('*.md'))) - 1  # Exclude TEMPLATE.md
    return 0

def calculate_streak():
    """Calculate current solving streak"""
    # TODO: Implement based on progress tracking
    return 0

def calculate_days_elapsed():
    """Calculate days since project start"""
    # Check for first commit or use current day
    import subprocess
    try:
        result = subprocess.run(
            ['git', 'log', '--reverse', '--format=%ct', '--max-count=1'],
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            first_commit_time = int(result.stdout.strip())
            from datetime import datetime
            first_date = datetime.fromtimestamp(first_commit_time)
            days = (datetime.now() - first_date).days
            return max(1, days)
    except:
        pass
    return 1

def generate_progress_data():
    """Generate progress.json for GitHub Pages"""

    progress = {
        'generated_at': datetime.now().isoformat(),
        'days': calculate_days_elapsed(),
        'problems_solved': count_problems_solved(),
        'streak': calculate_streak(),
        'writeups': count_writeups(),
        'current_pattern': 'Two Pointers',
        'current_pattern_progress': 0,
        'total_patterns': 15,
        'patterns_completed': 0,
        'infrastructure': {
            'skills': 4,
            'agents': 3,
            'hooks': 5,
            'tools': 1
        },
        'stats': {
            'avg_time_per_problem': 60,  # minutes
            'target_problems': 70,
            'target_weeks': 12
        }
    }

    return progress

def update_docs_data():
    """Update docs/data/progress.json"""

    docs_data_dir = Path(__file__).parent.parent / 'docs' / 'data'
    docs_data_dir.mkdir(parents=True, exist_ok=True)

    progress = generate_progress_data()

    output_file = docs_data_dir / 'progress.json'
    with open(output_file, 'w') as f:
        json.dump(progress, f, indent=2)

    print(f"✅ Updated {output_file}")
    print(f"📊 Stats: {progress['problems_solved']} problems, {progress['writeups']} writeups, Day {progress['days']}")

def main():
    os.chdir(Path(__file__).parent.parent)
    update_docs_data()

if __name__ == '__main__':
    main()
