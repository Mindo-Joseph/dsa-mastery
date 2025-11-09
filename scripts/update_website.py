#!/usr/bin/env python3
"""
Auto-update GitHub Pages with latest progress

Reads progress from git history and updates docs/index.md
Run after each solved problem to keep public site current
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path


def get_git_stats():
    """Extract stats from git commits"""
    try:
        # Count solved problems
        result = subprocess.run(
            ['git', 'log', '--oneline', '--grep=Solve:'],
            capture_output=True,
            text=True,
            cwd=Path.home() / 'dsa-mastery'
        )
        solved_problems = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0

        # Get current streak
        result = subprocess.run(
            ['git', 'log', '--since=30 days ago', '--format=%cd', '--date=short'],
            capture_output=True,
            text=True,
            cwd=Path.home() / 'dsa-mastery'
        )

        dates = set(result.stdout.strip().split('\n')) if result.stdout.strip() else set()
        streak = len(dates)

        return {
            'solved': solved_problems,
            'streak': streak
        }
    except:
        return {'solved': 0, 'streak': 0}


def load_progress():
    """Load progress from tracking file"""
    progress_file = Path.home() / 'dsa-mastery' / 'progress' / 'history.json'

    if progress_file.exists():
        with open(progress_file) as f:
            return json.load(f)
    return {"problems": [], "patterns": {}}


def update_index_page():
    """Update docs/index.md with latest stats"""

    git_stats = get_git_stats()
    progress = load_progress()

    # Calculate stats
    total_problems = len(progress.get('problems', []))
    patterns = progress.get('patterns', {})

    easy = sum(p.get('easy', 0) for p in patterns.values())
    medium = sum(p.get('medium', 0) for p in patterns.values())
    hard = sum(p.get('hard', 0) for p in patterns.values())

    successes = sum(1 for p in progress.get('problems', []) if p.get('status') == 'success')
    success_rate = (successes / total_problems * 100) if total_problems > 0 else 0

    avg_time = 0
    if progress.get('problems'):
        avg_time = sum(p.get('time_minutes', 0) for p in progress['problems']) / len(progress['problems'])

    # Current pattern
    current_pattern = "Two Pointers"
    if progress.get('problems'):
        current_pattern = progress['problems'][-1].get('pattern', 'Two Pointers')

    # Recent solutions
    recent = progress.get('problems', [])[-5:]
    recent.reverse()

    # Build recent solutions HTML
    recent_html = ""
    if recent:
        for p in recent:
            emoji = "🟢" if p['status'] == 'success' else "🟡" if p['status'] == 'partial' else "🔴"
            recent_html += f"- {emoji} **{p['problem']}** ({p['pattern']}) - {p['difficulty']} - {p['time_minutes']}min\n"
    else:
        recent_html = "*No solutions yet. Start solving!*"

    # Update index.md
    index_template = f"""# DSA Mastery Journey

**Goal**: Google Senior Engineer (L5+)
**Timeline**: 12 weeks
**Standard**: Every solution meets senior interview bar

---

## 🎯 My Progress

**Current Pattern**: {current_pattern}
**Problems Solved**: {total_problems} / 60+
**Days Active**: {git_stats['streak']}
**Current Streak**: {git_stats['streak']} 🔥

---

## 📚 Pattern Writeups

### Foundation Patterns (Weeks 1-2)
- [Two Pointers](patterns/01-two-pointers.html) - *In Progress*
- [Sliding Window](patterns/02-sliding-window.html) - *Locked*
- [Binary Search](patterns/03-binary-search.html) - *Locked*

### Data Structure Patterns (Weeks 3-4)
- [Fast & Slow Pointers](patterns/04-fast-slow-pointers.html) - *Locked*
- [Linked List In-Place Reversal](patterns/05-linked-list-reversal.html) - *Locked*
- [Tree BFS](patterns/06-tree-bfs.html) - *Locked*
- [Tree DFS](patterns/07-tree-dfs.html) - *Locked*

### Advanced Patterns (Weeks 5-6)
- [Graphs](patterns/08-graphs.html) - *Locked*
- [Heaps & Priority Queues](patterns/09-heaps.html) - *Locked*

### Problem-Solving Paradigms (Weeks 7-10)
- [Dynamic Programming](patterns/10-dynamic-programming.html) - *Locked*
- [Backtracking](patterns/11-backtracking.html) - *Locked*
- [Advanced Techniques](patterns/12-advanced.html) - *Locked*

---

## 🚀 Recent Solutions

{recent_html}

---

## 📊 Statistics

- **Total Problems**: {total_problems}
- **Easy**: {easy}
- **Medium**: {medium}
- **Hard**: {hard}
- **Success Rate**: {success_rate:.1f}%
- **Average Time**: {avg_time:.1f} min

---

## 🎓 Learning Philosophy

This is my public commitment to mastering data structures and algorithms from **first principles**, not just pattern memorization. Every solution here is:

- ✅ Optimal time/space complexity
- ✅ Clean, idiomatic Rust
- ✅ Comprehensively tested
- ✅ Clearly explained
- ✅ Reviewed to Google L5+ standards

---

## 🔗 Links

- [GitHub Repository](https://github.com/yourusername/dsa-mastery)
- [Progress Tracker](progress.html)

---

*Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

---

**"Excellence is not a destination; it is a continuous journey that never ends."** - Brian Tracy
"""

    # Write to file
    index_file = Path.home() / 'dsa-mastery' / 'docs' / 'index.md'
    index_file.parent.mkdir(parents=True, exist_ok=True)

    with open(index_file, 'w') as f:
        f.write(index_template)

    print(f"✓ Updated docs/index.md")
    print(f"  Problems: {total_problems}")
    print(f"  Streak: {git_stats['streak']} days")
    print(f"  Success Rate: {success_rate:.1f}%")
    print(f"\nPush to GitHub to update your public site:")
    print(f"  git add docs/index.md")
    print(f"  git commit -m 'Update progress: {total_problems} problems solved'")
    print(f"  git push")


if __name__ == "__main__":
    update_index_page()
