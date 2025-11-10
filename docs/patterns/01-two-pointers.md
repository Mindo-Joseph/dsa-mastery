---
layout: default
title: "Two Pointers Pattern - First Principles to Mastery"
show_breadcrumb: true
category: "Patterns"
category_url: "/#-pattern-writeups"
---

# Two Pointers Pattern - First Principles to Mastery

**Pattern Difficulty**: ⭐ Fundamental (Start here)
**Time to Master**: 2-3 days
**Problems to Solve**: 5-7

---

<div class="card">

</div>


## First Principles: Why Does This Exist?
## First Principles: Why Does This Exist?

### The Problem with Naive Approaches

Consider this problem:
> "Find two numbers in a sorted array that sum to a target"

**Naive approach:**
```rust
// Brute force: Check every pair
fn two_sum_brute(nums: &[i32], target: i32) -> Option<(usize, usize)> {
    for i in 0..nums.len() {
        for j in (i+1)..nums.len() {
            if nums[i] + nums[j] == target {
                return Some((i, j));
            }
        }
    }
    None
}
// Time: O(n²) - for each element, check all others
// Space: O(1)
```

**Why this fails at scale:**
- n = 10,000 → 100 million operations
- n = 100,000 → 10 billion operations
- Google-scale data → Completely unusable

### The Key Insight (First Principle)

**If the array is sorted**, we can make decisions that eliminate multiple possibilities at once.

Think about it:
- If `nums[left] + nums[right] < target` → left pointer is TOO SMALL
- Moving right pointer would make sum even SMALLER (sorted array!)
- Therefore: **We can eliminate ALL pairs with nums[left]**
- Move left pointer forward

Similarly:
- If `nums[left] + nums[right] > target` → right pointer is TOO LARGE
- Move right pointer backward

**This is the insight**: Use the sorted property to prune the search space in O(1) decisions.

---

<div class="card">

</div>


## Pattern Recognition: When to Use Two Pointers
## Pattern Recognition: When to Use Two Pointers

### ✅ Use Two Pointers When:

1. **Array/String is sorted** (or can be sorted)
2. **Looking for pairs/triplets** that satisfy a condition
3. **Partitioning** problem (move elements meeting criteria)
4. **Comparing elements from both ends** inward
5. **Need O(n) instead of O(n²)** solution

### ❌ Don't Use When:

- Array is unsorted AND can't be sorted
- Need to find subarrays (use Sliding Window instead)
- Random access pattern required
- Need O(log n) (use Binary Search instead)

---

<div class="card">

</div>


## Senior-Level Understanding: Complexity Analysis
## Senior-Level Understanding: Complexity Analysis

### Why is it O(n)?

**Proof:**
- Left pointer starts at 0, only moves RIGHT
- Right pointer starts at n-1, only moves LEFT
- Each iteration moves exactly ONE pointer
- Max total moves: n (left to end) + n (right to start) = 2n
- Therefore: **O(n) time**

This is **amortized analysis** - a senior engineer explains this clearly.

### Space Complexity

- Usually **O(1)** - just two pointers
- If you sort first: O(log n) for sorting stack space
- Always clarify assumptions in interviews

---

<div class="card">

</div>


## The Pattern Template (Rust)
## The Pattern Template (Rust)

### Basic Two Pointers (Opposite Ends)

```rust
pub fn two_pointers_opposite_ends<T, F>(arr: &[T], condition: F) -> Option<(usize, usize)>
where
    F: Fn(&T, &T) -> std::cmp::Ordering,
{
    if arr.is_empty() {
        return None;
    }

    let mut left = 0;
    let mut right = arr.len() - 1;

    while left < right {
        match condition(&arr[left], &arr[right]) {
            std::cmp::Ordering::Equal => return Some((left, right)),
            std::cmp::Ordering::Less => left += 1,   // Sum too small, increase left
            std::cmp::Ordering::Greater => right -= 1, // Sum too large, decrease right
        }
    }

    None
}
```

### Two Pointers (Same Direction - Slow/Fast)

```rust
pub fn two_pointers_same_direction<T, F>(arr: &mut [T], predicate: F) -> usize
where
    F: Fn(&T) -> bool,
{
    let mut slow = 0;

    for fast in 0..arr.len() {
        if predicate(&arr[fast]) {
            arr.swap(slow, fast);
            slow += 1;
        }
    }

    slow // Returns new length after partitioning
}
```

---

<div class="card">

</div>


## Common Variations (Senior Interview Level)
## Common Variations (Senior Interview Level)

### 1. Two Sum (Sorted Array)
- **Pattern**: Opposite ends
- **Time**: O(n)
- **Key**: Use sorted property to prune

### 2. Three Sum
- **Pattern**: Fix one element, two pointers on rest
- **Time**: O(n²) - but optimal for this problem
- **Key**: Skip duplicates carefully

### 3. Container With Most Water
- **Pattern**: Opposite ends, maximize area
- **Time**: O(n)
- **Key**: Move pointer of shorter height (greedy)

### 4. Remove Duplicates In-Place
- **Pattern**: Same direction (slow/fast)
- **Time**: O(n)
- **Key**: Slow pointer tracks unique elements

### 5. Trapping Rain Water
- **Pattern**: Opposite ends with height tracking
- **Time**: O(n)
- **Key**: Track max heights from both sides

---

<div class="card">

</div>


## Edge Cases (Google Interview Checklist)
## Edge Cases (Google Interview Checklist)

Always consider:
- [ ] **Empty array** - What should return?
- [ ] **Single element** - Pointers might not work
- [ ] **Two elements** - Boundary case
- [ ] **All duplicates** - How to handle?
- [ ] **No solution exists** - Return value?
- [ ] **Multiple solutions** - Which to return?
- [ ] **Integer overflow** - When summing large numbers
- [ ] **Negative numbers** - Does algorithm still work?

---

<div class="card">

</div>


## Rust-Specific Considerations
## Rust-Specific Considerations

### 1. Borrowing vs Ownership
```rust
// ❌ Takes ownership unnecessarily
fn solve(nums: Vec<i32>) -> i32 { ... }

// ✅ Borrows - caller keeps ownership
fn solve(nums: &[i32]) -> i32 { ... }

// ✅ Mutable borrow when modifying
fn solve(nums: &mut [i32]) -> usize { ... }
```

### 2. Slice vs Vec
```rust
// ✅ Use slices for flexibility
fn two_sum(nums: &[i32], target: i32) -> Option<(usize, usize)>

// Works with: Vec, arrays, subslices
```

### 3. Iterator Methods
```rust
// Sometimes built-in methods are clearer
nums.windows(2).position(|w| w[0] + w[1] == target)
```

---

<div class="card">

</div>


## Trade-offs (Senior Thinking)
## Trade-offs (Senior Thinking)

### Sorting First vs Hash Map

**Two Pointers (requires sort):**
- Time: O(n log n) for sort + O(n) for search = O(n log n)
- Space: O(1) or O(log n) for sort
- Pros: No extra space for data, finds all pairs easily
- Cons: Modifies array or needs copy

**Hash Map:**
- Time: O(n)
- Space: O(n)
- Pros: Faster, keeps original order
- Cons: Uses more memory

**Senior answer in interview:**
> "If space is constrained and array can be modified, two pointers after sorting is optimal. If we need O(n) time and have space, hash map is better. I'd ask: What are the constraints and priorities?"

---

<div class="card">

</div>


## Practice Problems (In Order)
## Practice Problems (In Order)

### Easy (Warm-up)
1. **Two Sum II** (sorted array)
2. **Valid Palindrome**
3. **Remove Duplicates from Sorted Array**

### Medium (Core)
4. **3Sum**
5. **Container With Most Water**
6. **Sort Colors** (Dutch National Flag)

### Hard (Stretch)
7. **Trapping Rain Water**
8. **Median of Two Sorted Arrays** (binary search + two pointers)

---

<div class="card">

</div>


## Interview Communication Template
## Interview Communication Template

When you identify a two pointers problem:

**1. Pattern Recognition (30 sec)**
> "This looks like a two pointers problem because we have a sorted array and we're looking for pairs. The naive O(n²) approach would time out with the given constraints."

**2. Approach Explanation (1 min)**
> "I'll use two pointers starting at opposite ends. If the sum is too small, the left pointer is too small so I move it right. If too large, I move right pointer left. This eliminates possibilities in O(1) per iteration."

**3. Complexity Analysis (30 sec)**
> "Time is O(n) because each pointer moves at most n times, and each move is O(1). Space is O(1) since we only use two pointers."

**4. Edge Cases (30 sec)**
> "I'll handle empty array, single element, and no solution cases explicitly."

**Total: ~2.5 minutes before coding** - This shows senior-level thinking.

---

<div class="card">

</div>


## Next Steps
## Next Steps

1. Implement the template in `src/patterns/two_pointers/mod.rs`
2. Solve first problem (Two Sum II)
3. Create PR with detailed analysis
4. Get feedback, optimize
5. Move to next problem

---

**Remember**: The pattern is just a tool. The understanding is the weapon.

Ready for your first problem?


</div>