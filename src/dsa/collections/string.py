"""Python String (str) Operations, Immutability, and Reference.

A Python string is an IMMUTABLE sequence of Unicode characters. Once created,
individual characters cannot be modified in-place. Any operation that appears
to alter a string returns an entirely new string object.

CPython Memory Model & Immutability:
------------------------------------
- Strings are stored in contiguous memory as arrays of bytes or code points.
- Small strings and string literals may be interned by Python for memory reuse.
- In-place mutation (e.g., s[0] = 'a') raises a TypeError.

DSA CRITICAL PERFORMANCE NOTE:
------------------------------
Repeated string concatenation inside loops (s += char) takes O(n^2) time
because a new string of increasing length is allocated and copied in every
iteration!
-> OPTIMAL DSA PATTERN: Accumulate characters in a list, then call ''.join(list)
   which takes O(n) linear time.

Time Complexity Overview:
-------------------------
- Index access (s[i]):             O(1)
- Length (len(s)):                 O(1) (stored in object header)
- Slicing (s[start:stop]):         O(k) where k is the slice length
- String concatenation (s1 + s2):  O(len(s1) + len(s2))
- Character search (c in s):       O(n) linear scan
- Substring search (sub in s):     O(n + m) (Boyer-Moore-Horspool algorithm)
- s.find(sub), s.index(sub):       O(n * m) worst case, O(n + m) average
- s.count(sub):                    O(n)
- s.startswith(), s.endswith():    O(k) where k is prefix/suffix length
- s.split(sep):                    O(n)
- sep.join(iterable):              O(total length of all strings)
- s.strip(), s.replace():          O(n)
- s.upper(), s.lower():            O(n)
- ord(c), chr(code):               O(1)
- Character predicates (isalnum):  O(n)
"""

# ============================================================================
# 1. INITIALIZATION & INDEX ACCESS
# ============================================================================

# Strings can be enclosed in either single quotes ('...') or double quotes ("...").
# Triple quotes ('''...''' or \"\"\"...\"\"\") allow multiline strings.
name = "Tejas"

# Direct index access s[index]:
# - Strings are 0-indexed: index 0 corresponds to the first character ('T').
# - Negative indexing is supported: index -1 refers to the last character ('s').
# - Time Complexity: O(1) direct pointer offset
print(f"First character (name[0]): {name[0]}")


# ============================================================================
# 2. STRING ITERATION
# ============================================================================

# Strings are iterable sequences: a for-loop traverses character by character.
# - Time Complexity: O(n) where n = len(name)
print("Iterating over characters:")
for i in name:
    print(i)


# ============================================================================
# 3. STRING SLICING (SHALLOW COPIES)
# Slicing Syntax: string[start:stop:step]
# - 'start' is inclusive (default: 0)
# - 'stop' is exclusive (default: len(string))
# - 'step' is stride and direction (default: 1)
# - Always creates and returns a NEW string in O(k) time (k = slice length).
# ============================================================================

# Omitting stop index: name[0:] extracts from index 0 to the end -> 'Tejas'
print(f"Slice from index 0 to end (name[0:]): {name[0:]}")

# Reversing a string using negative step:
# - start=-1 (starts at last character), stop omitted, step=-1 (walks backwards).
# - Produces reversed copy: 'sajeT'
# - Standard Python idiom for string reversal: name[::-1] or name[-1::-1]
print(f"Reversed string (name[-1::-1]): {name[-1::-1]}")

# Slicing with specific range [start:stop]:
# - name[1:5] extracts indices 1, 2, 3, 4 (excludes index 5).
# - Extracts characters 'e', 'j', 'a', 's' -> 'ejas'
print(f"Slice [1:5] (excluding index 5): {name[1:5]}")


# ============================================================================
# 4. IMMUTABILITY, SPLITTING & JOINING
# ============================================================================

new_string = "Tejas,is a software developer"

# String Immutability Demo:
# - Attempting new_string[0] = 't' would raise TypeError:
#   'str' object does not support item assignment.

# split(sep): Splits the string at each occurrence of 'sep' and returns a list.
# - If 'sep' is omitted, it splits by arbitrary consecutive whitespace.
# - Time Complexity: O(n)
# - Output: ['Tejas', 'is a software developer']
print(f"Splitting by comma: {new_string.split(',')}")

# sep.join(iterable): Joins elements of an iterable into a single string.
# - 'sep' is placed between each element.
# - Far more efficient than repeated concatenation: allocates memory once.
# - Time Complexity: O(total length of all strings)
updated_ = " joined ".join((new_string.split(",")))
print(f"Joined string: {updated_}")


# ============================================================================
# 5. WHITESPACE TRIMMING & SUBSTRING REPLACEMENT
# ============================================================================

strip_string = "   middle   "

# strip(): Removes leading and trailing whitespace (spaces, tabs, newlines).
# - lstrip() removes leading whitespace only; rstrip() removes trailing only.
# - Time Complexity: O(n)
print(f"Stripped string: '{strip_string.strip()}'")

# replace(old, new, [count]): Replaces occurrences of 'old' with 'new'.
# - Strings are immutable: returns a new string without modifying the original.
# - Chaining methods: .replace(...).strip() replaces then trims.
# - Time Complexity: O(n)
print(f"Replaced and stripped: '{strip_string.replace('middle', 'changed').strip()}'")


# ============================================================================
# 6. SEARCHING, COUNTING & PREFIX/SUFFIX CHECKS
# ============================================================================

# find(substring): Returns the lowest 0-based index of 'substring'.
# - Returns -1 if 'substring' is NOT found (safe check).
# - KEY DIFFERENCE from index(): index() raises ValueError if substring is absent!
# - Time Complexity: O(n + m) average
print(f"First occurrence index of 'joined': {updated_.find('joined')}")

# count(substring): Counts the number of non-overlapping occurrences.
# - Time Complexity: O(n)
print(f"Count of 'joined': {updated_.count('joined')}")

# startswith(prefix) / endswith(suffix):
# - Returns True if the string begins with 'prefix' or ends with 'suffix'.
# - Time Complexity: O(k) where k = len(prefix/suffix)
# - "Tejass" != "Tejas" -> Returns False
print(f"Starts with 'Tejass': {updated_.startswith('Tejass')}")

# Deliberate typo check: "developesr" does not match "developer" -> Returns False
print(f"Ends with 'developesr': {updated_.endswith('developesr')}")


# ============================================================================
# 7. CASE TRANSFORMATIONS & LEXICOGRAPHICAL COMPARISONS
# ============================================================================

# upper(): Converts all lowercase characters to uppercase.
# - Time Complexity: O(n)
print(f"Uppercase: {updated_.upper()}")

# lower(): Converts all uppercase characters to lowercase.
# - Time Complexity: O(n)
print(f"Lowercase: {updated_.lower()}")

# String equality (==):
# - Compares character by character based on Unicode code points.
# - Case-sensitive: 'T' (ASCII 84) != 't' (ASCII 116) -> False
print(f"Case-sensitive equality ('Tejas' == 'tejas'): {'Tejas' == 'tejas'}")


# ============================================================================
# 8. CHARACTER ENCODINGS & CHARACTER PREDICATES
# ============================================================================


# ord(character): Returns the integer Unicode code point / ASCII value of a char.
# - Time Complexity: O(1)
# - ord('a') = 97, ord('A') = 65, ord('0') = 48
print(f"ASCII value of 'a' (ord('a')): {ord('a')}")

# chr(code): Inverse of ord(); returns the character for a given Unicode code.
# - Time Complexity: O(1)
# - chr(97) = 'a'
print(f"Character for ASCII 97 (chr(97)): {chr(97)}")

# Character validation predicates:
# - isalnum(): True if all characters are alphanumeric (letters or digits).
# - isalpha(): True if all characters are alphabetic letters.
# - isdigit(): True if all characters are numeric digits.
# - isspace(): True if all characters are whitespace.
# - Time Complexity: O(n)
print(f"Is 'Tejas123' alphanumeric?: {'Tejas123'.isalnum()}")
