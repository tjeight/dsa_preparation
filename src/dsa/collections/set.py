"""Python Set Operations and Reference.

A Python set is a mutable, UNORDERED collection of UNIQUE, hashable elements.
Internally, it is implemented as a hash table (analogous to a dictionary with
keys only and dummy values).

Key Characteristics:
--------------------
- Unordered: Elements have no index or guaranteed sequence.
- Unique: Duplicate elements are automatically discarded.
- Fast Lookups: Average O(1) membership testing ('in' operator).
- Element Constraints: Elements MUST be hashable and immutable
  (e.g., int, float, str, tuple, frozenset). Lists, dicts, and sets cannot
  be stored inside a set.

Time Complexity Overview:
-------------------------
- Add element (s.add(x)):             Average O(1), Worst O(n)
- Remove element (s.remove(x)):       Average O(1), Worst O(n)
- Discard element (s.discard(x)):     Average O(1), Worst O(n)
- Pop arbitrary (s.pop()):            Average O(1), Worst O(n)
- Membership test (x in s):           Average O(1), Worst O(n)
- Copy set (s.copy()):                O(n)
- Clear set (s.clear()):              O(n)
- Union (s | t or s.union(t)):        O(len(s) + len(t))
- Intersection (s & t):               O(min(len(s), len(t)))
- Difference (s - t):                 O(len(s))
- Symmetric Diff (s ^ t):             O(len(s) + len(t))
- Subset test (s.issubset(t)):        O(len(s))
- Superset test (s.issuperset(t)):    O(len(t))
- Disjoint test (s.isdisjoint(t)):    O(min(len(s), len(t)))
"""

# ============================================================================
# 1. INITIALIZATION & DEDUPLICATION
# ============================================================================

# IMPORTANT SYNTAX NOTE:
# - A set literal with values is created using curly braces: {1, 2, 3}.
# - An EMPTY set MUST be created using set(), NOT {}!
#   {} creates an empty dictionary (dict), not a set.
empty_set = set()      # Correct way to instantiate an empty set (<class 'set'>)
empty_dict = {}        # Note: creates an empty dictionary (<class 'dict'>)

# Deduplication: Duplicate values (1 and 5) are automatically eliminated.
# Resulting set contains only unique elements: {1, 2, 3, 5, 9}
numbers = {1, 2, 1, 3, 5, 9, 5}
print("Initial set (duplicates removed):", numbers)


# ============================================================================
# 2. ADDING & REMOVING ELEMENTS
# ============================================================================

# add(element): Inserts a single element into the set.
# - Sets are UNORDERED: the element is placed based on its hash value, NOT at the end.
# - If the element already exists, the set remains unchanged (no error).
# - Time Complexity: Average O(1), Worst O(n)
# - State after operation: {1, 2, 3, 5, 9, 10}
numbers.add(10)

# remove(element): Deletes the specified element from the set.
# - CAUTION: Raises KeyError if 'element' is not present in the set.
# - Time Complexity: Average O(1), Worst O(n)
# - State after operation: {1, 2, 3, 9, 10} (5 is removed)
numbers.remove(5)


# ============================================================================
# 3. SHALLOW COPYING (copy())
# ============================================================================

# copy(): Creates a new shallow copy of the set with its own hash table.
# - Modifying 'copied_set' does not mutate 'numbers'.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
copied_set = numbers.copy()

print("Original set:", numbers)
print("Copied set:  ", copied_set)


# ============================================================================
# 4. DIFFERENCE & DISCARD (SAFE REMOVAL)
# ============================================================================

# Create a second set with duplicates (55 and 59 deduplicated): {55, 59, 555}
difference_set = {555, 55, 55, 59, 59}

# difference(other) or (s - other):
# - Returns a new set with elements that are in 'numbers' but NOT in 'difference_set'.
# - Time Complexity: O(len(numbers))
print("Difference set (numbers - difference_set):", numbers.difference(difference_set))

# discard(element): Safely removes 'element' from the set.
# - KEY DIFFERENCE from remove(): discard() does NOT raise an error
#   if the element is absent!
# - Time Complexity: Average O(1), Worst O(n)
difference_set.discard(555)
print("difference_set after discard(555):", difference_set)

# Subsequent discard of the same absent element will silently succeed without error:
difference_set.discard(555)

# Membership test ('in' operator):
# - Uses hashing for immediate lookup instead of scanning all elements sequentially.
# - Time Complexity: Average O(1), Worst O(n)
# - Output: False (since 555 was discarded)
print("Is 555 in difference_set?:", 555 in difference_set)


# ============================================================================
# 5. CLEARING A SET (clear())
# ============================================================================

# clear(): Empties the set in-place, removing all elements.
# - Leaves the set empty: set()
# - Time Complexity: O(n)
numbers.clear()

# An empty set prints as 'set()' (to distinguish from empty dict '{}'):
print("numbers after clear():", numbers)

# type(numbers) confirms it is still an instance of <class 'set'>:
print("Type of numbers:", type(numbers))


# ============================================================================
# 6. MATHEMATICAL SET OPERATIONS (Venn Diagram Operations)
# ============================================================================

first_set = {10, 20, 30, 40, 50}
second_set = {60, 70, 80, 90, 100}

# UNION (| or .union()):
# - Elements present in first_set, second_set, or both.
# - Time Complexity: O(len(first_set) + len(second_set))
# - Output: {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
print("Union (first_set | second_set):", first_set | second_set)

# INTERSECTION (& or .intersection()):
# - Elements common to BOTH sets.
# - Since first_set and second_set share no elements, this produces an empty set().
# - Time Complexity: O(min(len(first_set), len(second_set)))
# - Output: set()
print("Intersection (first_set & second_set):", first_set & second_set)

# DIFFERENCE (- or .difference()):
# - Elements in first_set that are NOT in second_set.
# - Time Complexity: O(len(first_set))
# - Output: {10, 20, 30, 40, 50}
print("Difference (first_set - second_set):", first_set - second_set)

# SYMMETRIC DIFFERENCE (^ or .symmetric_difference()):
# - Elements in either first_set or second_set, but NOT in both (XOR operation).
# - Time Complexity: O(len(first_set) + len(second_set))
# - Output: All elements combined except common ones
print("Symmetric Difference (first_set ^ second_set):", first_set ^ second_set)


# ============================================================================
# 7. POPPING & SUBSET CHECKS
# ============================================================================

# pop(): Removes and returns an ARBITRARY element from the set.
# - Because sets are unordered, you CANNOT predict which element is popped.
# - Raises KeyError if the set is empty.
# - Time Complexity: Average O(1), Worst O(n)
popped_element = first_set.pop()
print(f"Popped element: {popped_element}")
print("first_set after pop():", first_set)

# issubset(other):
# - Returns True if every element of first_set is contained within second_set.
# - Equivalent operator: first_set <= second_set
# - Time Complexity: O(len(first_set))
# - Output: False
print("Is first_set subset of second_set?:", first_set.issubset(second_set))

# isdisjoint(other):
# - Returns True if two sets have NO elements in common (intersection is empty).
# - Time Complexity: O(min(len(first_set), len(second_set)))
# - Output: True
print("Are sets disjoint?:", first_set.isdisjoint(second_set))
