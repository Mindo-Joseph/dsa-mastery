#!/usr/bin/env python3
"""
Daily DSA Learning Automation
Fully automated AI-driven learning system
"""

import os
import json
from datetime import datetime
from pathlib import Path
from gemini_rag import GeminiRAG


# 12-week curriculum with daily topics
CURRICULUM = [
    # Week 1-2: Foundation Patterns
    {"week": 1, "pattern": "Two Pointers", "days": 3, "problems": 7},
    {"week": 1, "pattern": "Sliding Window", "days": 3, "problems": 7},
    {"week": 2, "pattern": "Binary Search", "days": 2, "problems": 6},
    {"week": 2, "pattern": "Fast & Slow Pointers", "days": 2, "problems": 5},

    # Week 3-4: Data Structures
    {"week": 3, "pattern": "Linked List Reversal", "days": 2, "problems": 5},
    {"week": 3, "pattern": "Tree BFS", "days": 2, "problems": 6},
    {"week": 4, "pattern": "Tree DFS", "days": 2, "problems": 6},
    {"week": 4, "pattern": "Heaps", "days": 2, "problems": 6},

    # Week 5-6: Advanced Structures
    {"week": 5, "pattern": "Graph BFS/DFS", "days": 3, "problems": 7},
    {"week": 6, "pattern": "Topological Sort", "days": 2, "problems": 5},
    {"week": 6, "pattern": "Union Find", "days": 2, "problems": 5},

    # Week 7-10: Paradigms (Most Important!)
    {"week": 7, "pattern": "Dynamic Programming - 1D", "days": 4, "problems": 8},
    {"week": 8, "pattern": "Dynamic Programming - 2D", "days": 4, "problems": 8},
    {"week": 9, "pattern": "Dynamic Programming - Advanced", "days": 3, "problems": 7},
    {"week": 9, "pattern": "Backtracking", "days": 2, "problems": 6},
    {"week": 10, "pattern": "Greedy Algorithms", "days": 3, "problems": 7},

    # Week 11-12: Integration
    {"week": 11, "pattern": "Mixed Patterns", "days": 4, "problems": 10},
    {"week": 12, "pattern": "Mock Interviews", "days": 4, "problems": 10},
]


class DailyAutomation:
    """Automated daily DSA learning system"""

    def __init__(self):
        self.rag = GeminiRAG()
        self.progress_file = Path("progress/daily_progress.json")
        self.progress = self._load_progress()

    def _load_progress(self):
        """Load learning progress"""
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                return json.load(f)
        return {"day": 0, "patterns_completed": []}

    def _save_progress(self):
        """Save learning progress"""
        self.progress_file.parent.mkdir(exist_ok=True)
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f, indent=2)

    def get_todays_pattern(self):
        """Get today's pattern based on curriculum"""
        day = self.progress["day"]

        # Calculate which pattern we're on
        total_days = 0
        for item in CURRICULUM:
            if total_days + item["days"] > day:
                return item
            total_days += item["days"]

        # Curriculum complete
        return None

    def generate_writeup(self, pattern_name: str):
        """
        Query all sources and generate comprehensive writeup
        Returns: Complete markdown writeup
        """
        print(f"\n{'='*60}")
        print(f"🤖 AI GENERATING WRITEUP: {pattern_name}")
        print(f"{'='*60}\n")

        writeup_sections = {}

        # Query 1: First Principles & Theory
        print("📚 Querying your sources for first principles...")
        theory = self.rag.query(
            f"""Explain the {pattern_name} pattern in detail:
            1. First principles: WHY does this pattern exist? What problem does it solve?
            2. The key insight that makes it work
            3. Time and space complexity analysis with proof
            4. When to recognize this pattern (pattern recognition guide)
            5. Common variations of the pattern

            Use examples from algorithm textbooks. Be thorough and senior-level."""
        )
        writeup_sections['theory'] = theory

        # Query 2: Implementation & Code Patterns
        print("💻 Querying for implementation patterns...")
        implementation = self.rag.query(
            f"""For the {pattern_name} pattern:
            1. Show the canonical implementation template
            2. Common mistakes and how to avoid them
            3. Edge cases to handle
            4. Language-specific considerations (especially for Rust if available)
            5. Best practices for clean code

            Include code examples if available."""
        )
        writeup_sections['implementation'] = implementation

        # Query 3: Example Problems
        print("📝 Fetching example problems...")
        examples = self.rag.query(
            f"""List 5-7 problems that use {pattern_name}:
            - 2 easy (for pattern recognition)
            - 3 medium (core understanding)
            - 2 hard (mastery)

            For each, briefly explain why it uses this pattern."""
        )
        writeup_sections['examples'] = examples

        # Query 4: Interview Tips & Trade-offs
        print("🎯 Gathering interview insights...")
        interview = self.rag.query(
            f"""For {pattern_name} in technical interviews:
            1. How to communicate this approach clearly
            2. Trade-offs compared to alternative approaches
            3. Follow-up questions interviewers might ask
            4. Red flags that indicate this pattern
            5. Senior-level insights that impress interviewers"""
        )
        writeup_sections['interview'] = interview

        # Generate complete writeup
        writeup = self._format_writeup(pattern_name, writeup_sections)

        print(f"\n✅ Writeup generated ({len(writeup)} characters)")
        return writeup

    def _format_writeup(self, pattern_name: str, sections: dict) -> str:
        """Format sections into complete writeup"""
        return f"""# {pattern_name} - First Principles to Mastery

*AI-Generated from your sources on {datetime.now().strftime('%Y-%m-%d')}*
*Add your personal insights and edits in Google Docs*

---

## First Principles & Theory

{sections['theory']}

---

## Implementation Guide

{sections['implementation']}

---

## Example Problems

{sections['examples']}

---

## Interview Strategy

{sections['interview']}

---

## Your Personal Insights

*Add your notes here as you learn:*
- What clicked for you?
- What was confusing at first?
- Aha moments?
- Mistakes you made?

---

## Practice Log

*Track your problem-solving:*

| # | Problem | Difficulty | Time | Pass? | Notes |
|---|---------|------------|------|-------|-------|
| 1 |         |            |      |       |       |
| 2 |         |            |      |       |       |
| 3 |         |            |      |       |       |

---

*Generated by DSA Mastery AI System*
*Sources: Your uploaded algorithm books and problem sets*
"""

    def fetch_problems_for_pattern(self, pattern_name: str, count: int = 7):
        """
        Fetch specific problems from LeetCode PDF for this pattern
        """
        print(f"🔍 Fetching {count} problems for {pattern_name}...")

        result = self.rag.query(
            f"""From the LeetCode problems, find {count} problems for {pattern_name}:

            Format for EACH problem:
            - Problem Number
            - Problem Title
            - Difficulty (Easy/Medium/Hard)
            - Brief description (1-2 sentences)

            Try to include:
            - 2 Easy
            - 3-4 Medium
            - 1-2 Hard

            List them clearly with problem numbers."""
        )

        return result

    def run_daily_automation(self):
        """Main daily automation flow"""
        pattern_info = self.get_todays_pattern()

        if not pattern_info:
            print("🎉 Curriculum complete! You're interview ready!")
            return

        pattern_name = pattern_info["pattern"]
        day_in_pattern = self.progress["day"] % pattern_info["days"] + 1

        print(f"\n{'='*60}")
        print(f"📅 DAY {self.progress['day'] + 1} - Week {pattern_info['week']}")
        print(f"🎯 PATTERN: {pattern_name} (Day {day_in_pattern}/{pattern_info['days']})")
        print(f"{'='*60}\n")

        if day_in_pattern == 1:
            # First day of pattern: Generate writeup
            print("📖 First day of pattern - generating comprehensive writeup...\n")

            writeup = self.generate_writeup(pattern_name)

            # Save writeup
            writeup_file = Path(f"writeups/{pattern_name.lower().replace(' ', '_')}.md")
            writeup_file.parent.mkdir(exist_ok=True)
            with open(writeup_file, 'w') as f:
                f.write(writeup)

            print(f"\n✅ Writeup saved: {writeup_file}")
            print(f"\n📤 Next: Push to Google Docs")
            print(f"   Run: python3 scripts/gdocs_sync/setup_initial_docs.py")
            print(f"\n👉 Then read & edit in Google Docs, add your insights!")

        # Fetch problems for solving
        print(f"\n📋 Fetching problems to solve today...")
        problems = self.fetch_problems_for_pattern(pattern_name, pattern_info["problems"])

        if problems:
            # Save problem list
            problems_file = Path(f"daily-problems/{pattern_name.lower().replace(' ', '_')}_problems.md")
            problems_file.parent.mkdir(exist_ok=True)
            with open(problems_file, 'w') as f:
                f.write(f"# Problems for {pattern_name}\n\n")
                f.write(problems)
                f.write(f"\n\n*Fetched: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")

            print(f"✅ Problems saved: {problems_file}")
        else:
            print("⚠️  Could not fetch problems")

        # Update progress
        self.progress["day"] += 1
        self._save_progress()

        print(f"\n{'='*60}")
        print(f"✅ DAILY SETUP COMPLETE")
        print(f"{'='*60}\n")
        print(f"📚 Next steps:")
        print(f"1. Read writeup in Google Docs (add your insights)")
        print(f"2. Check problems list: {problems_file}")
        print(f"3. Solve problems in Rust")
        print(f"4. Create PR for review")
        print(f"\n💪 Let's go!\n")


def main():
    automation = DailyAutomation()
    automation.run_daily_automation()


if __name__ == '__main__':
    main()
