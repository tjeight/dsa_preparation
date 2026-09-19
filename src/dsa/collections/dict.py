"""Python Dictionary (Hash Map / Associative Array) Operations and Reference.

A Python dictionary is a mutable, ordered mapping that stores data in key-value
pairs. Internally, it is implemented as a highly optimized hash table:
- Since Python 3.6+ (guaranteed in 3.7+), dicts maintain insertion order.
- Keys must be hashable and immutable (e.g., int, float, str, tuple).
- Mutable types (list, dict, set) cannot be used as dictionary keys.

Time Complexity Overview:
-------------------------
- Key lookup (d[k]):            Average O(1), Worst O(n)
- Key assignment (d[k] = v):    Average O(1), Worst O(n)
- Key deletion (del d[k]):      Average O(1), Worst O(n)
- Membership check ('k' in d):  Average O(1), Worst O(n)
- d.get(k, default):            Average O(1), Worst O(n)
- d.setdefault(k, default):     Average O(1), Worst O(n)
- d.pop(k):                     Average O(1), Worst O(n)
- d.popitem():                  O(1) (removes last inserted LIFO pair)
- d.update(other):              O(m) where m is len(other)
- d.keys(), d.values():         O(1) view object creation, O(n) to iterate
- d.items():                    O(1) view object creation, O(n) to iterate
- d.copy():                     O(n) shallow copy
- d.clear():                    O(n) clears all entries
"""

# ============================================================================
# 1. INITIALIZATION & KEY-VALUE STORAGE
# ============================================================================

# Initial dictionary creation with two key-value pairs:
# - Keys: "1" (str), "2" (str)
# - Values: "one" (str), 2 (int)
new_dict = {"1": "one", "2": 2}


# ============================================================================
# 2. ACCESSING VALUES BY KEY
# ============================================================================

# Direct subscript access d[key]:
# - Hashes the key "1", finds the bucket index, and retrieves its value.
# - Time Complexity: Average O(1), Worst O(n) (hash collisions)
# - Note: Raises KeyError if the requested key does not exist.
# - Output: 'one'
print(new_dict["1"])


# ============================================================================
# 3. ADDING & UPDATING ELEMENTS
# ============================================================================

# update([other]): Merges key-value pairs from another dict or iterable of pairs.
# - If a key already exists, its value is overwritten.
# - If a key does not exist, a new key-value pair is inserted.
# - Time Complexity: O(m) where m is the size of the dictionary being merged.
# - State after operation: {'1': 'one', '2': 2, '5': 5}
new_dict.update({"5": 5})


# ============================================================================
# 4. SHALLOW COPYING (copy())
# ============================================================================

# copy(): Creates and returns a shallow copy of the dictionary.
# - The new dictionary has its own independent hash table.
# - Modifying top-level keys in 'copied_dict' does NOT affect 'new_dict'.
# - Time Complexity: O(n)
# - Space Complexity: O(n)
copied_dict = new_dict.copy()
print(f"old dict: {new_dict}")
print(f"new dict: {copied_dict}")

# Changing the copied dictionary demonstrates independence:
# - Adding 'new': 55 to copied_dict will leave new_dict intact.
copied_dict.update({"new": 55})
print(f"new dict (after update): {copied_dict}")
print(f"old dict (remains unchanged): {new_dict}")


# ============================================================================
# 5. CREATING DICTIONARIES WITH fromkeys()
# ============================================================================

# fromkeys(iterable, [value]): Class method that creates a new dictionary with
# keys from the given iterable and all values set to 'value' (default: None).
# - "1" is an iterable of 1 character -> creates {'1': None}.
# - If called like dict.fromkeys(["a", "b", "c"], 0) -> {'a': 0, 'b': 0, 'c': 0}.
# - Time Complexity: O(k) where k is the length of the iterable.
keys = new_dict.fromkeys("1")


# ============================================================================
# 6. DICTIONARY VIEW OBJECTS (keys(), values(), items())
# View objects provide dynamic, read-only windows into dict entries.
# If the dictionary changes, the view immediately reflects those changes.
# ============================================================================

# keys(): Returns a dict_keys view object containing all keys.
# - Supports set-like operations (union, intersection).
# - Time Complexity: O(1) to create the view, O(n) to convert to list.
get_all_keys = new_dict.keys()
print(list(get_all_keys))

# values(): Returns a dict_values view object containing all values.
# - Time Complexity: O(1) to create the view, O(n) to convert to list.
values = new_dict.values()
print(list(values))


# ============================================================================
# 7. SAFE RETRIEVAL WITH get()
# ============================================================================

# get(key, [default]): Retrieves value for 'key' without raising KeyError.
# - If 'key' exists: returns its associated value.
# - If 'key' does not exist: returns 'default' (or None if default not provided).
# - Key "9" is not present in new_dict -> returns fallback default value: 0.
# - Time Complexity: Average O(1), Worst O(n).
print(new_dict.get("9", 0))


# ============================================================================
# 8. CONDITIONAL DEFAULT INSERTION WITH setdefault()
# ============================================================================

# setdefault(key, default): Look up a key; insert with 'default' if absent.
# - If 'key' is in the dictionary: returns its existing value.
# - If 'key' is NOT in the dictionary: inserts 'key' with 'default' and returns it.
# - Ideal for grouping and graph adjacency list initialization in DSA:
#   graph.setdefault(node, []).append(neighbor)
# - Here, "555" is absent -> inserts "555": [] and prints [].
# - State after operation: {'1': 'one', '2': 2, '5': 5, '555': []}
print("setdefault:", new_dict.setdefault("555", []))


# ============================================================================
# 9. REMOVING ELEMENTS (pop(), popitem(), clear())
# ============================================================================

# pop(key, [default]): Removes 'key' and returns its corresponding value.
# - If 'key' is found: deletes it and returns the value.
# - If 'key' is not found: returns 'default' (raises KeyError if no default given).
# - Here, key "555" is removed (returned value was []).
# - Time Complexity: Average O(1), Worst O(n).
# - State after operation: {'1': 'one', '2': 2, '5': 5}
new_dict.pop("555")

# popitem(): Removes and returns the LAST inserted (key, value) pair (LIFO order).
# - Guaranteed LIFO order since Python 3.7.
# - Raises KeyError if the dictionary is empty.
# - Here, removes the last inserted pair: ("5", 5).
# - Time Complexity: O(1).
# - State after operation: {'1': 'one', '2': 2}
new_dict.popitem()

# Print remaining dictionary: {'1': 'one', '2': 2}
print(new_dict)

# Print keys dictionary created earlier from fromkeys: {'1': None}
print(keys)

# clear(): Removes all key-value pairs from the dictionary in-place.
# - Leaves the dictionary empty: {}
# - Time Complexity: O(n) (frees all internal hash table entries)
new_dict.clear()
