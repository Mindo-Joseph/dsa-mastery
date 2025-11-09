# DSA Pattern Mastery Guide

## 12 Core Patterns to Master

### 1. Two Pointers
**When to use**: Array/string problems requiring pair comparison or partitioning
**Key insight**: Reduce O(n²) to O(n) by using two indices moving inward/outward
**Practice goal**: 5-7 problems
**Common problems**: Pair sum, palindrome check, container with most water

### 2. Sliding Window
**When to use**: Subarray/substring problems with contiguous elements
**Key insight**: Maintain window state, expand/shrink based on condition
**Practice goal**: 5-7 problems
**Common problems**: Max sum subarray, longest substring, minimum window

### 3. Fast & Slow Pointers
**When to use**: Cycle detection, finding middle elements
**Key insight**: Two pointers moving at different speeds
**Practice goal**: 5-7 problems
**Common problems**: Linked list cycle, find middle, palindrome linked list

### 4. Merge Intervals
**When to use**: Overlapping intervals, scheduling problems
**Key insight**: Sort then merge overlapping ranges
**Practice goal**: 5-7 problems
**Common problems**: Meeting rooms, insert interval, interval intersection

### 5. Cyclic Sort
**When to use**: Array with numbers in range [1, n]
**Key insight**: Place each number at its correct index
**Practice goal**: 5-7 problems
**Common problems**: Find missing number, find duplicates, first k missing

### 6. In-place Linked List Reversal
**When to use**: Reversing parts or whole of linked list
**Key insight**: Change next pointers iteratively
**Practice goal**: 5-7 problems
**Common problems**: Reverse linked list, reverse k-group, palindrome check

### 7. Tree BFS (Breadth-First Search)
**When to use**: Level-order traversal, shortest path in tree
**Key insight**: Use queue for level-by-level processing
**Practice goal**: 5-7 problems
**Common problems**: Level order, zigzag traversal, right side view

### 8. Tree DFS (Depth-First Search)
**When to use**: Path problems, tree recursion
**Key insight**: Preorder/inorder/postorder traversal patterns
**Practice goal**: 5-7 problems
**Common problems**: Path sum, diameter, lowest common ancestor

### 9. Graphs (BFS/DFS/Topological Sort/Union Find)
**When to use**: Connected components, shortest paths, dependencies
**Key insight**: Model as graph, apply appropriate traversal
**Practice goal**: 7-10 problems
**Common problems**: Number of islands, course schedule, clone graph

### 10. Dynamic Programming
**When to use**: Optimization problems with overlapping subproblems
**Key insight**: Memoization or bottom-up table building
**Practice goal**: 10-15 problems (most important!)
**Subtypes**: 1D DP, 2D DP, Knapsack, LCS, LIS

### 11. Backtracking
**When to use**: Generate all combinations/permutations, constraint satisfaction
**Key insight**: DFS with choice exploration and pruning
**Practice goal**: 5-7 problems
**Common problems**: Permutations, subsets, N-queens, word search

### 12. Binary Search
**When to use**: Sorted arrays, search space reduction
**Key insight**: Divide search space in half repeatedly
**Practice goal**: 5-7 problems
**Common problems**: Search rotated array, find peak, first/last occurrence

---

## Learning Strategy

### Phase 1: Foundation (Weeks 1-2)
- Two Pointers
- Sliding Window
- Binary Search

### Phase 2: Data Structures (Weeks 3-4)
- Fast & Slow Pointers
- Linked List Reversal
- Tree BFS/DFS

### Phase 3: Advanced Structures (Weeks 5-6)
- Graphs
- Heaps
- Merge Intervals

### Phase 4: Problem-Solving Paradigms (Weeks 7-10)
- Dynamic Programming (2 weeks!)
- Backtracking
- Cyclic Sort

### Phase 5: Integration (Weeks 11-12)
- Mixed pattern problems
- Mock interviews
- Optimization challenges

---

## How to Use This with NotebookLM

### For Each Pattern:

1. **Query Theory**
   ```
   "Ask my algorithm design book about [pattern name] - when to use it,
   time complexity, and common variations"
   ```

2. **Get Practice Problems**
   ```
   "Query my leetcode notebook for 5 [difficulty] level problems
   using the [pattern name] pattern"
   ```

3. **Understand Architecture**
   ```
   "Why does [pattern] work? Explain the underlying algorithmic
   principle from my architecture book"
   ```

4. **Implement with Claude**
   - I help you code the solution
   - We analyze time/space complexity together
   - Debug and optimize

5. **Track Progress**
   ```bash
   python scripts/log_progress.py log [pattern] [problem] [difficulty] [time] [status]
   ```

---

## Pattern Recognition Checklist

When you see a problem, ask:
- [ ] Does it involve pairs/triplets? → Two Pointers
- [ ] Contiguous subarray/substring? → Sliding Window
- [ ] Cycle detection or middle finding? → Fast/Slow Pointers
- [ ] Overlapping ranges? → Merge Intervals
- [ ] Numbers in range [1,n]? → Cyclic Sort
- [ ] Reverse part of linked list? → In-place Reversal
- [ ] Tree level-by-level? → BFS
- [ ] Tree paths or recursion? → DFS
- [ ] Connected components? → Graph Traversal
- [ ] Optimal solution with choices? → Dynamic Programming
- [ ] Generate all possibilities? → Backtracking
- [ ] Sorted array search? → Binary Search
