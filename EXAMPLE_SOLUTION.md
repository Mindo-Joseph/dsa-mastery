# Example: What a Senior-Level Solution Looks Like

## The Code (Clean, Idiomatic Rust)

```rust
/// Solution for Two Sum II - Input Array Is Sorted
///
/// # Approach
/// Use two pointers starting at opposite ends of the sorted array.
/// - If sum < target: left pointer is too small, move it right
/// - If sum > target: right pointer is too large, move it left
/// - If sum == target: found the pair
///
/// The sorted property guarantees we can eliminate possibilities with each move.
///
/// # Complexity
/// - Time: O(n) - Each pointer moves at most n times, each move is O(1)
/// - Space: O(1) - Only two pointer variables used
///
/// # Pattern Applied
/// Two Pointers (Opposite Ends)
///
/// # Key Insights
/// Sorting allows us to make greedy decisions. When sum is too small,
/// we know moving left pointer right is the ONLY way to increase sum.
/// This eliminates checking all pairs with current left value.
pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];

        match sum.cmp(&target) {
            std::cmp::Ordering::Equal => {
                // Return 1-indexed positions
                return vec![(left + 1) as i32, (right + 1) as i32];
            }
            std::cmp::Ordering::Less => {
                // Sum too small, need larger left value
                left += 1;
            }
            std::cmp::Ordering::Greater => {
                // Sum too large, need smaller right value
                right -= 1;
            }
        }
    }

    // Problem guarantees solution exists, this is unreachable
    unreachable!("Problem guarantees exactly one solution")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(two_sum(&[2, 7, 11, 15], 9), vec![1, 2]);
    }

    #[test]
    fn test_example_2() {
        assert_eq!(two_sum(&[2, 3, 4], 6), vec![1, 3]);
    }

    #[test]
    fn test_example_3() {
        assert_eq!(two_sum(&[-1, 0], -1), vec![1, 2]);
    }

    #[test]
    fn test_two_elements() {
        assert_eq!(two_sum(&[1, 2], 3), vec![1, 2]);
    }

    #[test]
    fn test_negative_numbers() {
        assert_eq!(two_sum(&[-10, -5, 0, 5, 10], 0), vec![2, 4]);
    }

    #[test]
    fn test_duplicates() {
        assert_eq!(two_sum(&[1, 2, 2, 3], 4), vec![2, 4]);
    }

    #[test]
    fn test_large_array() {
        let numbers: Vec<i32> = (1..=1000).collect();
        assert_eq!(two_sum(&numbers, 1999), vec![999, 1000]);
    }

    #[test]
    fn test_boundaries() {
        assert_eq!(two_sum(&[-1000, 1000], 0), vec![1, 2]);
    }
}
```

## The PR Description (Shows Senior Thinking)

```markdown
## Problem
**LeetCode #167**: Two Sum II - Input Array Is Sorted
**Difficulty**: Easy
**Pattern**: Two Pointers (Opposite Ends)

---

## My Approach

### Pattern Recognition
- Sorted array + find pair = two pointers pattern
- Constraints allow O(n) solution
- Naive O(n²) would work but is suboptimal

### Solution Strategy
Use two pointers at opposite ends. Since array is sorted:
- If sum < target, left is too small → move left right
- If sum > target, right is too large → move right left
- This eliminates checking all pairs

### Why This Approach?
- **Time optimal**: O(n) is best possible (must examine elements)
- **Space optimal**: O(1) meets "constant extra space" requirement
- **Simple & clear**: Easy to understand and verify correctness

---

## Complexity Analysis

### Time Complexity: O(n)
**Proof**:
- Each pointer starts at an end
- Each iteration moves exactly one pointer
- Left moves right at most n times
- Right moves left at most n times
- Total moves ≤ 2n = O(n)

### Space Complexity: O(1)
**Proof**:
- Only two integer variables (left, right)
- Return vector is O(1) size (always 2 elements)
- No recursion stack

---

## Edge Cases Handled

- [x] Two elements (minimum valid input)
- [x] Negative numbers
- [x] Duplicate values
- [x] Large arrays (tested with 1000 elements)
- [x] Boundary values (-1000, 1000)
- [x] Sum at array ends
- [x] Sum in middle

---

## Alternative Approaches Considered

### Approach 1: Hash Map
- **Time**: O(n)
- **Space**: O(n)
- **Why not**: Uses O(n) space, violates "constant extra space" requirement

### Approach 2: Binary Search
- **Time**: O(n log n) - for each element, binary search for complement
- **Space**: O(1)
- **Why not**: Slower than two pointers, more complex

### Approach 3: Brute Force
- **Time**: O(n²)
- **Space**: O(1)
- **Why not**: Too slow for n = 30,000

---

## Rust-Specific Notes
- Used `&[i32]` slice instead of `Vec` for flexibility
- Used `cmp()` method for cleaner comparison logic
- `unreachable!()` documents problem guarantee
- All tests use inline data for clarity

---

## Questions for Review
1. Is the complexity analysis clear and rigorous?
2. Are there additional edge cases to consider?
3. Any Rust idioms I missed?

---

## Test Results
```
running 8 tests
test tests::test_boundaries ... ok
test tests::test_duplicates ... ok
test tests::test_example_1 ... ok
test tests::test_example_2 ... ok
test tests::test_example_3 ... ok
test tests::test_large_array ... ok
test tests::test_negative_numbers ... ok
test tests::test_two_elements ... ok

test result: ok. 8 passed
```

**Ready for senior-level review** ✓
```

---

This is what I expect in EVERY PR. Senior-level communication.
