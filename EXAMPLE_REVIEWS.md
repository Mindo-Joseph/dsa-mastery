# Example PR Reviews at Different Levels

## Scenario 1: ✅ PASS - Senior Level (Merge Approved)

### Code Quality: Excellent
- Clean, idiomatic Rust with proper borrowing
- Clear variable names and logic flow
- Good use of `match` for comparison
- `unreachable!()` documents problem guarantee

### Correctness: Perfect
- All test cases pass
- Handles edge cases comprehensively
- Returns 1-indexed as required

### Complexity Analysis: Outstanding
- Time: O(n) - **Proved with amortized analysis** ✓
- Space: O(1) - Correctly identified ✓
- Alternative approaches discussed with trade-offs ✓

### Communication: Senior Level
- Clear PR description explaining approach
- Pattern recognition explicitly stated
- Trade-offs discussed (hash map vs two pointers)
- "Why" is explained, not just "what"

**Verdict: ✅ PASS**

**Feedback:**
> Excellent work. This is exactly what I'd expect in a Google senior interview:
> 1. Optimal solution with proof
> 2. Clean, production-quality code
> 3. Comprehensive testing
> 4. Clear communication of trade-offs
>
> **One minor note**: In production, you might want to return `Result<Vec<i32>, Error>` instead of `unreachable!()`, but for leetcode this is fine.
>
> **Ready to merge. Move to next problem.**

---

## Scenario 2: 🔄 REVISE - Close But Needs Work

```rust
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut i = 0;
    let mut j = numbers.len() - 1;

    loop {
        let s = numbers[i] + numbers[j];
        if s == target {
            return vec![(i + 1) as i32, (j + 1) as i32];
        } else if s < target {
            i += 1;
        } else {
            j -= 1;
        }
    }
}
```

**Verdict: 🔄 REVISE**

**Issues:**

1. **Ownership Problem**
   ```rust
   pub fn two_sum(numbers: Vec<i32>, target: i32)  // ❌ Takes ownership
   ```
   **Fix**: Use `&[i32]` - borrowing is more flexible
   ```rust
   pub fn two_sum(numbers: &[i32], target: i32)  // ✅
   ```

2. **Variable Names Not Clear**
   ```rust
   let mut i = 0;  // ❌ What is 'i'?
   let mut j = numbers.len() - 1;  // ❌ What is 'j'?
   let s = ...;  // ❌ What is 's'?
   ```
   **Fix**: Use descriptive names
   ```rust
   let mut left = 0;
   let mut right = numbers.len() - 1;
   let sum = ...;
   ```

3. **Infinite Loop Risk**
   ```rust
   loop {  // ❌ What if no solution?
   ```
   **Fix**: Use `while left < right` - makes termination explicit

4. **Missing Edge Case Handling**
   - What if `numbers` is empty?
   - Current code would panic on `numbers[i]`

5. **Complexity Analysis Missing**
   - No proof of O(n) time
   - No discussion of why this works

**Required Changes:**
1. Change signature to use slice
2. Rename variables
3. Use `while left < right` instead of `loop`
4. Add edge case tests
5. Write complexity analysis in PR description

**After fixes, ping me for re-review.**

---

## Scenario 3: ❌ FAIL - Not Senior Level

```rust
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    for i in 0..numbers.len() {
        for j in i+1..numbers.len() {
            if numbers[i] + numbers[j] == target {
                return vec![(i+1) as i32, (j+1) as i32];
            }
        }
    }
    vec![]
}
```

**Verdict: ❌ FAIL - Would Not Pass Google Interview**

**Critical Issues:**

1. **Wrong Complexity - O(n²)**
   - This is brute force, not two pointers pattern
   - For n=30,000: 900 million operations
   - **This would time out on large inputs**
   - **A senior engineer must recognize this immediately**

2. **Pattern Not Applied**
   - Problem explicitly requires constant space
   - You ignored the "sorted array" property
   - Two pointers pattern exists for exactly this reason

3. **No Complexity Analysis**
   - PR should state "Time: O(n²), Space: O(1)"
   - And then explain **why this is suboptimal**
   - And then provide the O(n) solution

4. **Interview Scenario**
   - Interviewer: "What's the time complexity?"
   - You: "O(n²)"
   - Interviewer: "Can you do better?"
   - **A senior should say "Yes, O(n) with two pointers" immediately**

**What You Need to Do:**

1. **Study the writeup** `writeups/01_two_pointers.md`
2. **Understand WHY** two pointers works
3. **Re-implement** using the pattern
4. **Prove** it's O(n) with amortized analysis
5. **Test** with large arrays to see performance difference

**This is a learning moment**: In a real interview, the brute force shows you don't recognize patterns. For a senior role, pattern recognition is mandatory.

**Go back, understand the first principles, and resubmit.**

---

## Scenario 4: 🔄 REVISE - Correct But Poor Communication

```rust
pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];
        if sum == target {
            return vec![(left + 1) as i32, (right + 1) as i32];
        } else if sum < target {
            left += 1;
        } else {
            right -= 1;
        }
    }
    vec![]
}
```

**Code:** ✅ Correct and optimal
**Tests:** ✅ Pass
**PR Description:** ❌ Empty or minimal

**Verdict: 🔄 REVISE**

**Issue: Communication**

In a Google interview, **explaining your solution is as important as the code itself**.

**PR description says:**
> "Solved the problem with two pointers"

**This is insufficient for senior level.**

**What's Missing:**

1. **Why two pointers?**
   - What property of the problem makes this work?
   - Why not hash map? Why not binary search?

2. **Complexity proof**
   - "It's O(n)" is not enough
   - **Prove it**: "Each pointer moves at most n times..."

3. **Trade-off analysis**
   - What did you consider?
   - Why is this optimal?

4. **Edge case discussion**
   - What could go wrong?
   - How did you handle it?

**Senior Engineer Standard:**

Your code shows you CAN solve it.
Your explanation shows you UNDERSTAND it.

**In interviews, they're testing both.**

**Required:**
Update PR description with:
- Approach explanation
- Complexity proof
- Alternative approaches considered
- Trade-offs

**Then ping for re-review.**

---

## Key Takeaway

### ✅ PASS Requires:
1. Optimal solution (complexity)
2. Clean code (Rust idioms)
3. Comprehensive tests (edge cases)
4. **Clear communication** (why, not just what)
5. Trade-off analysis (alternatives considered)

### All 5 Must Be Present

In a Google senior interview:
- Great code + poor explanation = **No hire**
- Good explanation + suboptimal code = **No hire**
- Both excellent = **Hire**

**This system trains both.**

---

## What Happens Next

### If ✅ PASS:
```bash
gh pr merge --squash
git checkout main
git pull
```
**Immediately move to next problem**

### If 🔄 REVISE:
1. Address all feedback
2. Push changes
3. Comment "@claude ready for re-review"
4. I review again (usually passes on 2nd try)

### If ❌ FAIL:
1. Study the writeup again
2. Understand first principles
3. Re-implement from scratch
4. Don't just copy - understand WHY

---

**This is how you get to Google senior level: Rigorous standards, fast iteration.**
