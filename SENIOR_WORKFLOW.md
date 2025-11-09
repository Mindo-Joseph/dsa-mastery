# Senior Engineering Interview Prep - Workflow

**Goal**: Join Google as a Senior Engineer
**Standard**: Every solution must meet senior-level expectations
**Efficiency**: 2-3 days per pattern, 60-90 min per problem

---

## The Optimized Loop

```
Pattern Study (30min) → Solve 5-7 Problems (5-7 days) → Next Pattern
```

### Per Pattern (2-3 days):

#### Day 1: Pattern Mastery
1. **Query NotebookLM** (10 min)
   ```
   "Query my algorithm design book about [PATTERN]:
   - First principles: WHY does this work?
   - When to recognize this pattern
   - Time/space complexity fundamentals
   - Common variations"
   ```

2. **I Create Writeup** (15 min)
   - First principles explanation
   - Pattern recognition guide
   - Rust implementation template
   - Complexity analysis framework
   - Senior-level insights

3. **You implement pattern template** (20 min)
   - In `src/patterns/<pattern>/mod.rs`
   - Generic, reusable code
   - Fully documented

4. **Get problem set** (5 min)
   ```
   "Query my leetcode notebook for 5-7 problems for [PATTERN]:
   - 2 easy (warm-up)
   - 3 medium (core)
   - 2 hard (stretch)"
   ```

#### Day 2-3: Problem Solving

**Per Problem (45-60 min):**

1. **Solve** (30-40 min)
   - Identify pattern
   - Plan approach
   - Implement in Rust
   - Write tests
   - Analyze complexity

2. **Create PR** (5 min)
   ```bash
   git checkout -b pattern/<pattern>/problem-<number>
   git add src/patterns/<pattern>/<problem>.rs
   git commit -m "Solve: <Problem Title> using <Pattern>"
   git push origin pattern/<pattern>/problem-<number>

   # Create PR using template
   gh pr create --template solution_pr.md
   ```

3. **I Review as Google Senior Interviewer** (10 min)
   - Correctness: Edge cases? Off-by-one?
   - Complexity: Optimal? Can you prove it?
   - Code quality: Idiomatic Rust? Clean?
   - Communication: Clear explanation?
   - **Pass/Revise/Fail** with specific feedback

4. **You optimize** (5-10 min)
   - Address feedback
   - Push changes
   - I re-review

5. **Merge when optimal** (1 min)
   ```bash
   gh pr merge --squash
   git checkout main
   git pull
   ```

6. **Next problem immediately**

---

## My Review Rubric (Senior Engineer Standard)

### ✅ **PASS** - Ready for Google L5+
- Optimal time/space complexity
- Handles all edge cases elegantly
- Idiomatic, clean Rust code
- Clear complexity analysis with proof
- Considered trade-offs explicitly

### 🔄 **REVISE** - Close, needs refinement
- Suboptimal but working solution
- Missing edge cases
- Complexity analysis incomplete
- Code is correct but not clean
- Can be improved with hints

### ❌ **FAIL** - Not senior level
- Incorrect solution
- Doesn't handle basic edge cases
- Wrong complexity analysis
- No understanding of trade-offs
- Would not pass Google interview

---

## What I Look For (Senior Level)

### 1. Problem-Solving Approach
**Junior**: "I'll try this and see if it works"
**Senior**: "Given constraints N ≤ 10^5, O(n²) won't work. Need O(n log n) or O(n). This looks like sliding window because..."

### 2. Code Quality
**Junior**: Works but messy
**Senior**: Clean, idiomatic, self-documenting

**Example**:
```rust
// Junior
fn solve(v: Vec<i32>) -> i32 {
    let mut r = 0;
    for i in 0..v.len() {
        // ... 20 lines of nested logic
    }
    r
}

// Senior
fn max_subarray_sum(nums: &[i32], k: usize) -> i32 {
    nums.windows(k)
        .map(|window| window.iter().sum())
        .max()
        .unwrap_or(0)
}
```

### 3. Complexity Analysis
**Junior**: "I think it's O(n)"
**Senior**: "Time: O(n) because we visit each element once. Space: O(k) for the window state. Trade-off: We could do O(1) space with two pointers but code clarity suffers. For interview, clarity wins."

### 4. Edge Cases
**Junior**: Tests happy path only
**Senior**:
- Empty input
- Single element
- All same elements
- Duplicates
- Boundaries (min/max values)
- Integer overflow potential

### 5. Communication
**Junior**: Just submits code
**Senior**: PR description explains:
- Pattern recognition process
- Why this approach over alternatives
- Complexity with proof
- Trade-offs made
- Production considerations

---

## Rust-Specific Senior Expectations

### Ownership & Borrowing
```rust
// Junior: Unnecessary clones
fn process(nums: Vec<i32>) -> i32 {
    let copy = nums.clone(); // Why?
    helper(&copy)
}

// Senior: Appropriate borrowing
fn process(nums: &[i32]) -> i32 {
    helper(nums)
}
```

### Iterators over Indexing
```rust
// Junior: Manual indexing
for i in 0..arr.len() {
    sum += arr[i];
}

// Senior: Idiomatic iterators
let sum: i32 = arr.iter().sum();
```

### Error Handling
```rust
// Junior: panic! or unwrap everywhere
let val = arr[idx]; // Might panic!

// Senior: Explicit handling
let val = arr.get(idx).ok_or("Index out of bounds")?;
```

---

## Efficiency Rules

### DO:
- ✅ Move fast - 5-7 problems per pattern
- ✅ Iterate quickly on feedback
- ✅ Query NotebookLM liberally
- ✅ Ask me questions when stuck >15 min
- ✅ Focus on understanding WHY, not memorizing

### DON'T:
- ❌ Spend >2 days on one pattern
- ❌ Dwell on failed approaches >20 min
- ❌ Skip the PR process (it's the learning!)
- ❌ Ignore feedback - every comment matters
- ❌ Memorize solutions - understand principles

---

## Progress Tracking

```bash
# After each problem
cargo test --package dsa_mastery --lib patterns::<pattern>

# View your stats
git log --oneline --grep="Solve:" | wc -l  # Problems solved
gh pr list --state merged | wc -l          # Merged solutions

# Pattern completion
ls src/patterns/*/  # See what you've built
```

---

## Timeline to Google Senior Offer

**Week 1-2**: Master 3 easy patterns
- Two Pointers
- Sliding Window
- Binary Search
- **Goal**: Pattern recognition fast, clean Rust code

**Week 3-4**: Data structure patterns
- Fast/Slow Pointers
- Linked List In-place Reversal
- Tree BFS/DFS
- **Goal**: Optimal solutions first try, clear complexity analysis

**Week 5-6**: Advanced structures
- Graphs (BFS/DFS/Topological/Union-Find)
- Heaps
- **Goal**: Handle complex problems, consider trade-offs

**Week 7-10**: Problem-solving paradigms
- Dynamic Programming (2 weeks - most important!)
- Backtracking
- **Goal**: Senior-level optimization, multiple approaches

**Week 11-12**: Integration & Mock Interviews
- Mixed pattern problems
- System design integration
- **Goal**: Interview ready, confident

---

## Next Steps

1. **Right now**: Set up NotebookLM
   ```
   "Set up NotebookLM authentication"
   "Add my leetcode notebook: [URL]"
   "Add my algorithm design book: [URL]"
   ```

2. **In 5 minutes**: Start first pattern
   ```
   "Let's start Two Pointers. Query my resources for first principles
   explanation, then create the writeup."
   ```

3. **In 30 minutes**: Solve first problem
   ```
   "Get me an easy two-pointers problem from my leetcode notebook"
   ```

4. **In 60 minutes**: Submit first PR for review

5. **In 90 minutes**: Iterate on feedback, merge, next problem

---

## The Contract

**You commit to:**
- Solve 2-3 problems daily
- Create PR for every solution
- Address all feedback quickly
- Track progress religiously

**I commit to:**
- Review every PR as a Google L6 interviewer would
- Provide specific, actionable feedback
- Help you understand first principles
- Push you to senior-level thinking
- Be efficient - no wasted time

---

**Let's build your path to Google. Ready to start?**

Say: "Start pattern 1: Two Pointers"
