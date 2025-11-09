# Complete Setup Guide - Get Everything Running

**Time Required**: 20-30 minutes
**Result**: Fully operational DSA mastery system with public accountability

---

## ✅ Setup Checklist

### **Phase 1: System Setup (10 min)**

#### 1. Install Build Tools
```bash
sudo apt-get update
sudo apt-get install -y build-essential git python3 python3-pip
```

**Verify:**
```bash
gcc --version    # Should show version
git --version    # Should show version
python3 --version # Should show version
```

---

#### 2. Configure Git
```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify
git config --global --list
```

---

#### 3. Set up Rust
```bash
# Already installed, just activate
source "$HOME/.cargo/env"

# Verify
cargo --version
rustc --version
```

**Test build:**
```bash
cd ~/dsa-mastery
cargo build
cargo test
```

✅ **If builds successfully, Rust is ready!**

---

### **Phase 2: GitHub Setup (5 min)**

#### 4. Create GitHub Repository

**Option A: Via GitHub CLI** (Recommended)
```bash
# Install gh if needed
# sudo apt-get install gh

cd ~/dsa-mastery

# Login to GitHub
gh auth login

# Create repo
gh repo create dsa-mastery --public --source=. --remote=origin --push

# Enable GitHub Pages
gh api repos/:owner/dsa-mastery/pages \
  -X POST \
  -F source[branch]=main \
  -F source[path]=/docs
```

**Option B: Manual via GitHub.com**
1. Go to https://github.com/new
2. Repository name: `dsa-mastery`
3. Public repository
4. Don't initialize with README (we have one)
5. Create repository

Then:
```bash
cd ~/dsa-mastery
git remote add origin https://github.com/YOUR_USERNAME/dsa-mastery.git
git add -A
git commit -m "Initial commit: DSA Mastery System"
git push -u origin main
```

**Enable GitHub Pages:**
1. Go to repository → Settings → Pages
2. Source: Deploy from branch
3. Branch: `main`, Folder: `/docs`
4. Save

**Your site will be at:**
`https://YOUR_USERNAME.github.io/dsa-mastery/`

---

#### 5. Update Documentation URLs

Edit these files to replace `yourusername` with your GitHub username:

```bash
# In docs/index.md
sed -i 's/yourusername/YOUR_GITHUB_USERNAME/g' ~/dsa-mastery/docs/index.md

# In calendar script
sed -i 's/yourusername/YOUR_GITHUB_USERNAME/g' ~/dsa-mastery/scripts/calendar/create_events.py
```

**Or manually edit:**
- `docs/index.md` - Line with GitHub links
- `scripts/calendar/create_events.py` - URLs in description template

---

### **Phase 3: NotebookLM Setup (5 min)**

#### 6. Set up NotebookLM Skill

**Already installed at:** `~/.claude/skills/notebooklm/`

**Authenticate:**
```
"Set up NotebookLM authentication"
```

A Chrome window will open → Login with Google account.

**Add your notebooks:**
```
"Add my leetcode questions notebook to library: [YOUR_NOTEBOOKLM_URL]"
```

Claude will query it to discover content, then add it.

**Repeat for all notebooks:**
```
"Add my algorithm design book to library: [URL]"
"Add my architecture book to library: [URL]"
```

**Verify:**
```
"Show my NotebookLM notebooks"
```

You should see your library with all notebooks listed.

---

### **Phase 4: Google Calendar Integration (10 min)**

#### 7. Generate Your Schedule

```bash
cd ~/dsa-mastery

# Generate calendar events starting tomorrow at 9 AM
python3 scripts/calendar/create_events.py

# Or specify custom start date:
python3 scripts/calendar/create_events.py 2025-11-15
```

**This creates:**
- `schedule.json` - Full event data
- `dsa_schedule.csv` - Ready for Google Calendar import

---

#### 8. Import to Google Calendar

**Recommended: CSV Import (Fastest)**

1. Open https://calendar.google.com
2. Click ⚙️ Settings (top right)
3. Select "Import & Export" from left sidebar
4. Click "Select file from your computer"
5. Choose `dsa_schedule.csv`
6. Select calendar to import into (or create new "DSA Mastery")
7. Click "Import"

**Done!** All 12 weeks of events are now in your calendar.

---

#### 9. Customize Calendar Events (Optional)

Each event includes:
- 🎯 Pattern and problem for the day
- 💪 Motivational quote
- 🎓 Quick learning resources (videos/articles)
- 🔗 Direct links to writeups and repo
- ✅ Command to log completion

**You can:**
- Adjust times to fit your schedule
- Set custom reminders
- Add your own notes

---

### **Phase 5: Workflow Test (5 min)**

#### 10. Test the Complete System

**Start first pattern:**
```
"Start pattern 1: Two Pointers"
```

I will:
1. ✅ Query your NotebookLM for theory
2. ✅ Create writeup in `writeups/01_two_pointers.md`
3. ✅ Give you first problem
4. ✅ Wait for your solution

**You solve the problem**, then:

```bash
# Create branch
git checkout -b pattern/two-pointers/problem-001

# Edit file: src/patterns/two_pointers/problem_001_two_sum_ii.rs
# (Implement your solution)

# Test it
cargo test

# Commit & push
git add .
git commit -m "Solve: Two Sum II using Two Pointers"
git push origin pattern/two-pointers/problem-001

# Create PR
gh pr create --template .github/PULL_REQUEST_TEMPLATE/solution_pr.md
```

**I review your PR** with senior-level feedback.

**You iterate** based on feedback.

**Merge when optimal:**
```bash
gh pr merge --squash
git checkout main
git pull
```

**Update your public site:**
```bash
# Update progress in docs/index.md
git add docs/
git commit -m "Update progress: Solved Two Sum II"
git push

# GitHub Pages auto-updates in ~2 minutes
```

**Check your public site:**
`https://YOUR_USERNAME.github.io/dsa-mastery/`

---

## 🎯 Daily Workflow (After Setup)

### Morning (5 min)
1. Check Google Calendar event for today
2. Read the motivational quote
3. Quick skim of linked resources (optional)
4. Review pattern writeup if new pattern

### Deep Work (90 min)
1. Solve problem (30 min)
2. Create PR (5 min)
3. Get my review (10 min)
4. Optimize (10 min)
5. Merge & update docs (5 min)
6. Next problem or break

### Evening (2 min)
```bash
# Log your progress
python scripts/log_progress.py log pattern problem difficulty time status

# Commit & push
git add .
git commit -m "Day X: Pattern - N problems"
git push
```

**Your public site updates automatically!**

---

## 🚀 What You'll Have After Setup

### ✅ Local System
- Rust workspace with testing
- Pattern-based organization
- PR workflow with templates
- Progress tracking scripts

### ✅ Public Accountability
- GitHub Pages site showing progress
- Public writeups and solutions
- Commit history as learning journal

### ✅ NotebookLM Integration
- Query your curated resources
- Get theory from your books
- Problems from your collection

### ✅ Calendar Motivation
- Daily scheduled time
- Motivational quotes
- Quick learning resources
- Direct links to everything

### ✅ Senior-Level Review
- Every PR reviewed as Google L6 would
- Specific, actionable feedback
- No mercy, no shortcuts
- Iterate to perfection

---

## 📊 Success Metrics

You'll know setup is complete when:

- [ ] `cargo build` succeeds
- [ ] `cargo test` runs (even if 0 tests)
- [ ] GitHub repo is public
- [ ] GitHub Pages site is live
- [ ] NotebookLM authenticated and notebooks added
- [ ] Google Calendar has 12 weeks of events
- [ ] You can create and merge a test PR

---

## 🆘 Troubleshooting

### Rust Build Fails
```bash
# Install build tools
sudo apt-get install build-essential

# Verify
gcc --version
```

### GitHub Pages Not Showing
- Wait 2-5 minutes after enabling
- Check Settings → Pages for deployment status
- Make sure `docs/` folder is in main branch

### NotebookLM Not Working
```
"Reset NotebookLM authentication"
```
Then re-authenticate.

### Calendar Import Fails
- Make sure CSV is UTF-8 encoded
- Try importing 1 week at a time
- Or create events manually using schedule.json

---

## ⚡ Quick Start After Setup

Once everything is configured, starting each day is simple:

1. **Check calendar** - See today's pattern/problem
2. **Say:** "Give me today's problem"
3. **Solve → PR → Review → Optimize → Merge**
4. **Repeat**

---

## 📞 Ready to Start?

Complete the checklist above, then say:

**"Start pattern 1: Two Pointers"**

And we begin your journey to Google senior engineer.

---

**Time Investment:**
- Setup: 30 min (one time)
- Daily: 90 min (12 weeks)
- **Result**: Google L5+ offer

Worth it? Absolutely.

Let's go. 🚀
