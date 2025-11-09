#!/usr/bin/env python3
"""
Automatic Calendar Update via Google Calendar API

This script automatically updates Google Calendar without manual .ics imports.
Runs after each problem is logged.

Setup:
1. Enable Google Calendar API in Google Cloud Console
2. Download credentials.json
3. Run this script - it will authenticate once
4. Future updates are automatic
"""

import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    import pickle
except ImportError:
    print("❌ Google Calendar API libraries not installed")
    print("\nInstall with:")
    print("  pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    sys.exit(1)

# Google Calendar API setup
SCOPES = ['https://www.googleapis.com/auth/calendar']
CALENDAR_ID = 'primary'  # or specific calendar ID


class GoogleCalendarSync:
    """Automatic Google Calendar synchronization"""

    def __init__(self):
        self.base_dir = Path.home() / 'dsa-mastery'
        self.token_file = self.base_dir / 'scripts' / 'calendar' / 'token.pickle'
        self.credentials_file = self.base_dir / 'scripts' / 'calendar' / 'credentials.json'
        self.service = None

    def authenticate(self):
        """Authenticate with Google Calendar API"""
        creds = None

        # Load existing token
        if self.token_file.exists():
            with open(self.token_file, 'rb') as token:
                creds = pickle.load(token)

        # Refresh or get new credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not self.credentials_file.exists():
                    print("❌ credentials.json not found!")
                    print("\nGet credentials:")
                    print("1. Go to https://console.cloud.google.com/")
                    print("2. Create project: 'DSA-Mastery-Calendar'")
                    print("3. Enable Google Calendar API")
                    print("4. Create OAuth 2.0 credentials")
                    print("5. Download as credentials.json")
                    print(f"6. Save to: {self.credentials_file}")
                    sys.exit(1)

                flow = InstalledAppFlow.from_client_secrets_file(
                    str(self.credentials_file), SCOPES)
                creds = flow.run_local_server(port=0)

            # Save credentials
            with open(self.token_file, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)
        return True

    def create_or_update_event(self, event_data):
        """Create or update tomorrow's event"""

        # Check if event already exists for tomorrow
        tomorrow = event_data['start_date']
        tomorrow_start = tomorrow.replace(hour=0, minute=0, second=0).isoformat() + 'Z'
        tomorrow_end = tomorrow.replace(hour=23, minute=59, second=59).isoformat() + 'Z'

        # Search for existing event
        events_result = self.service.events().list(
            calendarId=CALENDAR_ID,
            timeMin=tomorrow_start,
            timeMax=tomorrow_end,
            q='DSA:',  # Search for events with "DSA:" in title
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])

        # Prepare event
        event = {
            'summary': event_data['summary'],
            'description': event_data['description'],
            'start': {
                'dateTime': event_data['start_date'].isoformat(),
                'timeZone': 'America/New_York',  # Adjust to your timezone
            },
            'end': {
                'dateTime': (event_data['start_date'] + timedelta(minutes=event_data['duration_minutes'])).isoformat(),
                'timeZone': 'America/New_York',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'popup', 'minutes': 30},
                ],
            },
        }

        if events:
            # Update existing event
            event_id = events[0]['id']
            updated_event = self.service.events().update(
                calendarId=CALENDAR_ID,
                eventId=event_id,
                body=event
            ).execute()
            print(f"✅ Updated tomorrow's calendar event")
            print(f"   {event_data['summary']}")
            return updated_event
        else:
            # Create new event
            created_event = self.service.events().insert(
                calendarId=CALENDAR_ID,
                body=event
            ).execute()
            print(f"✅ Created tomorrow's calendar event")
            print(f"   {event_data['summary']}")
            return created_event

    def run(self, event_data):
        """Main execution"""
        if not self.authenticate():
            return False

        self.create_or_update_event(event_data)
        return True


def main():
    """Run automatic calendar sync"""

    # Import adaptive scheduler
    sys.path.insert(0, str(Path(__file__).parent))
    from adaptive_scheduler import AdaptiveScheduler

    print("🔄 Generating tomorrow's adaptive event...")
    scheduler = AdaptiveScheduler()
    event = scheduler.generate_tomorrow_event()

    print("\n📅 Syncing to Google Calendar...")
    sync = GoogleCalendarSync()

    try:
        sync.run(event)
        print("\n✨ Calendar automatically updated!")
        print("   Check Google Calendar to see tomorrow's task")
    except Exception as e:
        print(f"\n❌ Failed to sync to calendar: {e}")
        print("\nFallback: Manual import")
        print(f"   Import file: {scheduler.update_google_calendar(event)}")


if __name__ == "__main__":
    main()
