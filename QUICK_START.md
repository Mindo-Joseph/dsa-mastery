# Quick Start Guide

## Setup (5 minutes)

### 1. Verify Installation
```bash
cd ~/dsa-mastery
ls -la  # Should see: patterns/, scripts/, progress/, etc.
```

### 2. Authenticate NotebookLM (One-Time)
In Claude Code, say:
```
"Set up NotebookLM authentication"
```
A browser will open → Log in with Google account

### 3. Add Your Notebooks
```
"Add my leetcode questions notebook to library: [YOUR-NOTEBOOKLM-URL]"
```

Claude will automatically query it to discover content, then add it.

Repeat for:
- Algorithm design books
- Architecture book
- Any other resources

### 4. Verify Notebooks
```
"Show my NotebookLM notebooks"
```

---

## Your First Problem (15 minutes)

### Step 1: Query for a Problem
```
"Query my leetcode notebook for an easy two-pointers problem"
```

I'll fetch it from NotebookLM and show you the problem.

### Step 2: Create Problem File
```
"Create a new problem file for this in the two-pointers pattern"
```

I'll generate: `patterns/two-pointers/[problem-name].py`

### Step 3: Solve Together

**Your turn:**
- Read the problem
- Think about approach (2-3 min)
- Try to code initial solution

**My turn:**
- Provide hints when stuck
- Help debug
- Optimize together
- Explain complexity

### Step 4: Test & Verify
```bash
cd ~/dsa-mastery
python patterns/two-pointers/[problem-name].py
```

Fix any failing tests together.

### Step 5: Log It
```bash
python scripts/log_progress.py log \
  "two-pointers" \
  "problem-name" \
  "easy" \
  "20" \
  "success"
```

### Step 6: View Progress
```bash
python scripts/log_progress.py stats
```

Congratulations! You've solved your first tracked problem!

---

## Daily Routine (60-90 min/day)

### Morning Check-in (5 min)
```bash
cd ~/dsa-mastery
python scripts/log_progress.py stats
python scripts/log_progress.py reviews
```

### Learn & Solve (70 min)

**If starting new pattern:**
1. Query theory from NotebookLM (5 min)
2. Implement template together (15 min)
3. Solve first problem (30 min)
4. Solve second problem (20 min)

**If continuing pattern:**
1. Quick theory review (2 min)
2. Solve problem 1 (30 min)
3. Solve problem 2 (35 min)

### Evening Commit (5 min)
```bash
git add .
git commit -m "Day X: [Pattern] - [N] problems"
python scripts/log_progress.py stats
```

---

## Common Commands

### NotebookLM Queries
```
"Query my [notebook-name] about [topic]"
"Ask my leetcode notebook for a [difficulty] [pattern] problem"
"Explain [concept] from my algorithm book"
"How does [algorithm] work architecturally?"
```

### Progress Tracking
```bash
# View dashboard
python scripts/log_progress.py stats

# Check reviews due
python scripts/log_progress.py reviews

# Log completed problem
python scripts/log_progress.py log [pattern] [problem] [difficulty] [minutes] [status]
```

### Git Workflow
```bash
# Daily commit
git status
git add .
git commit -m "Descriptive message"

# View history
git log --oneline -10
```

---

## Getting Help

### From Me (Claude)
```
"I'm stuck on [problem] - here's what I tried..."
"Why does this solution work?"
"What's the time complexity of this approach?"
"Generate test cases for this solution"
"Review my code for optimization"
```

### From NotebookLM
```
"Query my resources about [concept I don't understand]"
"Find similar problems to [problem name]"
"Explain the theory behind [algorithm]"
```

---

## Troubleshooting

### NotebookLM Not Working
```bash
# Check skill installation
ls ~/.claude/skills/notebooklm/

# Re-authenticate
```
Say: "Reset NotebookLM authentication"

### Scripts Not Working
```bash
# Make sure you're in the right directory
cd ~/dsa-mastery

# Check Python installed
python --version  # Should be 3.x
```

### Progress Not Saving
```bash
# Check progress directory exists
ls -la progress/

# Create if missing
mkdir -p progress
```

---

## Next Steps

1. **Right Now**: Complete "Your First Problem" above
2. **Today**: Solve 2 more problems in same pattern
3. **This Week**: Master your first pattern (Two Pointers)
4. **This Month**: Complete 3-4 patterns, 40+ problems

---

## Pro Tips

1. **Don't skip logging** - Data drives improvement
2. **Do reviews** - Spaced repetition is the secret
3. **Ask me questions** - I'm here to help you learn faster
4. **Query NotebookLM liberally** - It's your knowledge base
5. **Commit daily** - Git history = learning journal
6. **Time yourself** - Track improvement
7. **Explain solutions** - If you can't explain it, you don't understand it

---

Ready to start? Say:
```
"Let's start with Two Pointers - query my resources for theory"
```

Let's master DSA together!
