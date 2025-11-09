# Fully Automated DSA Mastery Workflow

**Vision: AI-driven, minimal manual work, maximum learning**

---

## 🎯 Your Complete System

```
1. Gemini RAG → Queries YOUR PDFs (books, LeetCode problems)
2. AI generates writeup → Pushes to Google Docs (formatted)
3. You read, add personal notes in Google Docs
4. AI fetches problems from YOUR LeetCode PDF
5. You solve in Rust → Submit PR
6. Auto-test with cargo
7. Request Manim visualization if needed
8. Repeat
```

---

## ⚡ Daily Workflow (Ultra Simple)

### Every Morning: Run ONE Command

```bash
./scripts/daily.sh
```

**What it does:**
1. ✅ Queries YOUR uploaded PDFs (CLRS, EPI, LeetCode, etc.)
2. ✅ Generates complete writeup using Gemini RAG
3. ✅ Formats and saves to Google Docs
4. ✅ Fetches 5-7 problems from YOUR LeetCode PDF
5. ✅ Saves problem list

**Output:**
- Writeup in Google Docs (link in `GOOGLE_DOCS_LINKS.md`)
- Problem list in `daily-problems/`
- You're ready to learn!

---

### Read & Edit (30 min)

```bash
# Open Google Doc (bookmark this URL)
open "https://docs.google.com/document/d/YOUR_DOC_ID/edit"
```

**In Google Docs:**
- ✅ Read AI-generated writeup (from YOUR sources)
- ✅ Add your personal insights: "What clicked for me..."
- ✅ Add notes, comments, highlight confusing parts
- ✅ Auto-saves, accessible on phone/tablet

---

### Solve Problems (2-3 hours)

```bash
# Check today's problems
cat daily-problems/<pattern>_problems.md

# Solve in Rust
# Create file: src/patterns/<pattern>/problem_001.rs
# Write solution + tests

# Test locally
cargo test --lib problem_001

# Submit when ready
./scripts/submit.sh src/patterns/<pattern>/problem_001.rs
```

**What `submit.sh` does:**
1. ✅ Runs cargo tests
2. ✅ Creates git branch
3. ✅ Commits your solution
4. ✅ Creates PR automatically
5. ✅ Ready for review

---

### Optional: Visualize (5 min)

```bash
# Generate Manim animation of your solution
./scripts/visualize.sh src/patterns/two_pointers/problem_001.rs "[1,2,3,4,5]" 6

# Opens MP4 video showing step-by-step execution
```

**What you see:**
- Pointers moving through array
- Variables changing
- Stack frames for recursion
- Why O(n) vs O(n²) matters

---

### End of Day: Sync (30 sec)

```bash
# Pull your Google Docs edits back to repo
python3 scripts/gdocs_sync/pull_from_docs.py

# Commit
git add .
git commit -m "Day X: Pattern mastery + insights"
git push
```

Done! Repeat tomorrow.

---

## 📅 Complete Example: Day 1

### Morning (5 min)

```bash
# Run daily automation
./scripts/daily.sh
```

**Output:**
```
========================================
🚀 DAILY DSA MASTERY - AUTOMATED
========================================

📚 Querying books for first principles...
✅ Theory from 3 sources (CLRS, EPI, CTCI)

💻 Querying for implementation patterns...
✅ Implementation guide generated

📝 Fetching example problems...
✅ 7 problems found

🎯 Gathering interview insights...
✅ Interview tips compiled

✅ Writeup saved: writeups/two_pointers.md
📤 Pushed to Google Docs

🔍 Fetching 7 problems for Two Pointers...
✅ Problems saved: daily-problems/two_pointers_problems.md

========================================
✅ DAILY SETUP COMPLETE
========================================
```

### Read & Learn (30 min)

```bash
# Open Google Doc
open "$(grep -o 'https://[^"]*' GOOGLE_DOCS_LINKS.md | head -1)"
```

**In Google Docs, you see:**
- AI-generated writeup from YOUR books
- First principles explanation
- Pattern recognition guide
- Implementation template
- Interview tips

**You add:**
- Personal notes: "Aha! The key insight is..."
- Comments: "Review this before interview"
- Examples that helped you understand

### Solve Problem 1 (45 min)

```bash
# Check problem list
cat daily-problems/two_pointers_problems.md
```

**You see:**
```markdown
# Problems for Two Pointers

## Easy: Two Sum II (LC 167)
Given sorted array, find two numbers that sum to target.
Input: [2,7,11,15], target=9
Expected: [0,1]
...
```

**Solve:**
```rust
// Create: src/patterns/two_pointers/problem_001_two_sum_ii.rs

pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];
        if sum == target {
            return vec![left as i32, right as i32];
        } else if sum < target {
            left += 1;
        } else {
            right -= 1;
        }
    }

    vec![]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_two_sum() {
        assert_eq!(two_sum(vec![2,7,11,15], 9), vec![0,1]);
    }
}
```

**Test:**
```bash
cargo test --lib problem_001_two_sum_ii
```

**Submit:**
```bash
./scripts/submit.sh src/patterns/two_pointers/problem_001_two_sum_ii.rs
```

### Review & Merge (10 min)

PR created automatically. I (Claude) review:

```
✅ PASS - Senior Level

**Correctness**: ✅ Handles all cases
**Complexity**: ✅ O(n) time, O(1) space - optimal
**Code Quality**: ✅ Clean, idiomatic Rust
**Edge Cases**: Consider empty array

Minor suggestion: Add edge case test for empty array.
Otherwise excellent! Merge when ready.
```

You push update:
```rust
#[test]
fn test_empty() {
    assert_eq!(two_sum(vec![], 0), vec![]);
}
```

Merge PR. Move to problem 2.

### Evening: Sync (1 min)

```bash
# Pull Google Docs changes
python3 scripts/gdocs_sync/pull_from_docs.py

# Commit everything
git add .
git commit -m "Day 1: Two Pointers - 2 problems solved + insights"
git push
```

**Day 1 complete!** 🎉

---

## 🗂️ File Organization

```
~/dsa-materials/           # NOT in git
├── books/
│   ├── clrs.pdf
│   ├── elements-of-programming-interviews.pdf
│   └── cracking-coding-interview.pdf
└── problem-sets/
    └── leetcode-premium.pdf

~/dsa-mastery/             # Git repo
├── scripts/
│   ├── daily.sh           ← Run every morning
│   ├── submit.sh          ← Submit solutions
│   ├── visualize.sh       ← Generate Manim videos
│   ├── daily_automation.py
│   └── gemini_file_search.py
├── daily-problems/        # AI-generated problem lists
├── writeups/              # Markdown (synced from Google Docs)
├── src/patterns/          # Your Rust solutions
└── visualizations/        # Manim MP4 videos
```

**Google Docs (cloud):**
- Source of truth for writeups
- You edit here
- Sync back to repo

**Gemini Cloud:**
- Your PDFs indexed
- Query anytime via RAG
- Costs ~$1/month

---

## 🔄 What's Automated vs Manual

### ✅ Fully Automated
- Daily writeup generation (queries YOUR PDFs)
- Problem fetching from YOUR LeetCode PDF
- Google Docs formatting
- PR creation
- Test running
- Manim visualization generation

### ✍️ Your Work (The Learning!)
- Read writeup, add personal insights
- Solve problems in Rust
- Review feedback, iterate
- Build deep understanding

---

## 🎓 12-Week Timeline

**Week 1-2**: Foundation (Two Pointers, Sliding Window, Binary Search)
**Week 3-4**: Data Structures (Trees, Linked Lists, Heaps)
**Week 5-6**: Advanced (Graphs, Union Find)
**Week 7-10**: Paradigms (DP, Backtracking, Greedy)
**Week 11-12**: Integration & Mocks

**Each day:**
1. Run `./scripts/daily.sh` (5 min)
2. Read + edit Google Docs (30 min)
3. Solve 2-3 problems (2-3 hours)
4. Visualize if confused (5 min)
5. Sync changes (1 min)

**Total daily time**: 3-4 hours
**Result after 12 weeks**: Google L5+ ready

---

## 🛠️ Setup (One-Time, 15 min)

### 1. Store PDFs

```bash
mkdir -p ~/dsa-materials/books
mkdir -p ~/dsa-materials/problem-sets

# Move your PDFs there
mv ~/Downloads/*.pdf ~/dsa-materials/books/
```

### 2. Setup Gemini File Search

```bash
# Get API key: https://aistudio.google.com/apikey
export GEMINI_API_KEY='your-key'
echo 'export GEMINI_API_KEY="your-key"' >> ~/.bashrc

cd ~/dsa-mastery
./scripts/setup_gemini_search.sh

# Upload PDFs (one-time)
python3 scripts/gemini_file_search.py upload --dir ~/dsa-materials/books
```

### 3. Setup Google Docs (if not done)

```bash
cd ~/dsa-mastery/scripts/gdocs_sync
# Follow README.md for OAuth credentials
python3 setup_initial_docs.py
```

### 4. Install Manim (for visualizations)

```bash
sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev
pip3 install manim
```

**Done!** System ready.

---

## 💡 Pro Tips

### Morning Routine
```bash
# Bookmark this command
alias dsa='cd ~/dsa-mastery && ./scripts/daily.sh'

# Every morning:
dsa
```

### Quick Visualization
```bash
# Create alias
alias viz='~/dsa-mastery/scripts/visualize.sh'

# Use it:
viz src/patterns/two_pointers/problem_001.rs "[1,2,3]" 6
```

### Mobile Editing
- Install Google Docs app
- Add insights while commuting
- Auto-syncs when you run `pull_from_docs.py`

### Share with Mentors
- Share Google Docs link
- They can comment inline
- You see feedback immediately

---

## 📊 Success Metrics

Track your progress:

```bash
# Problems solved
git log --oneline --grep="Solve:" | wc -l

# Patterns completed
ls src/patterns/ | wc -l

# Writeups published
ls writeups/*.md | wc -l

# Visualizations created
ls visualizations/*.mp4 | wc -l
```

**You're on track when:**
- ✅ Solving 2-3 problems daily
- ✅ 80%+ pass rate on first try
- ✅ Can explain complexity clearly
- ✅ Recognize patterns in <3 min

---

## 🚀 Start Now

```bash
# 1. Setup (15 min, one-time)
export GEMINI_API_KEY='your-key'
./scripts/setup_gemini_search.sh
python3 scripts/gemini_file_search.py upload --dir ~/dsa-materials/books

# 2. Run first day
./scripts/daily.sh

# 3. Read Google Doc, start solving
```

**12 weeks from now: Google Senior Engineer**

**Let's go!** 🚀
