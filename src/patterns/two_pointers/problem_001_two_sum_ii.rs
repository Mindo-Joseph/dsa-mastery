/*
LeetCode #167: Two Sum II - Input Array Is Sorted
Difficulty: Easy
Pattern: Two Pointers (Opposite Ends)

Problem Statement:
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one to return 1-indexed positions.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Examples:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order
- -1000 <= target <= 2000
- The tests are generated such that there is exactly one solution

---

YOUR TASK:
1. Implement the solution below
2. Write comprehensive tests
3. Analyze time/space complexity
4. Fill out the PR template
5. Create PR for review

---

BEFORE YOU START - THINK:
- Why does the naive O(n²) fail here?
- What property of the array can we exploit?
- How do two pointers help?
- What's the key insight that makes this O(n)?
*/

/// Solution for Two Sum II - Input Array Is Sorted
///
/// # Approach
/// Two pointers starting from opposite ends of the sorted array.
///
/// # Complexity
/// - Time: O(n) - Single pass, each pointer moves at most n times
/// - Space: O(1) - Only two pointer variables
///
/// # Pattern Applied
/// Two Pointers (Opposite Ends)
///
/// # Key Insights
/// Sorted order enables O(1) decisions to eliminate possibilities.
/// When sum < target: move left right (need larger number).
/// When sum > target: move right left (need smaller number).
/// This monotonic property reduces O(n²) to O(n).
// Time: O(n)
// Space: O(1)
pub fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
    let mut left = 0;
    let mut right = numbers.len() - 1;

    while left < right {
        let sum = numbers[left] + numbers[right];

        match sum.cmp(&target) {
            std::cmp::Ordering::Equal => {
                // Found! Return 1-indexed positions
                return vec![(left + 1) as i32, (right + 1) as i32];
            }
            std::cmp::Ordering::Less => {
                // Sum too small - need larger number
                left += 1;
            }
            std::cmp::Ordering::Greater => {
                // Sum too large - need smaller number
                right -= 1;
            }
        }
    }

    vec![] // Problem guarantees solution exists
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        let numbers = vec![2, 7, 11, 15];
        let target = 9;
        assert_eq!(two_sum(&numbers, target), vec![1, 2]);
    }

    #[test]
    fn test_example_2() {
        let numbers = vec![2, 3, 4];
        let target = 6;
        assert_eq!(two_sum(&numbers, target), vec![1, 3]);
    }

    #[test]
    fn test_example_3() {
        let numbers = vec![-1, 0];
        let target = -1;
        assert_eq!(two_sum(&numbers, target), vec![1, 2]);
    }

    #[test]
    fn test_duplicates() {
        let numbers = vec![1, 1, 1, 1, 1, 5];
        assert_eq!(two_sum(&numbers, 6), vec![1, 6]);
    }

    #[test]
    fn test_large_array() {
        let numbers: Vec<i32> = (1..=1000).collect();
        assert_eq!(two_sum(&numbers, 1999), vec![999, 1000]);
    }

    #[test]
    fn test_all_negatives() {
        let numbers = vec![-10, -5, -2, 0, 3, 7];
        assert_eq!(two_sum(&numbers, -3), vec![1, 6]); // -10 + 7 = -3
    }

    #[test]
    fn test_two_elements_min() {
        let numbers = vec![1, 2];
        assert_eq!(two_sum(&numbers, 3), vec![1, 2]);
    }

    #[test]
    fn test_max_min_values() {
        let numbers = vec![-1000, -500, 0, 500, 1000];
        assert_eq!(two_sum(&numbers, -500), vec![1, 4]); // -1000 + 500 = -500
    }
}

/*
SENIOR ENGINEER CHECKLIST (Complete before PR):

□ Solution is correct and handles all test cases
□ Time complexity is optimal (O(n))
□ Space complexity is optimal (O(1))
□ All edge cases are tested
□ Code is clean and idiomatic Rust
□ Complexity analysis is written with proof
□ Considered alternative approaches
□ Can explain why this approach over others

*/
