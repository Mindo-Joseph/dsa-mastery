#!/usr/bin/env python3
"""
Google Calendar Integration for DSA Mastery

Creates daily calendar events with:
- Pattern/problem for the day
- Motivational content
- Links to resources, videos, articles
- Progress tracking

Requires: google-auth, google-api-python-client
Install: pip install google-auth google-api-python-client google-auth-oauthlib
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# Will be populated after Google Calendar API setup
PATTERN_SCHEDULE = {
    # Week 1-2: Foundation
    "week_1": {
        "pattern": "Two Pointers",
        "days": 7,
        "problems_per_day": 1,
        "motivation": "Master the foundation. Two pointers is your gateway to thinking like a senior engineer.",
        "resources": [
            {
                "title": "Two Pointers Technique Explained",
                "url": "https://www.youtube.com/watch?v=On03HWe2tZM",
                "type": "video",
                "duration": "8 min"
            },
            {
                "title": "Why Two Pointers Works - Intuition",
                "url": "https://leetcode.com/discuss/study-guide/1688903/",
                "type": "article",
                "duration": "5 min read"
            }
        ]
    },
    "week_2": {
        "pattern": "Sliding Window",
        "days": 7,
        "problems_per_day": 1,
        "motivation": "Sliding window is two pointers evolved. Master state management.",
        "resources": [
            {
                "title": "Sliding Window Technique Visualization",
                "url": "https://www.youtube.com/watch?v=MK-NZ4hN7rs",
                "type": "video",
                "duration": "12 min"
            },
            {
                "title": "Fixed vs Dynamic Window - When to Use Each",
                "url": "https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66",
                "type": "article",
                "duration": "7 min read"
            }
        ]
    },
    # Add more weeks...
}

MOTIVATIONAL_QUOTES = [
    "Today's problem is tomorrow's pattern recognition. You're building intuition.",
    "Senior engineers don't memorize solutions. They understand principles. You're on that path.",
    "Every optimal solution you write is practice for the Google interview. Make it count.",
    "Consistency > Intensity. Show up today. The streak matters more than perfection.",
    "You're not just solving problems. You're training your brain to think in algorithms.",
    "Google senior engineers can prove complexity on the spot. That's your standard now.",
    "First principles thinking separates senior engineers from everyone else. Keep asking WHY.",
    "The problem might take 30 minutes. The understanding lasts forever.",
    "Your future Google teammates are solving these same patterns right now. Join them.",
    "12 weeks. 60+ problems. 1 goal: Senior engineer at Google. Stay focused.",
]


def create_calendar_event_description(day_num, pattern, problems, resources):
    """Create rich HTML description for calendar event"""

    quote = MOTIVATIONAL_QUOTES[day_num % len(MOTIVATIONAL_QUOTES)]

    description = f"""
<h2>🎯 Day {day_num} - {pattern} Pattern</h2>

<h3>💪 Today's Mission</h3>
<p><strong>{quote}</strong></p>

<h3>📝 Problems to Solve ({len(problems)})</h3>
<ul>
"""

    for i, problem in enumerate(problems, 1):
        description += f"<li><strong>Problem {i}</strong>: {problem['title']} ({problem['difficulty']})</li>\n"

    description += """
</ul>

<h3>🚀 Your Workflow Today</h3>
<ol>
<li><strong>Review writeup</strong> (10 min) - Understand first principles</li>
<li><strong>Solve problem</strong> (30 min) - Apply the pattern</li>
<li><strong>Create PR</strong> (5 min) - Document your approach</li>
<li><strong>Get review</strong> (10 min) - Senior-level feedback</li>
<li><strong>Optimize & merge</strong> (10 min) - Iterate to perfection</li>
</ol>

<h3>🎓 Quick Learning Resources</h3>
<ul>
"""

    for resource in resources:
        emoji = "🎥" if resource['type'] == 'video' else "📄"
        description += f"""<li>{emoji} <a href="{resource['url']}">{resource['title']}</a> ({resource['duration']})</li>\n"""

    description += f"""
</ul>

<h3>🔗 Quick Links</h3>
<ul>
<li>📚 <a href="https://yourusername.github.io/dsa-mastery/patterns/{pattern.lower().replace(' ', '-')}.html">Pattern Writeup</a></li>
<li>💻 <a href="https://github.com/yourusername/dsa-mastery">GitHub Repo</a></li>
<li>📊 <a href="https://yourusername.github.io/dsa-mastery/progress.html">Progress Dashboard</a></li>
</ul>

<h3>✅ Mark as Done</h3>
<p>After solving, run: <code>python scripts/log_progress.py log {pattern.lower().replace(' ', '_')} problem-name difficulty time status</code></p>

<hr>
<p><em>Excellence is built one day at a time. Make today count.</em></p>
"""

    return description


def generate_schedule(start_date, weeks=12):
    """Generate full 12-week schedule"""

    schedule = []
    current_date = start_date
    day_num = 1

    # Example for week 1
    pattern_info = PATTERN_SCHEDULE["week_1"]

    for day in range(pattern_info["days"]):
        event = {
            "summary": f"🎯 DSA Day {day_num}: {pattern_info['pattern']} - Problem {day + 1}",
            "start_date": current_date.isoformat(),
            "duration_minutes": 90,  # 1.5 hours
            "pattern": pattern_info['pattern'],
            "day_num": day_num,
            "description": create_calendar_event_description(
                day_num,
                pattern_info['pattern'],
                [
                    {
                        "title": f"{pattern_info['pattern']} Problem {day + 1}",
                        "difficulty": "Easy" if day < 2 else "Medium" if day < 5 else "Hard"
                    }
                ],
                pattern_info['resources']
            )
        }

        schedule.append(event)
        current_date += timedelta(days=1)
        day_num += 1

    return schedule


def save_schedule_json(schedule, output_file="schedule.json"):
    """Save schedule to JSON for manual import"""

    with open(output_file, 'w') as f:
        json.dump(schedule, f, indent=2)

    print(f"✓ Schedule saved to {output_file}")
    print(f"  Total events: {len(schedule)}")
    print(f"\nNext steps:")
    print("1. Review schedule.json")
    print("2. Import to Google Calendar (see instructions below)")


def print_google_calendar_instructions():
    """Print instructions for manual Google Calendar setup"""

    print("\n" + "="*60)
    print("GOOGLE CALENDAR SETUP INSTRUCTIONS")
    print("="*60)
    print("""
Option 1: Manual Creation (Simple, Recommended)
------------------------------------------------
1. Open Google Calendar: https://calendar.google.com
2. Click "Create" button
3. Add event details:
   - Title: Copy from schedule.json "summary"
   - Date: Copy from "start_date"
   - Duration: 1.5 hours (adjust as needed)
   - Description: Copy HTML from "description"
4. Set reminder: 30 min before
5. Repeat for each day (or week at a time)

Option 2: Automated with Google Calendar API (Advanced)
--------------------------------------------------------
Requires OAuth setup:

1. Go to: https://console.cloud.google.com/
2. Create new project: "DSA-Mastery-Calendar"
3. Enable Google Calendar API
4. Create OAuth 2.0 credentials
5. Download credentials.json to this directory
6. Run: python scripts/calendar/setup_oauth.py
7. Run: python scripts/calendar/create_events.py --auto

Option 3: CSV Import (Fastest for bulk)
----------------------------------------
1. Run: python scripts/calendar/export_csv.py
2. Open Google Calendar → Settings → Import & Export
3. Import the generated CSV file
4. All events created at once!

Option 4: .ics File Import
---------------------------
1. Run: python scripts/calendar/export_ics.py
2. Open Google Calendar → Settings → Import & Export
3. Select .ics file
4. Events imported with full formatting

RECOMMENDED: Start with Option 3 (CSV) - fastest setup!
""")
    print("="*60 + "\n")


def create_csv_export(schedule, output_file="dsa_schedule.csv"):
    """Create CSV for Google Calendar import"""

    import csv

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Google Calendar CSV format
        writer.writerow([
            'Subject', 'Start Date', 'Start Time', 'End Date', 'End Time',
            'All Day Event', 'Description', 'Location', 'Private'
        ])

        for event in schedule:
            start_dt = datetime.fromisoformat(event['start_date'])
            end_dt = start_dt + timedelta(minutes=event['duration_minutes'])

            # Remove HTML tags for CSV (Google Calendar will accept HTML in description)
            description = event['description'].replace('\n', ' ')

            writer.writerow([
                event['summary'],
                start_dt.strftime('%m/%d/%Y'),
                start_dt.strftime('%I:%M %p'),
                end_dt.strftime('%m/%d/%Y'),
                end_dt.strftime('%I:%M %p'),
                'False',
                description,
                'DSA Mastery Workspace',
                'False'
            ])

    print(f"\n✓ CSV created: {output_file}")
    print(f"  Ready for Google Calendar import!")
    print(f"\nImport steps:")
    print("1. Open https://calendar.google.com")
    print("2. Settings (gear icon) → Import & Export")
    print("3. Select file → Import")
    print("4. Choose calendar → Import")
    print("\n✨ All your daily DSA events will appear!")


if __name__ == "__main__":
    import sys

    # Start date (default: tomorrow)
    start_date = datetime.now() + timedelta(days=1)
    start_date = start_date.replace(hour=9, minute=0, second=0, microsecond=0)

    if len(sys.argv) > 1:
        # Allow custom start date: python create_events.py 2025-11-10
        start_date = datetime.fromisoformat(sys.argv[1])
        start_date = start_date.replace(hour=9, minute=0)

    print(f"Generating DSA Mastery schedule...")
    print(f"Start date: {start_date.strftime('%Y-%m-%d')}")
    print(f"Daily time: 9:00 AM (1.5 hours)")
    print()

    # Generate schedule
    schedule = generate_schedule(start_date, weeks=12)

    # Save JSON
    save_schedule_json(schedule)

    # Create CSV for easy import
    create_csv_export(schedule)

    # Print instructions
    print_google_calendar_instructions()
