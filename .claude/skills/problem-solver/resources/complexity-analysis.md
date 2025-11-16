# Complexity Analysis

## Core Principle

**Always provide TIGHT bounds, not just upper bounds.**

- ❌ "This is O(n²)" (without justification)
- ✅ "This is Θ(n²) because we have nested loops over n elements, and each inner iteration does O(1) work"

---

## Time Complexity

### Common Operations

| Operation | Time | Justification |
|-----------|------|---------------|
| Array access | O(1) | Direct memory address calculation |
| Array append | O(1) amortized | Doubling strategy: occasional O(n) copy |
| Array insert (middle) | O(n) | Must shift n elements |
| Hash table get/set | O(1) average | O(n) worst case (collision) |
| Binary search | O(log n) | Halve search space each step |
| Linear search | O(n) | Must check each element |
| Sorting | O(n log n) | Comparison-based lower bound |
| DFS/BFS | O(V + E) | Visit each vertex, explore each edge |

### Loop Analysis

**Single loop**:
```rust
for i in 0..n {  // O(n)
    println!("{}", i);  // O(1)
}
// Total: O(n)
```

**Nested loops**:
```rust
for i in 0..n {  // O(n)
    for j in 0..n {  // O(n)
        println!("{}, {}", i, j);  // O(1)
    }
}
// Total: O(n²)
```

**Dependent nested loops**:
```rust
for i in 0..n {  // O(n)
    for j in i..n {  // O(n - i)
        println!("{}, {}", i, j);  // O(1)
    }
}
// Sum from i=0 to n-1 of (n-i) = n + (n-1) + ... + 1 = n(n+1)/2 = O(n²)
```

**Logarithmic loop**:
```rust
let mut i = 1;
while i < n {
    println!("{}", i);
    i *= 2;  // i doubles each iteration
}
// i = 1, 2, 4, 8, ..., 2^k where 2^k < n
// k = log₂(n), so O(log n)
```

### Recursive Analysis

**Method 1: Recurrence Relations**

Example: Fibonacci
```rust
fn fib(n: i32) -> i32 {
    if n <= 1 { return n; }
    fib(n-1) + fib(n-2)
}
```

Recurrence: T(n) = T(n-1) + T(n-2) + O(1)

Without memoization: T(n) = O(2^n)
With memoization: T(n) = O(n)

**Method 2: Recursion Tree**

```
fib(4)
├─ fib(3)
│  ├─ fib(2)
│  │  ├─ fib(1) → 1
│  │  └─ fib(0) → 1
│  └─ fib(1) → 1
└─ fib(2)
   ├─ fib(1) → 1
   └─ fib(0) → 1
```

Height = n, each level ~doubles nodes → O(2^n)

**Method 3: Master Theorem**

For T(n) = aT(n/b) + f(n):

- If f(n) = O(n^(log_b(a) - ε)) for ε > 0: T(n) = Θ(n^log_b(a))
- If f(n) = Θ(n^log_b(a)): T(n) = Θ(n^log_b(a) × log n)
- If f(n) = Ω(n^(log_b(a) + ε)) for ε > 0: T(n) = Θ(f(n))

Example: Merge Sort
- T(n) = 2T(n/2) + O(n)
- a=2, b=2, f(n)=n
- log_b(a) = log_2(2) = 1
- f(n) = Θ(n^1) → Case 2
- T(n) = Θ(n log n)

### Amortized Analysis

**Example: Dynamic Array Append**

Single append might cost O(n) when array needs resizing, but:

1. Start with capacity 1
2. Double capacity each time: 1→2→4→8→16...
3. After n operations, total cost = n + (1+2+4+8+...+n/2) = n + (n-1) = 2n-1
4. Amortized cost = (2n-1)/n = O(1) per operation

**Accounting Method**:
- Charge $3 per append
- $1 for actual insertion
- $2 saved for future copying
- When resize happens, we've saved enough to pay for all copies

---

## Space Complexity

**Count auxiliary space** (excluding input):

**O(1) - Constant**:
```rust
fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut left = 0;  // O(1)
    let mut right = nums.len() - 1;  // O(1)
    // Only a few variables, no matter input size
}
```

**O(n) - Linear**:
```rust
use std::collections::HashMap;
let mut map = HashMap::new();  // Can store up to n elements
for num in nums {
    map.insert(num, i);  // O(n) space total
}
```

**O(log n) - Logarithmic (recursion depth)**:
```rust
fn binary_search(arr: &[i32], target: i32) -> Option<usize> {
    // Each recursive call adds to stack
    // Max depth = log n
}
```

**O(n) - Recursion stack**:
```rust
fn dfs(node: &TreeNode) {
    // For skewed tree, depth can be n
    // Stack space = O(n) worst case
    // For balanced tree, O(log n)
}
```

---

## Proof Techniques

### 1. Loop Invariant

**Claim**: Two pointers finds solution if it exists

**Proof**:
1. **Initialization**: Start with left=0, right=n-1 (covers entire array)
2. **Maintenance**:
   - If sum < target: increase sum by moving left right (correct)
   - If sum > target: decrease sum by moving right left (correct)
   - We never skip the solution
3. **Termination**: When left >= right, we've checked all valid pairs

### 2. Contradiction

**Claim**: Comparison-based sorting is Ω(n log n)

**Proof**:
- n! possible permutations of n elements
- Decision tree has n! leaves (one per permutation)
- Binary tree with n! leaves has height ≥ log₂(n!)
- log₂(n!) = Θ(n log n) by Stirling's approximation
- Therefore, any comparison-based sort is Ω(n log n)

### 3. Induction

**Claim**: Fibonacci with memoization is O(n)

**Base case**: fib(0) and fib(1) are O(1)

**Inductive step**:
- Assume fib(k) is O(1) for all k < n (cached)
- Then fib(n) = fib(n-1) + fib(n-2) = O(1) + O(1) = O(1)
- Total: n values × O(1) each = O(n)

---

## Common Mistakes

### Mistake 1: Ignoring Hidden Operations

❌ **Wrong**:
```rust
for s in strings {
    result += s;  // String concatenation is O(len(s))!
}
// Claimed: O(n), Actual: O(n × m) where m = avg string length
```

✅ **Correct**:
```rust
let mut result = String::new();
for s in strings {
    result.push_str(s);  // Still O(n × m) due to reallocation
}
// Better: Use Vec<String> and join, or StringBuilder equivalent
```

### Mistake 2: Confusing O, Ω, Θ

- **O**: Upper bound (≤)
- **Ω**: Lower bound (≥)
- **Θ**: Tight bound (=)

Example: Linear search
- Time: Θ(n) in worst case
- Time: O(1) in best case
- Time: Θ(n) average case

### Mistake 3: Forgetting Recalculation Costs

❌ **Wrong**:
```rust
for i in 0..n {
    if is_prime(i) {  // is_prime is O(√n)
        // ...
    }
}
// Claimed: O(n), Actual: O(n√n)
```

---

## Complexity Proof Template

For every solution, provide:

```
/// Two Sum II - Two Pointers
///
/// Time: O(n)
/// - Single pass through array with two pointers
/// - Each element visited at most once
/// - Pointer movements: left moves right ≤ n times, right moves left ≤ n times
/// - Total operations: ≤ 2n = O(n)
///
/// Space: O(1)
/// - Only two integer pointers (left, right)
/// - No auxiliary data structures
/// - Input array not modified
/// - Therefore constant space
```

**Be specific**:
- What's being counted? (comparisons, swaps, recursive calls)
- Why this bound? (loop iterations, recursion depth, data structure size)
- Best/average/worst case differences?

---

**Always prove your complexity. Interviewers expect justification, not guesses.**
