# Testing Strategies

## Comprehensive Test Coverage

### Edge Case Categories

1. **Size edge cases**:
   - Empty input: `[]`
   - Single element: `[1]`
   - Two elements: `[1, 2]`
   - Large input: Maximum constraints

2. **Value edge cases**:
   - All same: `[5, 5, 5, 5]`
   - All different: `[1, 2, 3, 4]`
   - Min/max values: `[i32::MIN, i32::MAX]`
   - Negative numbers: `[-5, -3, -1]`
   - Zero: `[0, 0, 0]`

3. **Order edge cases**:
   - Already sorted: `[1, 2, 3, 4]`
   - Reverse sorted: `[4, 3, 2, 1]`
   - Partially sorted: `[1, 3, 2, 4]`

4. **Special cases**:
   - No solution exists
   - Multiple solutions
   - Target at boundaries

### Test Template

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_from_problem() {
        assert_eq!(solution(vec![2, 7, 11, 15], 9), vec![0, 1]);
    }

    #[test]
    fn test_edge_empty() {
        assert_eq!(solution(vec![], 0), vec![]);
    }

    #[test]
    fn test_edge_single_element() {
        assert_eq!(solution(vec![1], 1), vec![]);
    }

    #[test]
    fn test_edge_two_elements() {
        assert_eq!(solution(vec![1, 2], 3), vec![0, 1]);
    }

    #[test]
    fn test_no_solution() {
        assert_eq!(solution(vec![1, 2, 3], 100), vec![]);
    }

    #[test]
    fn test_negative_numbers() {
        assert_eq!(solution(vec![-3, -1, 0, 2], -1), vec![1, 2]);
    }

    #[test]
    fn test_duplicates() {
        assert_eq!(solution(vec![3, 3], 6), vec![0, 1]);
    }

    #[test]
    fn test_large_input() {
        let nums = (0..10000).collect();
        assert!(solution(nums, 19999).len() == 2);
    }
}
```

### Property-Based Testing

```rust
#[cfg(test)]
mod property_tests {
    use super::*;

    #[test]
    fn property_result_sums_to_target() {
        let nums = vec![1, 2, 3, 4, 5];
        let target = 9;
        let result = two_sum(nums.clone(), target);

        if !result.is_empty() {
            let sum = nums[result[0] as usize] + nums[result[1] as usize];
            assert_eq!(sum, target);
        }
    }

    #[test]
    fn property_indices_in_bounds() {
        let nums = vec![1, 2, 3];
        let result = two_sum(nums.clone(), 5);

        for &idx in &result {
            assert!((idx as usize) < nums.len());
        }
    }
}
```

---

**Test thoroughly. L5+ candidates write comprehensive tests.**
