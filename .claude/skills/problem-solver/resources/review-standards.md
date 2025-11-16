# Review Standards (Google L5+)

## ✅ PASS - Interview Ready

**All criteria must be met:**

### 1. Correctness
- ✅ Handles all specified inputs correctly
- ✅ All edge cases considered (empty, single, duplicates, negatives, max values)
- ✅ No off-by-one errors
- ✅ No integer overflow/underflow issues

### 2. Optimal Complexity
- ✅ Time complexity is optimal (with proof)
- ✅ Space complexity is optimal or justified trade-off
- ✅ Cannot be improved without changing problem constraints
- ✅ Complexity documented with clear comments

### 3. Code Quality
- ✅ Idiomatic Rust (proper borrowing, no unnecessary clones)
- ✅ Clear variable names (not i, j, x, y unless standard)
- ✅ Proper structure (helper functions when needed)
- ✅ No code duplication

### 4. Communication
- ✅ Function has doc comments explaining approach
- ✅ Complexity documented: `/// Time: O(n), Space: O(1)`
- ✅ Non-obvious logic has inline comments
- ✅ Can explain WHY solution works (first principles)

### 5. Testing
- ✅ Comprehensive test coverage
- ✅ Edge cases tested
- ✅ All tests pass

### 6. Interview Performance
- ✅ Can explain approach before coding
- ✅ Can prove correctness
- ✅ Can analyze complexity rigorously
- ✅ Can handle follow-up questions

---

## 🔄 REVISE - Close, Needs Work

**One or more issues, but approach is sound:**

### Common REVISE Reasons

1. **Minor bugs**:
   - Off-by-one error
   - Missing edge case handling
   - Incorrect boundary condition

2. **Sub-optimal but works**:
   - O(n log n) when O(n) is possible
   - O(n) space when O(1) is possible
   - Correct but can be simplified

3. **Code quality issues**:
   - Too many unnecessary clones
   - Poor variable names
   - Logic can be simplified
   - Missing comments

4. **Incomplete testing**:
   - Basic tests only
   - Missing edge cases
   - No negative test cases

5. **Communication gaps**:
   - Can't explain why it works
   - Complexity analysis incomplete
   - Documentation missing

### Example REVISE Feedback

```
🔄 REVISE

Correctness: ✅ Works for all test cases
Complexity: ⚠️ O(n²) - can be optimized to O(n) using hash map

Suggested changes:
1. Replace nested loop with single pass + hash map
2. Add complexity proof in comments
3. Add test for large input (n=10000)

After these changes, this will be PASS quality.
```

---

## ❌ FAIL - Not Senior Level

**Fundamental issues that prevent passing:**

### Critical FAIL Reasons

1. **Incorrect solution**:
   - Produces wrong output
   - Fails basic test cases
   - Logic is fundamentally flawed

2. **Doesn't handle edge cases**:
   - Crashes on empty input
   - Fails on single element
   - Undefined behavior on edge cases

3. **Extremely sub-optimal**:
   - O(n³) when O(n) is standard
   - O(2^n) when O(n) is achievable
   - Brute force when pattern is obvious

4. **Can't explain approach**:
   - No understanding of why it works
   - Can't prove correctness
   - Can't analyze complexity

5. **Poor coding practices**:
   - Unreadable code
   - No structure
   - Massive code duplication

### Example FAIL Feedback

```
❌ FAIL

Issues:
1. Solution fails for empty array (crashes)
2. Time complexity is O(n³) - nested triple loop
   Standard solution is O(n) with hash map
3. No test cases written
4. Cannot explain why approach works

Recommendation:
- Study Two Pointers and Hash Table patterns
- Review first principles for this problem type
- Practice explaining approach before coding
- Resubmit after understanding the pattern
```

---

## Review Checklist

Before submitting for review:

- [ ] **Correctness**: All test cases pass
- [ ] **Optimal**: Time & space complexity are best possible
- [ ] **Complexity documented**: Clear comments with proof
- [ ] **Edge cases**: Empty, single, duplicates, negatives, max values
- [ ] **Clean code**: Idiomatic Rust, clear names, no duplication
- [ ] **Comments**: Doc comments + inline for non-obvious logic
- [ ] **Tests**: Comprehensive coverage including edge cases
- [ ] **Can explain**: Why it works, complexity proof, trade-offs

---

## Self-Review Questions

Ask yourself before submitting:

1. **Correctness**:
   - Does it work for all inputs?
   - What about empty input?
   - What about negative numbers?
   - What about max/min values?

2. **Optimality**:
   - Can I do better than O(n²)?
   - Can I reduce space from O(n) to O(1)?
   - Is there a pattern I'm missing?

3. **Code Quality**:
   - Would I want to review this code?
   - Are variable names clear?
   - Is logic easy to follow?
   - Any unnecessary complexity?

4. **Understanding**:
   - Can I explain WHY this works?
   - Can I prove the complexity?
   - Can I explain to a beginner?

---

**L5+ standard is high. Expect rigorous review. That's what makes you interview-ready.**
