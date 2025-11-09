# Setup Steps - Simple Version

**Quick checklist - do these in order:**

---

## ✅ **Phase 1: Core System (10 min)**

```bash
# 1. Install tools
sudo apt-get update
sudo apt-get install -y build-essential git python3 python3-pip

# 2. Configure git (YOUR info)
git config --global user.name "Your Name"
git config --global user.email "your@email.com"

# 3. Test Rust
cd ~/dsa-mastery
source "$HOME/.cargo/env"
cargo build
```

---

## ✅ **Phase 2: GitHub (5 min)**

**Create repo + enable Pages:**
```bash
# Login to GitHub
gh auth login

# Create repo
cd ~/dsa-mastery
gh repo create dsa-mastery --public --source=. --remote=origin --push
```

**Enable Pages:**
- Go to repo Settings → Pages
- Source: `main` branch, `/docs` folder
- Save

---

## ✅ **Phase 3: NotebookLM (5 min)**

**In Claude, say:**
```
"Set up NotebookLM authentication"
```
*(Browser opens, login)*

```
"Add my leetcode notebook: [URL]"
"Add my algorithm book: [URL]"
```

---

## ✅ **Phase 4: Adaptive Calendar (NEW - 5 min)**

**Generate FIRST event only:**
```bash
cd ~/dsa-mastery
python3 scripts/calendar/adaptive_scheduler.py
```

**Import to Google Calendar:**
1. Open calendar.google.com
2. Settings → Import & Export
3. Import the generated `.ics` file from `calendar_updates/`

**That's it!** Calendar will auto-update daily based on your progress.

---

## ✅ **Phase 5: Optional (10 min)**

**Visualization:**
```bash
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev
pip3 install manim
```

**Ruby:**
```bash
sudo apt-get install -y ruby-full
cd src_ruby && bundle install
```

---

## 🚀 **Start Learning**

**Say to Claude:**
```
"Start pattern 1: Two Pointers"
```

---

## 📅 **Daily Workflow with Adaptive Calendar**

### **Morning:**
- Check Google Calendar (shows today's adaptive task)

### **During:**
- Solve problems
- Create PRs
- Get reviews

### **After Each Problem:**
```bash
# Log progress
python scripts/log_progress.py log pattern problem difficulty time status

# Update tomorrow's calendar
./scripts/calendar/update_tomorrow.sh
```

**System analyzes your progress and adjusts tomorrow automatically!**

---

## 🔄 **How Adaptive Calendar Works**

**After you log a problem:**
1. System calculates your learning velocity
2. Checks pattern mastery
3. Analyzes success rate
4. Decides tomorrow's task:
   - Fast learner? → More/harder problems
   - Struggling? → Review problems
   - Mastered pattern? → Move to next
5. Generates new calendar event
6. You import it (or auto-sync with API)

**Calendar matches YOUR pace, not a fixed schedule!**

---

## ⚡ **Key Differences from Original Setup**

### **Original Calendar:**
```bash
# Generated ALL 12 weeks upfront
python3 scripts/calendar/create_events.py
# Import dsa_schedule.csv
```
**Problem:** Fixed schedule, doesn't adapt

### **New Adaptive Calendar:**
```bash
# Generates TOMORROW only, based on TODAY's progress
./scripts/calendar/update_tomorrow.sh
# Import single .ics file
```
**Benefit:** Adapts to YOUR actual pace!

---

## 📊 **What Gets Analyzed**

- **Velocity**: Problems per day
- **Success Rate**: First-attempt solve rate
- **Pattern Mastery**: Problems solved, difficulty progression
- **Current Level**: What difficulty you're at

**Result**: Tomorrow's task perfectly matched to you!

---

## 📚 **Read More**

- **ADAPTIVE_CALENDAR.md** - Full explanation
- **COMPLETE_SETUP.md** - Detailed setup (if stuck)
- **START_HERE.md** - System overview

---

**Setup is simpler now - only generate tomorrow's event, not entire 12 weeks!** ⚡
