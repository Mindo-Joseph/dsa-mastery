---
name: dsa-problem-solver
description: Comprehensive DSA problem-solving skill for algorithm mastery. Activates when solving problems, analyzing patterns, proving complexity, or writing Rust solutions. Covers pattern recognition, first principles analysis, complexity proofs, testing strategies, and Google L5+ standards.
---

# DSA Problem Solver

## Purpose

Master data structures and algorithms through first principles, pattern recognition, and rigorous analysis. This skill guides you to **understand** solutions, not memorize them.

## When This Skill Activates

Automatically activates when:
- Working on algorithm problems or coding challenges
- Analyzing time/space complexity
- Identifying patterns (two pointers, sliding window, DP, etc.)
- Writing or reviewing Rust solutions
- Preparing for technical interviews
- Discussing algorithmic approaches

---

## Quick Start

### Solving a New Problem

**Step 1: Pattern Recognition** (<3 minutes)
- What category? (Array, Graph, String, etc.)
- What pattern? (Two Pointers, Sliding Window, DP, etc.)
- Similar problems solved before?

**Step 2: First Principles Analysis** (5-10 minutes)
- Why does this pattern work here?
- What property enables the optimization?
- What's the brute force? What's the bottleneck?

**Step 3: Solution Design** (15-20 minutes)
- Sketch approach
- Prove correctness
- Analyze complexity
- Consider edge cases

**Step 4: Implementation** (15-20 minutes)
- Write clean, idiomatic Rust
- Add comprehensive tests
- Document complexity

**Step 5: Review** (5-10 minutes)
- Is it optimal? Prove it.
- All edge cases covered?
- Ready for L5+ review?

**Total: ~60 minutes per problem**

---

## Core Principles

### 1. First Principles Over Memorization

❌ **Don't**: "Two pointers works on sorted arrays"
✅ **Do**: "Sorted arrays allow O(1) decisions to eliminate possibilities, enabling linear search instead of O(n²)"

### 2. Prove, Don't Guess

Every solution requires:
- Correctness proof (why it works)
- Complexity proof (tight bounds, not just upper)
- Edge case analysis (empty, single element, all same, etc.)

### 3. Optimal or Learn Why Not

- Always find the theoretical optimal first
- If your solution isn't optimal, understand the gap
- Sometimes optimal is impractical (constant factors matter)

### 4. L5+ Communication Standards

Google L5+ candidates must:
- Explain approach clearly before coding
- Justify design decisions
- Prove complexity rigorously
- Discuss trade-offs
- Handle follow-up questions

---

## Pattern Recognition Guide

See [resources/pattern-recognition.md](resources/pattern-recognition.md) for:
- 15 core patterns with visual guides
- When to use each pattern
- How to identify pattern from problem statement
- Pattern combinations

---

## Rust-Specific Guidance

See [resources/rust-patterns.md](resources/rust-patterns.md) for:
- Idiomatic Rust for algorithms
- Common pitfalls (unnecessary clones, borrowing issues)
- Iterator patterns for clean solutions
- Performance considerations

---

## Complexity Analysis

See [resources/complexity-analysis.md](resources/complexity-analysis.md) for:
- How to analyze time/space complexity
- Recurrence relations
- Amortized analysis
- Master theorem applications
- Common complexity patterns

---

## Testing Strategies

See [resources/testing-strategies.md](resources/testing-strategies.md) for:
- Edge case categories
- Test case generation
- Property-based testing
- Stress testing approaches

---

## Review Standards (Google L5+)

See [resources/review-standards.md](resources/review-standards.md) for:
- PASS ✅ criteria
- REVISE 🔄 criteria
- FAIL ❌ criteria
- Common mistakes to avoid

---

## Problem-Solving Workflow

### Phase 1: Understand (5 min)

```
1. Read problem carefully (2x)
2. Identify inputs, outputs, constraints
3. Work through examples manually
4. Ask clarifying questions
5. Restate problem in own words
```

### Phase 2: Pattern Recognition (3 min)

```
1. What data structure category? (Array, Graph, Tree, etc.)
2. What algorithmic pattern? (Two Pointers, DP, Binary Search, etc.)
3. Similar problems? (Query Gemini RAG for related problems)
4. Special properties? (Sorted, unique, constraints)
```

### Phase 3: Approach Design (10 min)

```
1. Brute force first - what's the naive approach?
2. Identify bottleneck - why is brute force slow?
3. Optimize - what property can we exploit?
4. Sketch algorithm - pseudocode or visual diagram
5. Prove correctness - why does it work?
6. Analyze complexity - tight bounds
```

### Phase 4: Implementation (20 min)

```
1. Write function signature
2. Handle edge cases first (empty, single element)
3. Implement core logic
4. Add complexity comments
5. Write comprehensive tests
```

### Phase 5: Review & Optimize (10 min)

```
1. Test with edge cases
2. Is it optimal? If not, why?
3. Any unnecessary operations?
4. Idiomatic Rust?
5. Ready for PR?
```

---

## Using Gemini RAG Integration

Query your curated books (CLRS, EPI, CTCI) for theory:

```
"Query Gemini: Explain dynamic programming from first principles"
"Query Gemini: Find similar problems to Two Sum"
"Query Gemini: What does CLRS say about graph traversal?"
```

See [gemini-rag-integration skill](../gemini-rag-integration/SKILL.md) for details.

---

## Common Patterns Quick Reference

| Pattern | When to Use | Time | Space |
|---------|-------------|------|-------|
| Two Pointers | Sorted array, pairs/triplets | O(n) | O(1) |
| Sliding Window | Subarray/substring problems | O(n) | O(1) |
| Binary Search | Sorted, find in O(log n) | O(log n) | O(1) |
| DFS/BFS | Graph/tree traversal | O(V+E) | O(V) |
| Dynamic Programming | Optimal substructure + overlapping | Varies | O(n) to O(n²) |
| Hash Table | Fast lookup, count frequency | O(n) | O(n) |
| Heap | Top K, priority queue | O(n log k) | O(k) |
| Union Find | Connected components | O(α(n)) | O(n) |

See [resources/pattern-recognition.md](resources/pattern-recognition.md) for full details.

---

## Complexity Cheat Sheet

**Array/String Operations:**
- Access by index: O(1)
- Linear scan: O(n)
- Nested loops: O(n²)
- Sorting: O(n log n)

**Hash Table:**
- Insert/Delete/Lookup: O(1) average, O(n) worst

**Binary Search:**
- Sorted array search: O(log n)

**Graph:**
- BFS/DFS: O(V + E)
- Dijkstra: O((V + E) log V)

**Dynamic Programming:**
- Memoization: O(states × work per state)
- Tabulation: O(states)

See [resources/complexity-analysis.md](resources/complexity-analysis.md) for proofs.

---

## Interview Communication Template

**1. Clarify (2 min)**
```
"Just to confirm, the input is a sorted array of integers?"
"Can the array have duplicates?"
"What's the constraint on n? Up to 10^5?"
```

**2. Approach (5 min)**
```
"I'll use two pointers here because the array is sorted.
Starting from both ends, if the sum is too large, I move the right pointer left.
If too small, I move left pointer right.
This works because moving the larger pointer when sum is too high
can only decrease the sum, which is what we need."
```

**3. Complexity (1 min)**
```
"Time: O(n) - we traverse the array once
Space: O(1) - only two pointers"
```

**4. Edge Cases (1 min)**
```
"I'll handle: empty array, single element, no solution exists,
multiple solutions (return first found)"
```

**5. Code (15 min)**
```rust
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    // Implementation
}
```

**6. Test (3 min)**
```
"Let me test with:
- [2,7,11,15], target=9 -> [0,1]
- [1,2,3], target=7 -> no solution
- [], target=0 -> no solution"
```

---

## Key Resources

Load these as needed during problem-solving:

- **[Pattern Recognition](resources/pattern-recognition.md)** - Identify which pattern to use
- **[Complexity Analysis](resources/complexity-analysis.md)** - Prove time/space bounds
- **[Rust Patterns](resources/rust-patterns.md)** - Write idiomatic Rust solutions
- **[Testing Strategies](resources/testing-strategies.md)** - Comprehensive test coverage
- **[Review Standards](resources/review-standards.md)** - L5+ quality bar

---

## Integration with Your Workflow

This skill works with:
- **Gemini RAG**: Query your books for theory
- **PR Review Standards**: Enforce L5+ quality
- **Test Validator Hook**: Ensure tests pass
- **Complexity Validator Hook**: Require complexity annotations

---

## Skill Activation Examples

This skill auto-suggests when you:

✅ "Solve: Two Sum II"
✅ "What pattern should I use for finding subarrays?"
✅ "Is this approach optimal?"
✅ "Analyze the complexity of this solution"
✅ Edit files in `src/patterns/`
✅ "Why does two pointers work here?"

---

**Master the patterns. Understand the principles. Achieve L5+.**
