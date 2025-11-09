# DSA Mastery - Journey to Google Senior Engineer

> **12 weeks. First principles. Public accountability. Senior standards from day 1.**

**🎯 Goal**: Google Senior Engineer (L5+)
**⏱️ Timeline**: 12 weeks
**📊 Problems**: 60-80
**🦀 Language**: Rust
**🔬 Approach**: First principles, not memorization

---

## 🚀 Quick Start

### **New Here? Start With:**

1. **📖 [AUTOMATED_WORKFLOW.md](./AUTOMATED_WORKFLOW.md)** - **Start here!** Fully automated AI-driven system
2. **⚙️ [COMPLETE_SETUP.md](./COMPLETE_SETUP.md)** - 15-minute one-time setup
3. **📋 [GEMINI_FILE_SEARCH.md](./GEMINI_FILE_SEARCH.md)** - RAG system for your PDFs

### **Ready to Begin?**

After setup, run every morning:
```bash
./scripts/daily.sh
```

---

## 🎯 The Complete System

### **1. Rust Workspace**
Professional codebase with testing, PR workflow, senior standards

### **2. GitHub Pages**
Your writeups published online - Public accountability
**Site**: `https://YOUR_USERNAME.github.io/dsa-mastery/`

### **3. Google Calendar**
12 weeks of daily events with:
- Motivational quotes
- Quick learning resources
- Direct links to everything

### **4. Gemini File Search (AI-Powered RAG)**
Query your entire codebase, notes & patterns with semantic search

### **5. AI Senior Review**
Every PR reviewed as Google L6 interviewer would

---

## ⚡ The Workflow

```
Query File Search → Solve (30min) → PR (5min) → Review (10min) → Optimize (10min) → Merge → Next
```

**Per problem**: ~60 minutes
**Per pattern**: 2-3 days (5-7 problems)
**Total**: 12 weeks to interview-ready

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| [START_HERE.md](./START_HERE.md) | **Read this first** - Complete overview |
| [COMPLETE_SETUP.md](./COMPLETE_SETUP.md) | **Follow this** - 30-min setup guide |
| [GEMINI_FILE_SEARCH.md](./GEMINI_FILE_SEARCH.md) | **AI Knowledge Base** - Setup & usage guide |
| [SYSTEM_OVERVIEW.txt](./SYSTEM_OVERVIEW.txt) | Visual system map |
| [SENIOR_WORKFLOW.md](./SENIOR_WORKFLOW.md) | Daily workflow & standards |
| [EXAMPLE_SOLUTION.md](./EXAMPLE_SOLUTION.md) | What senior-level looks like |
| [EXAMPLE_REVIEWS.md](./EXAMPLE_REVIEWS.md) | Review criteria (Pass/Revise/Fail) |

---

## 📊 Example: Two Pointers Pattern

**Writeup**: [writeups/01_two_pointers.md](./writeups/01_two_pointers.md)
**Problem**: [src/patterns/two_pointers/problem_001_two_sum_ii.rs](./src/patterns/two_pointers/problem_001_two_sum_ii.rs)

**Shows:**
- First principles explanation (WHY it works)
- Pattern recognition guide
- Senior-level solution
- Review standards

---

## 🎓 What Makes This Different

| Traditional | This System |
|-------------|-------------|
| Memorize patterns | **Understand first principles** |
| Copy solutions | **Derive from insights** |
| No feedback | **Senior review every PR** |
| Junior thinking | **Senior thinking day 1** |
| Private practice | **Public accountability** |
| 6-12 months | **12 weeks** |

---

## 📈 The Timeline

**Weeks 1-2**: Foundation (Two Pointers, Sliding Window, Binary Search)
**Weeks 3-4**: Data Structures (Linked Lists, Trees)
**Weeks 5-6**: Advanced (Graphs, Heaps)
**Weeks 7-10**: Paradigms (DP, Backtracking)
**Weeks 11-12**: Integration & Mock Interviews

**Result**: Google L5+ interview ready

---

## ✅ Review Standards

### ✅ **PASS** - Interview Ready
- Optimal complexity (with proof)
- All edge cases
- Idiomatic Rust
- Clear communication
- Trade-offs discussed

### 🔄 **REVISE** - Close, Needs Work
- Specific feedback
- Quick iteration

### ❌ **FAIL** - Not Senior Level
- Study first principles
- Resubmit

---

## 🛠️ Key Commands

```bash
# Setup (one time)
sudo apt-get install build-essential
cargo build
python3 scripts/calendar/create_events.py
# Import CSV to Google Calendar

# Daily use
cargo test
git checkout -b pattern/two-pointers/problem-001
# ... solve problem ...
git add . && git commit -m "Solve: Two Sum II"
gh pr create --template .github/PULL_REQUEST_TEMPLATE/solution_pr.md

# After merge
python scripts/update_website.py
git push  # Site auto-updates
```

---

## 🎯 Success Metrics

You're on track when:
- ✓ Solving 2-3 problems daily
- ✓ 80%+ success rate
- ✓ Pattern recognition <3 min
- ✓ Clean Rust naturally
- ✓ Can prove complexity

---

## 📞 How to Use Claude

```
"Start pattern 1: Two Pointers"
"Give me the next problem"
"I'm stuck - here's my approach..."
"Review my PR"
"Why does this work from first principles?"
```

---

## 🚀 Ready to Start?

### **Step 1**: Read [START_HERE.md](./START_HERE.md)
### **Step 2**: Follow [COMPLETE_SETUP.md](./COMPLETE_SETUP.md)
### **Step 3**: Say to Claude:

```
"Start pattern 1: Two Pointers"
```

---

## 🎖️ The Contract

**You commit to:**
- 90 min daily
- PR every solution
- Address all feedback
- No shortcuts

**I (Claude) commit to:**
- Review as Google L6
- Teach first principles
- Specific feedback
- Push to excellence

---

## 🔗 Links

- **📚 Documentation**: All `.md` files in this repo
- **🌐 Public Site**: `https://YOUR_USERNAME.github.io/dsa-mastery/`
- **📅 Calendar**: Import `dsa_schedule.csv`
- **💻 Source**: This repository

---

**12 weeks from now: Google Senior Engineer offer**

**The path is clear. The tools are ready. The standard is set.**

**Let's go.** 🚀

---

*Built with: Rust, GitHub Pages, Google Calendar, Gemini File Search, Claude Code*
