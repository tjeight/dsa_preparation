# Essential Coding Interview Patterns

A structured guide to identifying and applying high-yield algorithmic patterns when solving DSA problems.

---

## 🧭 Pattern Identification Matrix ("When you see X, think Y")

| Problem Characteristic / Keyword | Recommended Pattern | Data Structure | Target Time Complexity |
| :--- | :--- | :--- | :--- |
| Sorted array, finding a pair/triplet with target sum | **Two Pointers** | Array / List | $O(n)$ or $O(n \log n)$ |
| Contiguous subarray/substring, min/max length with condition | **Sliding Window** | Array / String / Hash Map | $O(n)$ |
| Linked list cycle detection, finding middle of linked list | **Fast & Slow Pointers** | Linked List | $O(n)$ time, $O(1)$ space |
| Overlapping time intervals, scheduling, calendar conflicts | **Merge Intervals** | Array (sorted by start time) | $O(n \log n)$ |
| Numbers in range $[1 \dots n]$ or $[0 \dots n]$ with missing/duplicate numbers | **Cyclic Sort** | Array | $O(n)$ time, $O(1)$ space |
| Reversing linked list nodes without extra memory | **In-Place Reversal** | Linked List | $O(n)$ time, $O(1)$ space |
| Level-by-level traversal, shortest path in unweighted graph | **Tree / Graph BFS** | Queue (`collections.deque`) | $O(V + E)$ |
| Finding all paths, max depth, subtree calculations | **Tree DFS / Recursion** | Call Stack / Explicit Stack | $O(V + E)$ |
| Running median, streaming data with min/max tracking | **Two Heaps** | Min-Heap + Max-Heap (`heapq`) | $O(\log n)$ insert, $O(1)$ query |
| Generating all subsets, permutations, combinations | **Backtracking** | Recursion with state undo | $O(2^n)$ or $O(n!)$ |
| Sorted array, rotated sorted array, search on answer space | **Modified Binary Search** | Array / Monotonic Function | $O(\log n)$ |
| Finding $K$ largest/smallest/most frequent elements | **Top-K Elements** | Heap (`heapq`) or Quickselect | $O(n \log k)$ or $O(n)$ |
| Next greater element, largest rectangle in histogram | **Monotonic Stack** | Stack (`list`) | $O(n)$ |
| Maximum profit, minimum cost, overlapping subproblems | **Dynamic Programming** | Array / Memoization Dict | $O(n)$ to $O(n^2)$ |

---

## 1. Two Pointers
- **Idea**: Use two pointers (`left` and `right`) moving toward each other or in the same direction to eliminate unnecessary combinations.
- **Template**:
  ```python
  left, right = 0, len(arr) - 1
  while left < right:
      current_sum = arr[left] + arr[right]
      if current_sum == target:
          return [left, right]
      elif current_sum < target:
          left += 1  # Need larger sum
      else:
          right -= 1  # Need smaller sum
  ```

---

## 2. Sliding Window
- **Idea**: Maintain an expanding and contracting subarray window `[left, right]` to satisfy a constraint.
- **Template (Variable Size)**:
  ```python
  left = 0
  for right in range(len(arr)):
      # 1. Expand window: add arr[right] to window state
      add_to_window(arr[right])

      # 2. Shrink window while invalid
      while not is_valid():
          remove_from_window(arr[left])
          left += 1

      # 3. Update answer with valid window
      max_len = max(max_len, right - left + 1)
  ```

---

## 3. Fast & Slow Pointers (Tortoise and Hare)
- **Idea**: Advance `slow` by 1 step and `fast` by 2 steps. If a cycle exists, they will inevitably meet.
- **Template**:
  ```python
  slow = fast = head
  while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
          return True  # Cycle detected
  return False
  ```

---

## 4. Monotonic Stack
- **Idea**: Maintain elements in strict increasing or decreasing order. When a new element violates the order, pop until order is restored.
- **Template (Next Greater Element)**:
  ```python
  result = [-1] * len(nums)
  stack = []  # Stores indices
  for i, num in enumerate(nums):
      while stack and nums[stack[-1]] < num:
          prev_idx = stack.pop()
          result[prev_idx] = num
      stack.append(i)
  ```

---

## 5. Binary Search on Answer Space
- **Idea**: If the feasibility function $f(x)$ is monotonic (e.g., False False ... True True), binary search the optimal value $x$ directly.
- **Template**:
  ```python
  low, high = min_possible, max_possible
  ans = high
  while low <= high:
      mid = (low + high) // 2
      if is_feasible(mid):
          ans = mid
          high = mid - 1  # Try for smaller/better
      else:
          low = mid + 1
  ```
