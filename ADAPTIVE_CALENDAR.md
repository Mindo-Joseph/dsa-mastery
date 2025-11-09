# Adaptive Calendar System

**Your calendar adjusts to YOUR learning pace - not a fixed schedule.**

---

## 🎯 How It Works

### **Traditional Calendar (Rigid)**
```
Day 1: Two Pointers Problem 1
Day 2: Two Pointers Problem 2
Day 3: Two Pointers Problem 3
...
```
**Problem**: What if you master it in 2 days? Or need 5 days?

### **Adaptive Calendar (Smart)**
```
After each problem solved:
→ Analyzes your performance
→ Calculates learning velocity
→ Adjusts tomorrow's task
→ Updates calendar automatically
```

**Result**: Calendar matches YOUR pace, not arbitrary dates.

---

## 📊 What It Analyzes

### **1. Learning Velocity**
- Problems solved per day (last 7 days)
- **Fast** (>3/day): Increase difficulty, add problems
- **Normal** (1-3/day): Continue current pace
- **Slow** (<1/day): Review fundamentals, easier problems

### **2. Success Rate**
- First-attempt success on problems
- **High** (>80%): Ready for harder problems
- **Medium** (50-80%): Continue current level
- **Low** (<50%): Add review problems

### **3. Pattern Mastery**
- Problems solved per pattern
- Success rate on pattern
- **Mastered** (5+ problems, >80% success): Move to next pattern
- **Learning**: Continue with progression
- **Struggling**: Add review, slow down

### **4. Current Difficulty**
- What difficulty you're solving
- Automatically progresses: Easy → Medium → Hard
- Or stays at level if needed

---

## 🔄 Adaptive Decisions

### **Scenario 1: Fast Learner**
```
You: Solved 4 two-pointers problems today, 100% success
System:
  ✓ Detects high velocity
  ✓ Tomorrow: 3 medium problems (harder + more)
  ✓ Calendar: "Strong performance - increasing challenge"
```

### **Scenario 2: Struggling**
```
You: Solved 1 problem, took 90 min, partial success
System:
  ✓ Detects low success rate
  ✓ Tomorrow: 1 easy review problem
  ✓ Calendar: "Reviewing fundamentals - building confidence"
```

### **Scenario 3: Mastered Pattern**
```
You: Completed 6 two-pointers, 85% success rate
System:
  ✓ Detects pattern mastery
  ✓ Tomorrow: Move to Sliding Window (new pattern)
  ✓ Calendar: "Mastered Two Pointers! Starting Sliding Window"
```

### **Scenario 4: Normal Progress**
```
You: Solving 2 problems/day, ~75% success
System:
  ✓ Continue current pace
  ✓ Tomorrow: 2 problems, next difficulty
  ✓ Calendar: "Solid progress - continuing pattern"
```

---

## 🚀 How to Use

### **Daily Workflow**

**Morning:**
```bash
# Check tomorrow's adaptive plan
cat calendar_updates/tomorrow_*.ics
```

**After Each Problem:**
```bash
# Log your completion
python scripts/log_progress.py log \
  two_pointers \
  problem-name \
  medium \
  35 \
  success

# Update tomorrow's calendar
./scripts/calendar/update_tomorrow.sh
```

**System automatically:**
1. Analyzes your progress
2. Decides tomorrow's task
3. Generates calendar event
4. Creates .ics file to import

---

## ⚙️ Configuration

Edit `scripts/calendar/learning_config.json`:

```json
{
  "current_pattern": "two_pointers",
  "target_problems_per_day": 2,
  "mastery_threshold": 5,
  "adaptive_mode": true,

  "velocity_thresholds": {
    "fast": 3,
    "slow": 1
  },

  "success_thresholds": {
    "high": 80,
    "low": 50
  }
}
```

**Adjust based on:**
- Your available time
- Learning goals
- Current skill level

---

## 📅 Calendar Integration Options

### **Option 1: Manual Import (Simple)**
```bash
# After each problem
./scripts/calendar/update_tomorrow.sh

# Import the generated .ics file
# calendar_updates/tomorrow_YYYYMMDD.ics
```

**Steps:**
1. Open Google Calendar
2. Settings → Import & Export
3. Import the .ics file
4. Done!

### **Option 2: Automatic (Advanced)**

**Set up Google Calendar API:**
```bash
# See scripts/calendar/GOOGLE_CALENDAR_API_SETUP.md
# Requires OAuth credentials
```

**Then it auto-updates calendar without manual import!**

### **Option 3: Git Hook (Automated)**

```bash
# Add to .git/hooks/post-commit
#!/bin/bash
./scripts/calendar/update_tomorrow.sh
```

**Now calendar updates automatically when you commit!**

---

## 🎓 What Tomorrow's Event Looks Like

**Adaptive event includes:**

```
🎯 DSA: Two Pointers - Medium

💪 Today's Mission
"Solid progress - continuing pattern"

📋 Your Task
Pattern: Two Pointers
Difficulty: Medium
Problems to solve: 2
Why: Current velocity is healthy, progressing difficulty

🚀 Workflow
1. Say to Claude: "Give me a medium two_pointers problem"
2. Solve in Rust (30 min)
3. Generate visualization (5 min)
4. Optional: Solve in Ruby (15 min)
5. Create PR (5 min)
6. Get Claude review (10 min)
7. Optimize & merge (10 min)

🎓 Quick Resources
🎥 Two Pointers Explained (8 min)
📄 Why Two Pointers Works (5 min read)

📊 Your Progress
Learning velocity: 2.3 problems/day
Pattern mastery: 4/5
Success rate: 75.0%

🔗 Quick Links
📚 Progress Dashboard
💻 GitHub Repo
📊 Statistics

This event was automatically adapted to your learning pace.
After solving, run: python scripts/calendar/update_tomorrow.py
```

---

## 📊 Progress-Based Adaptation Examples

### **Week 1 - Learning**
```
Mon: 2 easy problems (starting out)
Tue: 2 easy problems (building confidence)
Wed: 1 medium problem (first challenge)
Thu: 2 medium problems (adapting to you)
Fri: 3 medium problems (you're fast!)
```

### **Week 2 - Mastering**
```
Mon: 2 hard problems (pushing limits)
Tue: 1 hard + review (detected struggle)
Wed: 2 medium problems (consolidating)
Thu: New pattern! (mastered previous)
Fri: 2 easy (new pattern start)
```

**See how it adapts to YOUR actual performance?**

---

## 🔧 Advanced Features

### **Pattern Progression**

System knows the optimal pattern order:
1. Two Pointers
2. Sliding Window
3. Binary Search
4. Fast/Slow Pointers
5. Linked List Reversal
6. Tree BFS/DFS
7. Graphs
8. Heaps
9. Dynamic Programming
10. Backtracking

**Auto-advances when you master each pattern.**

### **Difficulty Progression**

Within each pattern:
```
2 easy → 3 medium → 2 hard → mastery
```

**Adjusts based on your success rate.**

### **Review Integration**

If success rate drops:
```
- Adds review problems
- Returns to easier difficulty
- Schedules spaced repetition
```

---

## 💡 Smart Features

### **Motivational Quotes**

Changes based on your situation:
- Struggling: "Mastery comes from repetition"
- Fast: "You're crushing it! Time to level up"
- Normal: "Steady progress wins the race"
- New pattern: "New pattern unlocked!"

### **Resource Links**

Dynamically includes relevant resources:
- Pattern-specific videos
- Articles for current difficulty
- Visualization examples

### **Progress Stats**

Shows your current metrics:
- Learning velocity
- Pattern mastery
- Success rate

**You see your growth in every event!**

---

## 🎯 Integration with Workflow

### **Updated Daily Flow**

```
1. Check calendar (adaptive event)
2. Say: "Give me today's problem"  ← I know from calendar
3. Solve → PR → Review → Optimize
4. Log progress: python scripts/log_progress.py log ...
5. Update tomorrow: ./scripts/calendar/update_tomorrow.sh
6. System adapts to your performance
7. Tomorrow's calendar reflects YOUR pace
```

**Your calendar becomes smarter every day!**

---

## 🆚 Comparison

### **Static Calendar**
- ❌ Fixed schedule regardless of progress
- ❌ Too fast or too slow
- ❌ Doesn't account for life events
- ❌ One-size-fits-all
- ❌ Manual updates

### **Adaptive Calendar**
- ✅ Adjusts to YOUR pace
- ✅ Matches your learning velocity
- ✅ Detects struggles, adjusts
- ✅ Personalized to you
- ✅ Automatic updates

---

## 🚀 Quick Start

### **Initial Setup**

```bash
# Create first calendar event
python3 scripts/calendar/adaptive_scheduler.py

# Import to Google Calendar
# (Import the generated .ics file)
```

### **After Each Problem**

```bash
# Log completion
python scripts/log_progress.py log pattern problem difficulty time status

# Update tomorrow
./scripts/calendar/update_tomorrow.sh

# Import new .ics if manual mode
```

### **Check Tomorrow's Plan**

```bash
# See what's planned
cat calendar_updates/tomorrow_*.ics

# Or just check your Google Calendar
```

---

## 📚 Files Created

```
scripts/calendar/
├── adaptive_scheduler.py      - Main adaptive logic
├── update_tomorrow.sh         - Quick update script
├── learning_config.json       - Your settings (auto-created)
└── GOOGLE_CALENDAR_API_SETUP.md - API setup guide (optional)

calendar_updates/
└── tomorrow_YYYYMMDD.ics     - Generated events (auto-created)
```

---

## 🎓 Why This Matters

**Google senior interviews expect adaptive thinking.**

This system:
- Trains you to self-assess
- Teaches you to adjust based on feedback
- Builds meta-learning skills
- Shows you data-driven decision making

**These are senior-level skills!**

---

## ✅ Success Metrics

You're using it effectively when:
- ✓ Calendar matches your actual pace
- ✓ Problems feel appropriately challenging
- ✓ You're not rushing or bored
- ✓ Progress is steady and sustainable
- ✓ System adapts when you struggle or excel

---

**Your learning is unique. Your calendar should be too.**

**Static schedules are for courses. Adaptive calendars are for mastery.** 📅
