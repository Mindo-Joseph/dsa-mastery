# Pattern Recognition Guide

## Core Philosophy

**The secret to pattern recognition: Don't memorize solutions. Understand the properties that enable each pattern.**

---

## The 15 Essential Patterns

### 1. Two Pointers

**Property**: Sorted data or pairs with a relationship

**When to Use**:
- "Find pair/triplet that sums to target" + sorted array
- "Remove duplicates" from sorted array
- "Palindrome" checking
- "Container with most water" type problems

**Why It Works**:
Sorted arrays allow O(1) decisions that eliminate possibilities. Instead of checking all O(n²) pairs, we can eliminate half the search space with each comparison.

**Recognition Keywords**:
- Sorted array/linked list
- Pair/triplet problems
- Two elements with relationship
- Left/right symmetry

**Template**:
```rust
let mut left = 0;
let mut right = nums.len() - 1;

while left < right {
    let sum = nums[left] + nums[right];
    if sum == target {
        return vec![left, right];
    } else if sum < target {
        left += 1;  // Need larger sum
    } else {
        right -= 1; // Need smaller sum
    }
}
```

**Time**: O(n) | **Space**: O(1)

**Example Problems**:
- Two Sum II (sorted array)
- 3Sum
- Container With Most Water
- Trapping Rain Water

---

### 2. Sliding Window

**Property**: Contiguous subarray/substring with constraints

**When to Use**:
- "Subarray/substring with sum/length constraint"
- "Maximum/minimum of all subarrays of size K"
- "Longest substring without repeating characters"
- "Minimum window substring"

**Why It Works**:
Instead of recalculating from scratch for each window (O(n×k)), we maintain window state and update incrementally (O(n)).

**Recognition Keywords**:
- Subarray/substring
- Contiguous elements
- Fixed or variable window size
- Maximum/minimum with constraint

**Fixed Window Template**:
```rust
let mut window_sum = 0;
for i in 0..k {
    window_sum += nums[i];
}

let mut max_sum = window_sum;
for i in k..nums.len() {
    window_sum += nums[i] - nums[i - k];
    max_sum = max_sum.max(window_sum);
}
```

**Variable Window Template**:
```rust
let mut left = 0;
let mut result = 0;

for right in 0..s.len() {
    // Expand window
    add_to_window(s[right]);

    // Shrink if invalid
    while !is_valid() {
        remove_from_window(s[left]);
        left += 1;
    }

    result = result.max(right - left + 1);
}
```

**Time**: O(n) | **Space**: O(1) to O(k)

**Example Problems**:
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Longest Substring with K Distinct Characters

---

### 3. Binary Search

**Property**: Sorted data or monotonic function

**When to Use**:
- "Find target in sorted array"
- "Find first/last occurrence"
- "Search in rotated sorted array"
- "Find minimum in rotated array"
- "Kth smallest/largest element"

**Why It Works**:
Each comparison eliminates half the search space. O(n) → O(log n).

**Recognition Keywords**:
- Sorted/rotated array
- Find in logarithmic time
- First/last occurrence
- Peak element
- Square root, Kth element

**Template**:
```rust
let mut left = 0;
let mut right = nums.len() - 1;

while left <= right {
    let mid = left + (right - left) / 2;

    if nums[mid] == target {
        return mid;
    } else if nums[mid] < target {
        left = mid + 1;
    } else {
        right = mid - 1;
    }
}
```

**Time**: O(log n) | **Space**: O(1)

**Example Problems**:
- Binary Search
- Find First and Last Position
- Search in Rotated Sorted Array
- Find Peak Element

---

### 4. Fast & Slow Pointers (Floyd's Cycle)

**Property**: Linked list with cycle or finding middle

**When to Use**:
- "Detect cycle in linked list"
- "Find middle of linked list"
- "Find start of cycle"
- "Happy number" problems

**Why It Works**:
If there's a cycle, fast pointer will eventually lap slow pointer. If no cycle, fast reaches end.

**Recognition Keywords**:
- Linked list
- Cycle detection
- Middle element
- Cycle problems

**Template**:
```rust
let mut slow = head;
let mut fast = head;

while fast.is_some() && fast.as_ref().unwrap().next.is_some() {
    slow = slow.unwrap().next;
    fast = fast.unwrap().next.unwrap().next;

    if slow == fast {
        return true; // Cycle detected
    }
}
false // No cycle
```

**Time**: O(n) | **Space**: O(1)

**Example Problems**:
- Linked List Cycle
- Linked List Cycle II
- Middle of Linked List
- Happy Number

---

### 5. Hash Table

**Property**: Need fast lookup, counting, or grouping

**When to Use**:
- "Find pair with sum" (unsorted)
- "Count frequency"
- "Group anagrams"
- "First non-repeating character"
- "Subarray sum equals K"

**Why It Works**:
O(1) average lookup trades space for time. O(n²) → O(n).

**Recognition Keywords**:
- Count frequency
- Find pair/complement
- Group by property
- First unique/non-repeating
- Subarray sum

**Template**:
```rust
use std::collections::HashMap;

let mut map = HashMap::new();

for num in nums {
    let complement = target - num;
    if let Some(&index) = map.get(&complement) {
        return vec![index, i];
    }
    map.insert(num, i);
}
```

**Time**: O(n) | **Space**: O(n)

**Example Problems**:
- Two Sum
- Group Anagrams
- Subarray Sum Equals K
- Longest Consecutive Sequence

---

### 6. Depth-First Search (DFS)

**Property**: Tree/graph exploration, need all paths or backtracking

**When to Use**:
- "Find all paths"
- "Generate all combinations/permutations"
- "Solve maze/grid problems"
- "Tree traversal (in/pre/post-order)"
- "Connected components"

**Why It Works**:
Explores deeply before backtracking. Natural for recursive problems.

**Recognition Keywords**:
- All paths/solutions
- Backtracking
- Tree/graph traversal
- Maze/grid problems
- Combinations/permutations

**Template (Recursive)**:
```rust
fn dfs(node: &TreeNode, path: &mut Vec<i32>) {
    if node.is_none() {
        return;
    }

    path.push(node.val);

    if node.left.is_none() && node.right.is_none() {
        // Leaf node - process path
        process(path);
    }

    dfs(&node.left, path);
    dfs(&node.right, path);

    path.pop(); // Backtrack
}
```

**Time**: O(V + E) for graphs, O(n) for trees | **Space**: O(h) stack

**Example Problems**:
- Binary Tree Paths
- Path Sum
- Number of Islands
- Word Search
- Generate Parentheses

---

### 7. Breadth-First Search (BFS)

**Property**: Shortest path, level-order traversal

**When to Use**:
- "Shortest path in unweighted graph"
- "Level-order tree traversal"
- "Minimum steps/moves"
- "Nearest/closest problems"

**Why It Works**:
Explores level by level, guarantees shortest path in unweighted graphs.

**Recognition Keywords**:
- Shortest path (unweighted)
- Level-order traversal
- Minimum steps/distance
- Nearest/closest element

**Template**:
```rust
use std::collections::VecDeque;

let mut queue = VecDeque::new();
let mut visited = HashSet::new();

queue.push_back(start);
visited.insert(start);

while let Some(node) = queue.pop_front() {
    if node == target {
        return steps;
    }

    for neighbor in get_neighbors(node) {
        if !visited.contains(&neighbor) {
            visited.insert(neighbor);
            queue.push_back(neighbor);
        }
    }
}
```

**Time**: O(V + E) | **Space**: O(V)

**Example Problems**:
- Binary Tree Level Order Traversal
- Minimum Depth of Binary Tree
- Word Ladder
- Rotting Oranges

---

### 8. Dynamic Programming

**Property**: Optimal substructure + overlapping subproblems

**When to Use**:
- "Maximum/minimum profit/cost"
- "Count ways to do X"
- "Longest/shortest subsequence/substring"
- "Can partition/split optimally"

**Why It Works**:
Avoid recomputing subproblems. O(2^n) → O(n²) or O(n).

**Recognition Keywords**:
- Maximum/minimum
- Count ways
- Longest/shortest
- Optimal partition
- "Can you" questions with constraints

**Template (Top-Down)**:
```rust
use std::collections::HashMap;

fn dp(n: i32, memo: &mut HashMap<i32, i32>) -> i32 {
    if n <= 1 {
        return n;
    }

    if let Some(&result) = memo.get(&n) {
        return result;
    }

    let result = dp(n - 1, memo) + dp(n - 2, memo);
    memo.insert(n, result);
    result
}
```

**Template (Bottom-Up)**:
```rust
let mut dp = vec![0; n + 1];
dp[0] = 1;
dp[1] = 1;

for i in 2..=n {
    dp[i] = dp[i - 1] + dp[i - 2];
}
```

**Time**: O(states × work) | **Space**: O(states)

**Example Problems**:
- Climbing Stairs
- House Robber
- Longest Common Subsequence
- Coin Change
- Longest Increasing Subsequence

---

### 9. Backtracking

**Property**: Generate all solutions with constraints

**When to Use**:
- "Generate all permutations/combinations"
- "Solve puzzle (Sudoku, N-Queens)"
- "Word break with all solutions"
- "Partition with constraints"

**Why It Works**:
Build solution incrementally, backtrack when constraints violated.

**Recognition Keywords**:
- All solutions/possibilities
- Combinations with constraints
- Puzzle solving
- "Can you solve" with validation

**Template**:
```rust
fn backtrack(
    path: &mut Vec<i32>,
    remaining: &[i32],
    result: &mut Vec<Vec<i32>>
) {
    if is_solution(path) {
        result.push(path.clone());
        return;
    }

    for (i, &num) in remaining.iter().enumerate() {
        if !is_valid(path, num) {
            continue;
        }

        path.push(num);
        backtrack(path, &remaining[i+1..], result);
        path.pop();
    }
}
```

**Time**: O(2^n) to O(n!) | **Space**: O(n) stack

**Example Problems**:
- Permutations
- Subsets
- N-Queens
- Sudoku Solver
- Combination Sum

---

### 10. Greedy

**Property**: Local optimal → global optimal

**When to Use**:
- "Minimum intervals to remove"
- "Jump game"
- "Activity selection"
- "Fractional knapsack"

**Why It Works**:
Proof required! Greedy works when local choice is always safe.

**Recognition Keywords**:
- Interval scheduling
- Minimum/maximum with choices
- "At each step, choose..."
- Activity selection

**How to Verify**:
1. Greedy choice property: Local optimal is safe
2. Optimal substructure: Optimal solution contains optimal subsolutions
3. Proof by contradiction or exchange argument

**Template**:
```rust
// Sort by relevant property
items.sort_by_key(|item| item.end_time);

let mut count = 0;
let mut last_end = 0;

for item in items {
    if item.start >= last_end {
        count += 1;
        last_end = item.end;
    }
}
```

**Time**: O(n log n) for sorting | **Space**: O(1)

**Example Problems**:
- Jump Game
- Non-overlapping Intervals
- Partition Labels
- Gas Station

---

## Pattern Combinations

Many problems use multiple patterns:

- **Two Pointers + Hash Table**: 3Sum, 4Sum
- **Sliding Window + Hash Table**: Longest Substring with K Distinct
- **DFS + Backtracking**: Word Search, N-Queens
- **Binary Search + Greedy**: Minimum Speed to Arrive on Time
- **DP + DFS**: Longest Increasing Path in Matrix

---

## Decision Tree for Pattern Selection

```
Problem involves...

Array/String?
  ├─ Pairs/triplets? → Two Pointers (if sorted) or Hash Table
  ├─ Subarray/substring? → Sliding Window or Prefix Sum
  ├─ Sorted? → Binary Search
  └─ All subsets/permutations? → Backtracking

Tree/Graph?
  ├─ All paths? → DFS
  ├─ Shortest path? → BFS
  ├─ Connected components? → Union Find or DFS
  └─ Level order? → BFS

Optimization (max/min)?
  ├─ Choices at each step? → DP or Greedy
  ├─ Count ways? → DP
  └─ Partition problems? → DP

Linked List?
  ├─ Cycle? → Fast & Slow Pointers
  ├─ Middle? → Fast & Slow Pointers
  └─ Reverse? → Iterative pointer manipulation
```

---

## Practice Strategy

1. **Learn one pattern at a time** (5-7 problems per pattern)
2. **Understand WHY pattern works**, not just HOW
3. **Solve without looking at solution** (struggle builds skill)
4. **Time yourself** (45-60 min per problem)
5. **Review optimal solution** after solving
6. **Teach the pattern** to someone (or write explanation)

---

**Pattern recognition is a learnable skill. After 60-80 problems, patterns become obvious within minutes.**
