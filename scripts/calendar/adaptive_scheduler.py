#!/usr/bin/env python3
"""
Adaptive Calendar Scheduler

Updates tomorrow's calendar event based on:
- Today's completion status
- Learning velocity
- Pattern mastery level
- Success rate

Automatically adjusts:
- Next problem difficulty
- Pattern progression
- Review schedule
- Time allocation
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import subprocess


class AdaptiveScheduler:
    """Dynamic calendar that adapts to your learning pace"""

    def __init__(self):
        self.base_dir = Path.home() / 'dsa-mastery'
        self.progress_file = self.base_dir / 'progress' / 'history.json'
        self.config_file = self.base_dir / 'scripts' / 'calendar' / 'learning_config.json'
        self.load_progress()
        self.load_config()

    def load_progress(self):
        """Load learning progress data"""
        if self.progress_file.exists():
            with open(self.progress_file) as f:
                self.progress = json.load(f)
        else:
            self.progress = {"problems": [], "patterns": {}}

    def load_config(self):
        """Load learning configuration"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                self.config = json.load(f)
        else:
            # Default configuration
            self.config = {
                "current_pattern": "two_pointers",
                "target_problems_per_day": 2,
                "difficulty_progression": ["easy", "medium", "hard"],
                "mastery_threshold": 5,  # Problems to master pattern
                "adaptive_mode": True
            }
            self.save_config()

    def save_config(self):
        """Save configuration"""
        self.config_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def calculate_learning_velocity(self):
        """Calculate problems solved per day (last 7 days)"""
        if not self.progress.get('problems'):
            return 0

        week_ago = datetime.now() - timedelta(days=7)
        recent_problems = [
            p for p in self.progress['problems']
            if datetime.fromisoformat(p['date']) > week_ago
        ]

        return len(recent_problems) / 7 if recent_problems else 0

    def calculate_success_rate(self, pattern=None):
        """Calculate success rate for pattern (or overall)"""
        problems = self.progress.get('problems', [])

        if pattern:
            problems = [p for p in problems if p.get('pattern') == pattern]

        if not problems:
            return 0

        successes = sum(1 for p in problems if p.get('status') == 'success')
        return (successes / len(problems)) * 100

    def get_pattern_mastery(self, pattern):
        """Check if pattern is mastered"""
        pattern_data = self.progress.get('patterns', {}).get(pattern, {})
        total = pattern_data.get('total', 0)
        success_rate = self.calculate_success_rate(pattern)

        return {
            'problems_solved': total,
            'success_rate': success_rate,
            'is_mastered': total >= self.config['mastery_threshold'] and success_rate >= 80
        }

    def decide_next_task(self):
        """Decide what to do tomorrow based on today's progress"""

        current_pattern = self.config['current_pattern']
        mastery = self.get_pattern_mastery(current_pattern)
        velocity = self.calculate_learning_velocity()

        # Decision logic
        if mastery['is_mastered']:
            # Move to next pattern
            return self.advance_to_next_pattern()

        elif mastery['success_rate'] < 50:
            # Struggling - add review problems, slow down
            return {
                'action': 'review',
                'pattern': current_pattern,
                'difficulty': 'easy',
                'count': 1,
                'note': 'Reviewing fundamentals - success rate low'
            }

        elif velocity > 3:
            # Fast learner - increase difficulty or add problems
            return {
                'action': 'accelerate',
                'pattern': current_pattern,
                'difficulty': self.next_difficulty(current_pattern),
                'count': 3,
                'note': 'Strong performance - increasing challenge'
            }

        elif velocity < 1:
            # Slow progress - maintain current level
            return {
                'action': 'maintain',
                'pattern': current_pattern,
                'difficulty': self.current_difficulty(current_pattern),
                'count': 1,
                'note': 'Building consistency - keep steady pace'
            }

        else:
            # Normal progress
            return {
                'action': 'continue',
                'pattern': current_pattern,
                'difficulty': self.next_difficulty(current_pattern),
                'count': 2,
                'note': 'Solid progress - continuing pattern'
            }

    def advance_to_next_pattern(self):
        """Move to next pattern in curriculum"""
        patterns = [
            "two_pointers",
            "sliding_window",
            "binary_search",
            "fast_slow_pointers",
            "linked_list_reversal",
            "tree_bfs",
            "tree_dfs",
            "graphs",
            "heaps",
            "dynamic_programming",
            "backtracking",
            "advanced"
        ]

        current_idx = patterns.index(self.config['current_pattern'])
        next_pattern = patterns[current_idx + 1] if current_idx < len(patterns) - 1 else patterns[-1]

        self.config['current_pattern'] = next_pattern
        self.save_config()

        return {
            'action': 'new_pattern',
            'pattern': next_pattern,
            'difficulty': 'easy',
            'count': 2,
            'note': f'Mastered {self.config["current_pattern"]}! Starting {next_pattern}'
        }

    def current_difficulty(self, pattern):
        """Get current difficulty level for pattern"""
        pattern_problems = [
            p for p in self.progress.get('problems', [])
            if p.get('pattern') == pattern
        ]

        if not pattern_problems:
            return 'easy'

        # Return most common recent difficulty
        recent = pattern_problems[-3:]
        difficulties = [p.get('difficulty', 'easy') for p in recent]
        return max(set(difficulties), key=difficulties.count)

    def next_difficulty(self, pattern):
        """Determine next difficulty level"""
        current = self.current_difficulty(pattern)
        pattern_data = self.progress.get('patterns', {}).get(pattern, {})

        easy_count = pattern_data.get('easy', 0)
        medium_count = pattern_data.get('medium', 0)

        if current == 'easy' and easy_count >= 2:
            return 'medium'
        elif current == 'medium' and medium_count >= 3:
            return 'hard'
        else:
            return current

    def generate_tomorrow_event(self):
        """Generate adaptive calendar event for tomorrow"""

        decision = self.decide_next_task()

        # Get motivational quote based on action
        quotes = {
            'review': "Mastery comes from repetition. Review strengthens foundations.",
            'accelerate': "You're crushing it! Time to level up the challenge.",
            'maintain': "Consistency is the secret. Keep building the habit.",
            'continue': "Steady progress wins the race. Keep going.",
            'new_pattern': "New pattern unlocked! Your toolkit expands."
        }

        quote = quotes.get(decision['action'], "Today's effort is tomorrow's strength.")

        # Format event
        event = {
            'summary': f"🎯 DSA: {decision['pattern'].replace('_', ' ').title()} - {decision['difficulty'].title()}",
            'start_date': (datetime.now() + timedelta(days=1)).replace(hour=9, minute=0),
            'duration_minutes': 90,
            'description': self.create_event_description(decision, quote)
        }

        return event

    def create_event_description(self, decision, quote):
        """Create rich event description"""

        # Get resources for pattern
        resources = self.get_pattern_resources(decision['pattern'])

        description = f"""
<h2>🎯 Today's Mission</h2>
<p><strong>{quote}</strong></p>

<h3>📋 Your Task</h3>
<p><strong>Pattern</strong>: {decision['pattern'].replace('_', ' ').title()}</p>
<p><strong>Difficulty</strong>: {decision['difficulty'].title()}</p>
<p><strong>Problems to solve</strong>: {decision['count']}</p>
<p><strong>Why</strong>: {decision['note']}</p>

<h3>🚀 Workflow</h3>
<ol>
<li>Say to Claude: "Give me a {decision['difficulty']} {decision['pattern'].replace('_', ' ')} problem"</li>
<li>Solve in Rust (30 min)</li>
<li>Generate visualization (5 min)</li>
<li>Optional: Solve in Ruby (15 min)</li>
<li>Create PR (5 min)</li>
<li>Get Claude review (10 min)</li>
<li>Optimize & merge (10 min)</li>
</ol>

<h3>🎓 Quick Resources</h3>
<ul>
"""

        for resource in resources:
            emoji = "🎥" if resource['type'] == 'video' else "📄"
            description += f"<li>{emoji} <a href='{resource['url']}'>{resource['title']}</a> ({resource['duration']})</li>\n"

        description += f"""
</ul>

<h3>📊 Your Progress</h3>
<ul>
<li>Learning velocity: {self.calculate_learning_velocity():.1f} problems/day</li>
<li>Pattern mastery: {self.get_pattern_mastery(decision['pattern'])['problems_solved']}/{self.config['mastery_threshold']}</li>
<li>Success rate: {self.calculate_success_rate(decision['pattern']):.1f}%</li>
</ul>

<h3>🔗 Quick Links</h3>
<ul>
<li>📚 <a href="https://yourusername.github.io/dsa-mastery">Progress Dashboard</a></li>
<li>💻 <a href="https://github.com/yourusername/dsa-mastery">GitHub Repo</a></li>
<li>📊 <a href="https://yourusername.github.io/dsa-mastery/progress.html">Statistics</a></li>
</ul>

<hr>
<p><em>This event was automatically adapted to your learning pace.</em></p>
<p><em>After solving, run: <code>python scripts/calendar/update_tomorrow.py</code></em></p>
"""

        return description

    def get_pattern_resources(self, pattern):
        """Get learning resources for pattern"""

        # Resource database
        resources_db = {
            'two_pointers': [
                {'title': 'Two Pointers Explained', 'url': 'https://www.youtube.com/watch?v=On03HWe2tZM', 'type': 'video', 'duration': '8 min'},
                {'title': 'Why Two Pointers Works', 'url': 'https://leetcode.com/discuss/study-guide/1688903/', 'type': 'article', 'duration': '5 min read'}
            ],
            'sliding_window': [
                {'title': 'Sliding Window Visualization', 'url': 'https://www.youtube.com/watch?v=MK-NZ4hN7rs', 'type': 'video', 'duration': '12 min'},
                {'title': 'Fixed vs Dynamic Window', 'url': 'https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66', 'type': 'article', 'duration': '7 min read'}
            ],
            # Add more patterns...
        }

        return resources_db.get(pattern, [
            {'title': f'{pattern.replace("_", " ").title()} Pattern Guide', 'url': '#', 'type': 'article', 'duration': '10 min read'}
        ])

    def update_google_calendar(self, event):
        """Update tomorrow's Google Calendar event"""

        # This would use Google Calendar API
        # For now, we'll create a .ics file you can import

        ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//DSA Mastery//Adaptive Scheduler//EN
BEGIN:VEVENT
UID:{datetime.now().timestamp()}@dsa-mastery.local
DTSTAMP:{datetime.now().strftime('%Y%m%dT%H%M%SZ')}
DTSTART:{event['start_date'].strftime('%Y%m%dT%H%M%S')}
DTEND:{(event['start_date'] + timedelta(minutes=event['duration_minutes'])).strftime('%Y%m%dT%H%M%S')}
SUMMARY:{event['summary']}
DESCRIPTION:{event['description'].replace('\n', '\\n')}
END:VEVENT
END:VCALENDAR
"""

        # Save to file
        output_file = self.base_dir / 'calendar_updates' / f"tomorrow_{datetime.now().strftime('%Y%m%d')}.ics"
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'w') as f:
            f.write(ics_content)

        return output_file

    def run(self):
        """Main execution - update tomorrow's calendar"""

        print("🔄 Analyzing your learning progress...")
        print(f"   Velocity: {self.calculate_learning_velocity():.1f} problems/day")
        print(f"   Current pattern: {self.config['current_pattern']}")

        decision = self.decide_next_task()

        print(f"\n📋 Tomorrow's plan:")
        print(f"   Action: {decision['action']}")
        print(f"   Pattern: {decision['pattern']}")
        print(f"   Difficulty: {decision['difficulty']}")
        print(f"   Problems: {decision['count']}")
        print(f"   Reason: {decision['note']}")

        event = self.generate_tomorrow_event()

        print(f"\n📅 Generating calendar event...")
        ics_file = self.update_google_calendar(event)

        print(f"\n✅ Done!")
        print(f"\n📎 Import to Google Calendar:")
        print(f"   File: {ics_file}")
        print(f"\n   1. Open Google Calendar")
        print(f"   2. Settings → Import & Export")
        print(f"   3. Import {ics_file.name}")
        print(f"\nOR use Google Calendar API (see setup instructions)")


if __name__ == "__main__":
    scheduler = AdaptiveScheduler()
    scheduler.run()
