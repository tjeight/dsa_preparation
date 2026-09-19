"""Python Tuple (tuple) Operations, Immutability, and Reference.

A Python tuple is an IMMUTABLE, ordered sequence of elements. Once constructed,
its size and elements cannot be modified, appended, or removed.

Why Use Tuples in DSA?
----------------------
1. Hashability: Unlike lists, tuples containing only immutable items are
   HASHABLE. This makes them ideal as dictionary keys and set elements
   (e.g., storing 2D grid coordinates (row, col) in visited sets or DP memo).
2. Memory Efficiency: Tuples are stored in a single fixed block of memory,
   consuming less memory overhead than dynamic lists.
3. Data Integrity: Tuples prevent accidental mutations when passing read-only
   records, lookup pairs, or coordinates across functions.

Time Complexity Overview:
-------------------------
- Index access (t[i]):            O(1)
- Length (len(t)):                O(1)
- Slicing (t[start:stop]):        O(k) where k is slice length
- Membership check (x in t):      O(n) linear scan
- t.count(x):                     O(n) counts occurrences
- t.index(x):                     O(n) returns first index
- Tuple concatenation (t1 + t2):  O(len(t1) + len(t2)) (allocates a new tuple)
- Tuple repetition (t * k):       O(k * len(t))
- Packing & Unpacking:            O(n)
"""

# ============================================================================
# 1. INITIALIZATION & SYNTAX QUIRKS
# ============================================================================

# Tuples are defined using parentheses '()' or comma-separated values (packing).
new_tuple = (1, 2, 34, 5)
print(f"Original tuple: {new_tuple}")

# SYNTAX QUIRK - Single Element Tuple:
# - A single element inside parentheses without a comma is evaluated as that type:
not_a_tuple = (42)    # <class 'int'>
is_a_tuple = (42,)    # <class 'tuple'> (trailing comma is REQUIRED)
print(f"(42) is {type(not_a_tuple)}, but (42,) is {type(is_a_tuple)}")

# Empty tuple:
empty_tuple = ()      # or tuple()
print(f"Empty tuple: {empty_tuple}")


# ============================================================================
# 2. INDEX ACCESS & SLICING
# ============================================================================

# Index access:
# - 0-indexed from the left (0 to n - 1), negative-indexed from the right (-1 to -n).
# - Time Complexity: O(1)
print(f"First element (new_tuple[0]): {new_tuple[0]}")
print(f"Last element (new_tuple[-1]): {new_tuple[-1]}")

# Slicing:
# - Returns a NEW tuple with the sliced elements.
# - Time Complexity: O(k) where k is slice length
print(f"Slice [1:3]: {new_tuple[1:3]}")
print(f"Reversed tuple (new_tuple[::-1]): {new_tuple[::-1]}")


# ============================================================================
# 3. IMMUTABILITY CAVEAT
# ============================================================================

# Tuples cannot be modified in-place:
# - new_tuple[0] = 99  -> Raises TypeError:
#   'tuple' object does not support item assignment.

# CAVEAT: If a tuple contains a MUTABLE object (e.g., a list), the inner list
# can be mutated, but the tuple's reference to that list remains fixed.
hybrid_tuple = (1, [10, 20], 3)
hybrid_tuple[1].append(30)
print(f"Tuple with mutated inner list: {hybrid_tuple}")
# Note: hybrid_tuple is NOT hashable because it contains an unhashable list!


# ============================================================================
# 4. BUILT-IN TUPLE METHODS (count() & index())
# Tuples only possess TWO built-in methods because of their immutability.
# ============================================================================

# count(value): Returns the number of times 'value' appears in the tuple.
# - Time Complexity: O(n) (scans every element from start to end)
# - Output: 1 (1 appears once)
print(f"Count of 1 in new_tuple: {new_tuple.count(1)}")

# index(value, [start, [stop]]): Returns the lowest 0-based index of 'value'.
# - Raises ValueError if the element is not found.
# - Time Complexity: O(n) linear search
# - Output: 2 (34 is located at index 2)
print(f"Index of 34 in new_tuple: {new_tuple.index(34)}")


# ============================================================================
# 5. TUPLE PACKING & UNPACKING (DESTRUCTURING)
# Widely used in Python DSA for multiple returns, swapping, and coordinate parsing.
# ============================================================================

# Tuple Unpacking:
a, b, c, d = new_tuple
print(f"Unpacked values: a={a}, b={b}, c={c}, d={d}")

# Extended Unpacking with * (starred expression):
first, *middle, last = new_tuple
print(f"Starred unpacking -> first: {first}, middle: {middle}, last: {last}")

# In-Place Variable Swapping (uses tuple packing/unpacking behind the scenes):
x, y = 10, 20
x, y = y, x  # (y, x) is packed into a tuple, then unpacked into x, y
print(f"Swapped variables: x={x}, y={y}")


# ============================================================================
# 6. DSA APPLICATION: HASHABLE KEYS (MEMOIZATION & VISITED SETS)
# ============================================================================

# In Graph and Grid DP problems (e.g., BFS, DFS, Dijkstra, Grid Unique Paths):
# Lists cannot be set elements or dict keys, but tuples CAN!
visited: set[tuple[int, int]] = set()
visited.add((0, 0))
visited.add((1, 2))
print(f"Visited grid coordinates set: {visited}")
print(f"Is (1, 2) visited?: {(1, 2) in visited}")

# Memoization dictionary with coordinate tuple key:
memo: dict[tuple[int, int], int] = {}
memo[(0, 0)] = 1
memo[(1, 1)] = 2
print(f"Memoized DP states: {memo}")
