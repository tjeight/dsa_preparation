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

### `list`
- Index / Assign: $O(1)$
- Append: Amortized $O(1)$
- Pop from end: $O(1)$
- Pop from front / Insert at index $i$: $O(n)$
- Slice `arr[a:b]`: $O(b - a)$
- `in` check: $O(n)$
- Reverse: $O(n)$
- Sort (Timsort): $O(n \log n)$

### `collections.deque`
- Append / Appendleft: $O(1)$
- Pop / Popleft: $O(1)$
- Access by index: $O(n)$

### `dict` & `set`
- Insert / Update: Average $O(1)$, Worst $O(n)$
- Lookup / Delete: Average $O(1)$, Worst $O(n)$
- Iteration: $O(n)$

### `heapq`
- `heappush(heap, item)`: $O(\log n)$
- `heappop(heap)`: $O(\log n)$
- `heapify(list)`: $O(n)$
- `heappushpop(heap, item)`: $O(\log n)$

---

## Operations Limit (1 Second Rule of Thumb for Contests & Online Judges)
- $N \le 10$: $O(n!)$
- $N \le 20$: $O(2^n)$
- $N \le 500$: $O(n^3)$
- $N \le 5000$: $O(n^2)$
- $N \le 10^5 \sim 10^6$: $O(n \log n)$ or $O(n)$
- $N \ge 10^9$: $O(\log n)$ or $O(1)$
