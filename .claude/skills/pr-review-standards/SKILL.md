---
name: pr-review-standards
description: Google L5+ review standards for DSA solutions. Enforces optimal complexity, comprehensive testing, idiomatic Rust, and clear communication.
---

# PR Review Standards

## L5+ Quality Bar

Every solution must meet:

### ✅ PASS Criteria
- Optimal time/space complexity (with proof)
- All edge cases handled
- Idiomatic Rust (no unnecessary clones)
- Comprehensive tests
- Clear documentation

### 🔄 REVISE Criteria
- Works but sub-optimal
- Minor bugs or missing edge cases
- Code quality issues
- Incomplete testing

### ❌ FAIL Criteria
- Incorrect solution
- Extremely sub-optimal
- Can't explain approach
- No tests

## Review Process

1. **Correctness**: Does it work?
2. **Optimality**: Can it be better?
3. **Code Quality**: Is it clean and idiomatic?
4. **Communication**: Can you explain it?
5. **Testing**: All cases covered?

See [problem-solver/resources/review-standards.md](../problem-solver/resources/review-standards.md) for full details.

---

**Senior engineers ship quality code. Every time.**
