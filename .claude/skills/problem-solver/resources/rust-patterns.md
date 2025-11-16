# Rust Patterns for Algorithms

## Idiomatic Rust for DSA

### Avoid Unnecessary Clones

❌ **Bad**:
```rust
pub fn process(nums: Vec<i32>) -> Vec<i32> {
    let mut result = nums.clone();  // Unnecessary clone!
    result.sort();
    result
}
```

✅ **Good**:
```rust
pub fn process(mut nums: Vec<i32>) -> Vec<i32> {
    nums.sort();  // Mutate in place
    nums
}
```

### Use Slices for Borrowing

❌ **Bad**:
```rust
pub fn max_sum(nums: Vec<i32>) -> i32 {
    // Takes ownership, can't use nums after
}
```

✅ **Good**:
```rust
pub fn max_sum(nums: &[i32]) -> i32 {
    // Borrows, allows reuse
}
```

### Iterator Patterns

✅ **Idiomatic**:
```rust
// Instead of manual loops
let sum: i32 = nums.iter().sum();
let max = nums.iter().max().unwrap();
let filtered: Vec<_> = nums.iter().filter(|&&x| x > 0).collect();
```

### Option Handling

✅ **Pattern matching**:
```rust
match node {
    Some(n) => process(n),
    None => return None,
}
```

✅ **map/and_then**:
```rust
node.map(|n| n.val).unwrap_or(0)
node.and_then(|n| find_target(&n.left))
```

### Common DSA Patterns in Rust

**Two Pointers**:
```rust
pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let (mut left, mut right) = (0, numbers.len() - 1);

    while left < right {
        match numbers[left] + numbers[right] {
            sum if sum == target => return vec![left as i32, right as i32],
            sum if sum < target => left += 1,
            _ => right -= 1,
        }
    }
    vec![]
}
```

**Sliding Window**:
```rust
pub fn max_sum_subarray(nums: &[i32], k: usize) -> i32 {
    let window_sum: i32 = nums[..k].iter().sum();
    let mut max_sum = window_sum;

    nums.windows(k + 1).fold(window_sum, |sum, window| {
        let new_sum = sum - window[0] + window[k];
        max_sum = max_sum.max(new_sum);
        new_sum
    });

    max_sum
}
```

**Hash Map**:
```rust
use std::collections::HashMap;

pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map = HashMap::new();

    for (i, &num) in nums.iter().enumerate() {
        if let Some(&complement_idx) = map.get(&(target - num)) {
            return vec![complement_idx as i32, i as i32];
        }
        map.insert(num, i);
    }
    vec![]
}
```

**DFS (Tree)**:
```rust
pub fn dfs(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
    let mut result = Vec::new();

    fn traverse(node: &Option<Rc<RefCell<TreeNode>>>, result: &mut Vec<i32>) {
        if let Some(n) = node {
            let n = n.borrow();
            traverse(&n.left, result);
            result.push(n.val);
            traverse(&n.right, result);
        }
    }

    traverse(&root, &mut result);
    result
}
```

**BFS**:
```rust
use std::collections::VecDeque;

pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
    let mut result = Vec::new();
    let mut queue = VecDeque::new();

    if let Some(node) = root {
        queue.push_back(node);
    }

    while !queue.is_empty() {
        let level_size = queue.len();
        let mut level = Vec::new();

        for _ in 0..level_size {
            if let Some(node) = queue.pop_front() {
                let node = node.borrow();
                level.push(node.val);

                if let Some(left) = node.left.clone() {
                    queue.push_back(left);
                }
                if let Some(right) = node.right.clone() {
                    queue.push_back(right);
                }
            }
        }
        result.push(level);
    }

    result
}
```

**Memoization (DP)**:
```rust
use std::collections::HashMap;

pub fn fib(n: i32) -> i32 {
    fn helper(n: i32, memo: &mut HashMap<i32, i32>) -> i32 {
        if n <= 1 {
            return n;
        }

        if let Some(&result) = memo.get(&n) {
            return result;
        }

        let result = helper(n - 1, memo) + helper(n - 2, memo);
        memo.insert(n, result);
        result
    }

    helper(n, &mut HashMap::new())
}
```

### Cargo Test Patterns

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        assert_eq!(two_sum(vec![2, 7, 11, 15], 9), vec![0, 1]);
    }

    #[test]
    fn test_edge_empty() {
        assert_eq!(two_sum(vec![], 0), vec![]);
    }

    #[test]
    fn test_edge_single() {
        assert_eq!(two_sum(vec![1], 1), vec![]);
    }

    #[test]
    fn test_no_solution() {
        assert_eq!(two_sum(vec![1, 2, 3], 10), vec![]);
    }
}
```

### Performance Tips

1. **Pre-allocate** when size is known:
   ```rust
   let mut result = Vec::with_capacity(n);
   ```

2. **Use iterators** (often faster than manual loops):
   ```rust
   nums.iter().filter(|&&x| x > 0).collect()
   ```

3. **Avoid bounds checking** when safe:
   ```rust
   unsafe { *nums.get_unchecked(i) }  // Only if you're SURE i is valid
   ```

4. **Use references** to avoid moves:
   ```rust
   for &num in &nums {  // Borrow, not move
   ```

---

**Write clean, idiomatic Rust. Borrowing and lifetimes are features, not obstacles.**
