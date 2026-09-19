# Time and Space Complexity Cheatsheet

## Big-O Hierarchy (Fastest to Slowest)
1. $O(1)$ - Constant
2. $O(\log n)$ - Logarithmic
3. $O(n)$ - Linear
4. $O(n \log n)$ - Linearithmic
5. $O(n^2)$ - Quadratic
6. $O(2^n)$ - Exponential
7. $O(n!)$ - Factorial

---

## Python Built-in Operation Complexities

### `list` (Dynamic Array)
- Index / Assign: $O(1)$
- Append (at end): Amortized $O(1)$
- Pop from end: $O(1)$
- Pop from front / Insert at index $i$: $O(n)$ (requires shifting elements)
- Slice `arr[a:b]`: $O(b - a)$
- `in` check (membership): $O(n)$ linear scan
- Reverse in-place: $O(n)$
- Sort in-place (Timsort): $O(n \log n)$ time, $O(n)$ space

### `str` (Immutable Sequence of Characters)
- Index access `s[i]`: $O(1)$
- Length `len(s)`: $O(1)$
- Slicing `s[a:b]`: $O(b - a)$ (creates a new string)
- Substring check `sub in s`: $O(n + m)$ (Boyer-Moore-Horspool algorithm)
- Search `s.find(sub)`: $O(n \cdot m)$ worst case, $O(n + m)$ average
- Count occurrences `s.count(sub)`: $O(n)$
- Case conversion `s.upper()`, `s.lower()`: $O(n)$
- Whitespace stripping `s.strip()`: $O(n)$
- Substring replace `s.replace(old, new)`: $O(n)$
- Concatenation in loop `s += ch`: **$O(n^2)$ anti-pattern!**
- List join `''.join(list_of_chars)`: **$O(n)$ optimal linear pattern**

### `tuple` (Immutable Sequence of Elements)
- Index access `t[i]`: $O(1)$
- Length `len(t)`: $O(1)$
- Slicing `t[a:b]`: $O(b - a)$
- Membership `x in t`: $O(n)$ linear scan
- Count occurrences `t.count(x)`: $O(n)$
- Index lookup `t.index(x)`: $O(n)$
- Concatenation `t1 + t2`: $O(\text{len}(t1) + \text{len}(t2))$

### `dict` & `set` (Hash Tables)
- Insert / Update / Set: Average $O(1)$, Worst $O(n)$
- Lookup / Get: Average $O(1)$, Worst $O(n)$
- Delete / Pop / Remove: Average $O(1)$, Worst $O(n)$
- Membership (`x in s` / `k in d`): Average $O(1)$, Worst $O(n)$
- Set Discard `s.discard(x)`: Average $O(1)$, Worst $O(n)$ (safe, no `KeyError`)
- Set Union $s \mid t$: $O(\text{len}(s) + \text{len}(t))$
- Set Intersection $s \ \& \ t$: $O(\min(\text{len}(s), \text{len}(t)))$
- Set Difference $s - t$: $O(\text{len}(s))$
- Iteration over keys / values: $O(n)$

### `collections.deque` (Doubly-Linked List / Block Array)
- Append / Appendleft: $O(1)$
- Pop / Popleft: $O(1)$
- Access by index: $O(n)$ (use `list` if random index access is needed)

### `heapq` (Binary Min-Heap)
- `heappush(heap, item)`: $O(\log n)$
- `heappop(heap)`: $O(\log n)$
- `heapify(list)`: $O(n)$
- `heappushpop(heap, item)`: $O(\log n)$

---

## Operations Limit (1-Second Rule of Thumb for Online Judges)
In competitive programming and coding platforms (LeetCode, Codeforces), execution time limit is typically 1.0 to 2.0 seconds (~$10^8$ operations in C++, ~$10^7$ operations in Python).

| Input Size ($N$) | Feasible Time Complexity | Target Algorithms |
| :--- | :--- | :--- |
| $N \le 10$ | $O(n!)$ | Permutations, brute force backtracking |
| $N \le 20$ | $O(2^n)$ | Subsets, bitmask DP |
| $N \le 100$ | $O(n^4)$ | Floyd-Warshall variants, 4-nested loops |
| $N \le 500$ | $O(n^3)$ | Matrix multiplication, 3D DP, Floyd-Warshall |
| $N \le 5000$ | $O(n^2)$ | 2D DP, nested loops, bubble/selection/insertion sort |
| $N \le 10^5 \sim 10^6$ | $O(n \log n)$ or $O(n)$ | Sorting, heaps, binary search, two pointers, sliding window |
| $N \ge 10^9$ | $O(\log n)$ or $O(1)$ | Binary search on answer space, math, GCD, fast exponentiation |
