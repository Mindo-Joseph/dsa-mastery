# Complete Daily Workflow

## 🌅 Morning Routine (5 min)

### Step 1: Generate Daily Content

```bash
cd ~/dsa-mastery
source ~/.venv/bin/activate
export GEMINI_API_KEY='AIzaSyAYYc7FtOnneziaD7xHtvMIigO8FrUzswI'

./scripts/daily.sh
```

**Output:**
- ✅ New writeup in `writeups/`
- ✅ Problem list in `daily-problems/`
- ✅ Progress tracked

---

## 📚 Step 2: Read & Study (30 min)

### Read the Writeup

```bash
# View locally
cat writeups/two_pointers.md

# Or view on GitHub Pages
open https://mindo-joseph.github.io/dsa-mastery/patterns/two-pointers.html
```

**What to focus on:**
- ✅ First principles - WHY the pattern exists
- ✅ Key insight that makes it work
- ✅ Time/space complexity
- ✅ When to recognize the pattern

**Take notes:**
- Aha moments
- Confusing parts
- Questions

---

## 🎯 Step 3: Get Problems (2 min)

### Option A: From Generated List

```bash
# Check problem list generated this morning
cat daily-problems/two_pointers_problems.md
```

### Option B: Query for More

```bash
# Ask Gemini RAG for specific problems
python3 scripts/gemini_rag.py query --question "Give me an easy two pointers problem for beginners with test cases"
```

**Pick your first problem** (start with Easy)

---

## 💻 Step 4: Solve the Problem (30-45 min)

### Create Solution File

```bash
# Create branch
git checkout -b two-pointers/problem-001

# Create solution file
mkdir -p src/patterns/two_pointers
touch src/patterns/two_pointers/problem_001_two_sum_ii.rs
```

### Write Your Solution

```rust
// src/patterns/two_pointers/problem_001_two_sum_ii.rs

/// Problem: Two Sum II - Input Array Is Sorted
/// Given a 1-indexed array of integers that is sorted in ascending order,
/// find two numbers such that they add up to a target.
///
/// Example:
/// Input: numbers = [2,7,11,15], target = 9
/// Output: [1,2]
/// Explanation: The sum of 2 and 7 is 9. Return indices 1 and 2.

pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];

        if sum == target {
            // 1-indexed
            return vec![left as i32 + 1, right as i32 + 1];
        } else if sum < target {
            left += 1;
        } else {
            right -= 1;
        }
    }

    vec![] // No solution
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(two_sum(vec![2,7,11,15], 9), vec![1,2]);
    }

    #[test]
    fn test_example_2() {
        assert_eq!(two_sum(vec![2,3,4], 6), vec![1,3]);
    }

    #[test]
    fn test_negative_numbers() {
        assert_eq!(two_sum(vec![-1,0], -1), vec![1,2]);
    }

    #[test]
    fn test_two_elements() {
        assert_eq!(two_sum(vec![1,2], 3), vec![1,2]);
    }
}
```

### Add to lib.rs

```bash
# Add module to src/lib.rs
echo "pub mod patterns { pub mod two_pointers { pub mod problem_001_two_sum_ii; } }" >> src/lib.rs
```

---

## 🧪 Step 5: Test Locally (5 min)

```bash
# Run tests
cargo test problem_001_two_sum_ii

# Expected output:
# running 4 tests
# test tests::test_example_1 ... ok
# test tests::test_example_2 ... ok
# test tests::test_negative_numbers ... ok
# test tests::test_two_elements ... ok
```

**If tests fail:**
- Debug
- Fix
- Repeat

---

## 📤 Step 6: Submit for Review (2 min)

```bash
./scripts/submit.sh src/patterns/two_pointers/problem_001_two_sum_ii.rs
```

**What happens:**
1. ✅ Runs all tests
2. ✅ Creates git branch (if needed)
3. ✅ Commits code
4. ✅ Pushes to GitHub
5. ✅ Creates pull request

**PR Template includes:**
- Problem description
- Your approach
- Complexity analysis
- Test results

---

## 👀 Step 7: Get Review (5 min)

**I (Claude) review your PR as Google L6 interviewer:**

### ✅ **PASS** Criteria:
- Optimal time/space complexity
- All edge cases handled
- Clean, idiomatic Rust
- Clear explanation

### 🔄 **REVISE** Criteria:
- Works but suboptimal
- Missing edge cases
- Code quality issues

### ❌ **FAIL** Criteria:
- Incorrect solution
- Wrong complexity
- Major issues

**You get feedback like:**

```
🔍 Review: Two Sum II

Correctness: ✅ Handles all cases
Complexity: ✅ O(n) time, O(1) space - optimal
Code Quality: ✅ Clean and idiomatic

Minor suggestions:
- Add doc comment explaining WHY two pointers works here
- Consider overflow: what if numbers[left] + numbers[right] > i32::MAX?

Overall: ✅ PASS - Merge when ready!
```

---

## 🔄 Step 8: Iterate (Optional, 5-10 min)

**If revisions needed:**

```bash
# Make changes
vim src/patterns/two_pointers/problem_001_two_sum_ii.rs

# Test again
cargo test problem_001_two_sum_ii

# Commit
git add .
git commit -m "Address review feedback"
git push
```

---

## ✅ Step 9: Merge & Publish (1 min)

```bash
# Merge PR on GitHub
gh pr merge --squash

# Pull latest
git checkout master
git pull

# Optional: Visualize your solution
./scripts/visualize.sh src/patterns/two_pointers/problem_001_two_sum_ii.rs "[2,7,11,15]" 9

# Opens Manim animation showing step-by-step execution
```

---

## 🔁 Step 10: Next Problem

**Repeat Steps 3-9 for next problem!**

Target: **2-3 problems per day**

---

## 📊 Track Progress

```bash
# Check stats
git log --oneline --grep="Solve:" | wc -l  # Problems solved

# Update progress
python3 scripts/log_progress.py

# Publish to GitHub Pages
python3 scripts/publish_to_pages.py

git add docs/
git commit -m "Update progress"
git push
```

---

## 🎯 Daily Goals

**Minimum:** 1 problem solved, tested, reviewed, merged
**Target:** 2-3 problems
**Stretch:** Complete pattern (5-7 problems)

---

## 📅 Example: Complete Day 1

```bash
# 9:00 AM - Generate content
./scripts/daily.sh

# 9:05 AM - Read writeup (on GitHub Pages)
open https://mindo-joseph.github.io/dsa-mastery/patterns/two-pointers.html

# 9:35 AM - Start first problem
git checkout -b two-pointers/valid-palindrome
# ... solve ...
cargo test
./scripts/submit.sh src/patterns/two_pointers/problem_001.rs

# 10:30 AM - Iterate on feedback
# ... fix issues ...
gh pr merge --squash

# 11:00 AM - Start second problem
git checkout -b two-pointers/two-sum-ii
# ... solve ...
cargo test
./scripts/submit.sh src/patterns/two_pointers/problem_002.rs

# 12:00 PM - Done! 2 problems solved
```

---

## 🔥 Tips

### When Stuck (>15 min)

```bash
# Query Gemini for hints
python3 scripts/gemini_rag.py query --question "Hints for solving [problem name] using two pointers"

# Or ask me (Claude)
"I'm stuck on problem X. Here's my approach: ... What am I missing?"
```

### Visualize Complex Solutions

```bash
# Generate animation
./scripts/visualize.sh src/patterns/two_pointers/problem_003.rs "[1,2,3,4,5]" 6

# Watch the MP4 to understand execution flow
```

### Weekend Deep Dive

```bash
# Query for pattern variations
python3 scripts/gemini_rag.py query --question "What are advanced variations of two pointers? Provide examples."

# Practice more problems
# Update writeup with your insights
```

---

## 🎖️ Week 1 Milestone

**By end of Week 1:**
- ✅ Two Pointers: 7 problems
- ✅ Sliding Window: 7 problems
- ✅ First principles understood
- ✅ Can recognize patterns in <3 min
- ✅ Solutions are O(n) optimal

**Then move to Week 2 patterns!**

---

## 🚀 Summary

```
Daily: Generate → Read → Solve → Test → Submit → Review → Merge → Repeat
Weekly: Complete pattern (5-7 problems) → Publish → Next pattern
Monthly: Review all patterns → Mock interviews → Identify weak areas
```

**12 weeks = Interview ready!** 🎯
