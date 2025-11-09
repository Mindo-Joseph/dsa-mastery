# Automatic Google Calendar Updates - Setup Guide

**Make your calendar update automatically without manual .ics imports**

---

## 🎯 What This Does

After you solve each problem and run:
```bash
./scripts/calendar/update_tomorrow.sh
```

**Automatically:**
1. Analyzes your progress
2. Generates tomorrow's adaptive event
3. **Updates Google Calendar directly** (no manual import!)

---

## ⚡ Quick Setup (10 minutes)

### **Step 1: Install Google Calendar API Library**

```bash
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### **Step 2: Get Google Calendar API Credentials**

1. Go to https://console.cloud.google.com/
2. Create new project: "DSA-Mastery-Calendar"
3. Enable "Google Calendar API":
   - APIs & Services → Library
   - Search "Google Calendar API"
   - Click "Enable"
4. Create OAuth 2.0 Credentials:
   - APIs & Services → Credentials
   - "Create Credentials" → "OAuth client ID"
   - Application type: "Desktop app"
   - Name: "DSA Mastery Calendar Sync"
   - Click "Create"
5. Download credentials:
   - Click the download icon (⬇️) next to your new OAuth 2.0 Client
   - Save as `credentials.json`

### **Step 3: Move Credentials to Project**

```bash
mv ~/Downloads/credentials.json ~/dsa-mastery/scripts/calendar/credentials.json
```

### **Step 4: First-Time Authentication**

```bash
cd ~/dsa-mastery
python3 scripts/auto_update_calendar.py
```

**What happens:**
- Browser opens
- You log in with Google
- Grant calendar permissions
- Authentication is saved
- First event is created automatically!

### **Step 5: Update the Daily Script**

Edit `scripts/calendar/update_tomorrow.sh`:

```bash
#!/bin/bash
cd ~/dsa-mastery

echo "📊 Analyzing your progress..."
python3 scripts/calendar/adaptive_scheduler.py

echo ""
echo "📅 Auto-updating Google Calendar..."
python3 scripts/auto_update_calendar.py

echo ""
echo "✨ Done! Tomorrow's event is ready in your Google Calendar"
```

Make it executable:
```bash
chmod +x ~/dsa-mastery/scripts/calendar/update_tomorrow.sh
```

---

## 🔄 Daily Usage

After solving each problem:

```bash
# Log progress
python scripts/log_progress.py log pattern problem difficulty time status

# Update calendar automatically
./scripts/calendar/update_tomorrow.sh
```

**That's it!** Calendar updates automatically in Google.

---

## ⚙️ Configure Your Timezone

Edit `scripts/auto_update_calendar.py` line 96:

```python
'timeZone': 'America/New_York',  # Change to your timezone
```

**Common timezones:**
- `America/New_York` (EST/EDT)
- `America/Los_Angeles` (PST/PDT)
- `America/Chicago` (CST/CDT)
- `Europe/London` (GMT/BST)
- `Africa/Nairobi` (EAT)
- `Asia/Tokyo` (JST)

Full list: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

---

## 🔧 Advanced: Git Hook (Fully Automatic)

Make calendar update every time you commit:

```bash
cat > ~/dsa-mastery/.git/hooks/post-commit << 'EOF'
#!/bin/bash
# Auto-update calendar after each commit

cd ~/dsa-mastery
./scripts/calendar/update_tomorrow.sh > /dev/null 2>&1 &

echo "📅 Calendar updating in background..."
EOF

chmod +x ~/dsa-mastery/.git/hooks/post-commit
```

**Now:**
```bash
git commit -m "Solved two sum"
# Calendar automatically updates!
```

---

## 🆚 Comparison

### **Manual Method (Original)**
```
1. Solve problem
2. Run: ./scripts/calendar/update_tomorrow.sh
3. Download .ics file
4. Open Google Calendar
5. Settings → Import & Export
6. Select file
7. Import
```
**7 steps!**

### **Automatic Method (New)**
```
1. Solve problem
2. Run: ./scripts/calendar/update_tomorrow.sh
```
**2 steps!** Calendar updates automatically.

---

## ❓ Troubleshooting

### **"credentials.json not found"**
- Download from Google Cloud Console (Step 2 above)
- Save to `~/dsa-mastery/scripts/calendar/credentials.json`

### **"Authentication failed"**
```bash
# Remove old token and re-authenticate
rm ~/dsa-mastery/scripts/calendar/token.pickle
python3 scripts/auto_update_calendar.py
```

### **Wrong timezone**
- Edit `scripts/auto_update_calendar.py` line 96
- Change to your timezone

### **Event not showing**
- Check you're logged into the right Google account
- Refresh Google Calendar
- Check spam/trash in calendar

---

## 🎯 What Gets Updated

Every day after you solve problems:

**Before (today):**
```
Tomorrow: Two Pointers - Medium (2 problems)
```

**After you log progress:**
```
System analyzes:
- You solved 3 problems today (fast!)
- 90% success rate (crushing it!)

Tomorrow: Two Pointers - Hard (3 problems)
  "Strong performance - increasing challenge"
```

**Google Calendar updates automatically!**

---

## 🔒 Security

**Is this safe?**
- OAuth 2.0 is industry standard
- Credentials stay on your machine
- Token has calendar-only access
- Can revoke anytime at https://myaccount.google.com/permissions

---

## 🚀 Quick Start Summary

```bash
# 1. Install library
pip3 install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# 2. Get credentials from Google Cloud Console
# (Follow Step 2 above)

# 3. Save credentials
mv ~/Downloads/credentials.json ~/dsa-mastery/scripts/calendar/

# 4. Authenticate once
python3 scripts/auto_update_calendar.py

# 5. Done! Use daily:
./scripts/calendar/update_tomorrow.sh
```

---

**Calendar updates become automatic. Focus on solving, not scheduling.** 📅✨
