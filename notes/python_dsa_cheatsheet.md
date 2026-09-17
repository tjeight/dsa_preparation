# Python DSA Standard Library Cheatsheet

Quick reference for essential modules in Python when solving DSA problems.

---

## 1. `collections`
```python
from collections import Counter, defaultdict, deque

# Double-ended queue for BFS and sliding windows
dq = deque([1, 2, 3])
dq.append(4)  # right
dq.appendleft(0)  # left
dq.pop()  # right
dq.popleft()  # left

# Defaultdict avoids KeyError
graph = defaultdict(list)
graph[1].append(2)

# Counter for frequencies
counts = Counter("leetcode")
top_freq = counts.most_common(2)
```

---

## 2. `heapq` (Min-Heap by default)
```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)  # 2

# Max-heap trick: invert sign
heapq.heappush(heap, -val)
val = -heapq.heappop(heap)

# Heapify an existing list in O(n)
arr = [5, 1, 9, 3]
heapq.heapify(arr)
```

---

## 3. `bisect` (Binary Search)
```python
import bisect

arr = [1, 2, 4, 4, 4, 7, 9]

# First index >= x
left_idx = bisect.bisect_left(arr, 4)  # 2

# First index > x
right_idx = bisect.bisect_right(arr, 4)  # 5
```

---

## 4. `functools.cache` (Memoization for DP)
```python
from functools import cache


@cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

## 5. `math`
```python
import math

gcd = math.gcd(a, b)
lcm = math.lcm(a, b)
infinity = math.inf
comb = math.comb(n, k)
```
