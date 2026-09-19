"""Python List (Dynamic Array) Operations and Reference.

A Python list is a mutable, ordered sequence of elements stored contiguously
in memory as an array of pointers. It provides O(1) random access by index
and amortized O(1) appending at the end.

Time Complexity Overview:
-------------------------
- Index access / assignment:   O(1)
- Append (at end):             O(1) amortized
- Insert (at arbitrary index): O(n) (requires shifting elements right)
- Remove by value:             O(n) (linear search + shifting elements left)
- Pop (from end):              O(1)
- Pop (from arbitrary index):  O(n) (requires shifting elements left)
- In-place Sort (Timsort):     O(n log n) time, O(n) space
- In-place Reverse:            O(n)
- Slicing [start:stop]:        O(k) where k is the slice length
- Membership check (x in list):O(n) (linear scan from start to end)
"""

# ============================================================================
# 1. INITIALIZATION
# ============================================================================
# Initial list creation with 6 integer elements.
# Memory: Allocated as a contiguous array of pointers to integer objects.
numbers: list = [1, 2, 3, 4, 5, 6]


# ============================================================================
# 2. ADDING & INSERTING ELEMENTS
# ============================================================================

# append(element): Adds the element to the end of the list.
# - Time Complexity: Amortized O(1) (over-allocates memory to minimize resizing)
# - State after operation: [1, 2, 3, 4, 5, 6, 5]
numbers.append(5)

# insert(index, element): Inserts an element at the specified index.
# - Index 0 places the element at the beginning (prepend).
# - Time Complexity: O(n) because all existing elements must shift 1 position right.
# - State after operation: [10, 1, 2, 3, 4, 5, 6, 5]
numbers.insert(0, 10)


# ============================================================================
# 3. REMOVING ELEMENTS
# ============================================================================

# remove(value): Searches for the first occurrence of 'value' and deletes it.
# - Raises ValueError if the value is not present in the list.
# - Time Complexity: O(n) (O(n) to find the element + O(n) to shift remaining elements)
# - State after operation: [10, 1, 2, 3, 4, 5, 5] (first 6 removed)
numbers.remove(6)

# pop(): Removes and returns the element at the given index (defaults to the last item).
# - Popping from the end does not require element shifting.
# - Time Complexity: O(1) from the end; O(n) if popping from any other index.
# - Removed element: 5
# - State after operation: [10, 1, 2, 3, 4, 5]
numbers.pop()


# ============================================================================
# 4. SORTING & REVERSING (IN-PLACE MODIFICATIONS)
# ============================================================================

# sort(): Sorts elements in ascending order in-place using Timsort.
# - Timsort is an adaptive, stable hybrid sorting algorithm
#   (combines Merge Sort and Insertion Sort).
# - Modifies the original list directly and returns None.
# - Time Complexity: O(n log n)
# - Space Complexity: O(n) auxiliary memory
# - State after operation: [1, 2, 3, 4, 5, 10]
numbers.sort()

# sort(reverse=True): Sorts elements in descending order in-place.
# - Time Complexity: O(n log n)
# - State after operation: [10, 5, 4, 3, 2, 1]
numbers.sort(reverse=True)


# reverse(): Reverses the elements of the list in-place using two-pointer swaps.
# - Modifies the original list directly without allocating a new list.
# - Time Complexity: O(n)
# - Space Complexity: O(1)
# - State after operation: [1, 2, 3, 4, 5, 10]
numbers.reverse()


# Print the final mutated list: [1, 2, 3, 4, 5, 10]
print(numbers)


# ============================================================================
# 5. LIST SLICING (SHALLOW COPIES)
# Slicing Syntax: list[start:stop:step]
# - 'start' is inclusive (default: 0)
# - 'stop' is exclusive (default: len(list))
# - 'step' is stride/direction (default: 1)
# - Always creates and returns a NEW list (shallow copy) in O(k) time.
# ============================================================================

# Slicing from index 0 to 5 (exclusive of index 5):
# - Extracts indices 0, 1, 2, 3, 4 -> elements: [1, 2, 3, 4, 5]
# - Excludes index 5 (which holds value 10).
print(numbers[0:5])

# Reversing via slice step:
# - start=-1 (last element), stop omitted, step=-1 (walk backwards).
# - Produces a new reversed list: [10, 5, 4, 3, 2, 1]
# - Note: Unlike numbers.reverse(), this creates a new list without modifying original.
print(numbers[-1::-1])

# Omitting stop index:
# - numbers[0:] extracts from index 0 through the end of the list.
# - Equivalent to numbers[:] which creates a complete shallow copy: [1, 2, 3, 4, 5, 10]
print(numbers[0:])


# ============================================================================
# 6. MEMBERSHIP TESTING
# ============================================================================

# 'in' operator: Performs a linear search across the list.
# - Checks equality (==) for each element from left to right until found or list ends.
# - Time Complexity: O(n) worst-case (contrast with O(1) average lookup in set/dict).
# - Output: True (since 10 is present at index 5)
print(10 in numbers)


# ============================================================================
# 7. LIST COMPREHENSION
# Syntax: [expression for item in iterable if condition]
# - Provides a concise, readable, and optimized way to generate lists.
# - Implemented at C-level in Python, generally faster than equivalent for-loops.
# - Filter condition 'if n % 2 == 0' selects only even numbers.
# - Range(10) produces: 0, 1, 2, ..., 9 -> Even numbers: [0, 2, 4, 6, 8]
# ============================================================================

# Create a list of even numbers from 0 to 9 using comprehension
numers = [n for n in range(10) if n % 2 == 0]


# Syntax reference explanation:
"""[number loop condition]"""
# Output: [0, 2, 4, 6, 8]
print(numers)


# ============================================================================
# 8. TWO-DIMENSIONAL LISTS (MATRICES / GRIDS)
# ============================================================================

# A 2D list is a list containing other lists as its elements (row-major order).
# Representing a 3x3 matrix:
# Row 0: [1, 2, 3]
# Row 1: [4, 5, 6]
# Row 2: [7, 8, 9]
d2 = [[1,2,3],[4,5,6],[7,8,9]]

# Multi-dimensional indexing:
# - First index selects the row: d2[0] -> [1, 2, 3]
# - Second index selects the column within that row: d2[0][0] -> 1
# - Time Complexity: O(1) direct pointer dereference
print(d2[0][0])