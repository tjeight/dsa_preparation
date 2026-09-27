"""Problem: Palindrome Check Using Recursive Two-Boundary Slicing.

A string is a palindrome if it reads the same forward and backward.
This script implements a recursive boundary-checking strategy:
comparing the outermost characters (`string[0]` and `string[-1]`) and
recursively narrowing down to the inner substring (`string[1:-1]`).

Examples:
    "madams" -> False ('m' != 's' on the first comparison)
    "madam"  -> True  ('m' == 'm' -> 'a' == 'a' -> 'd' is base case)
    "racecar"-> True

Recursion Strategy (Boundary Comparison & Shrinking Window):
------------------------------------------------------------
1. Base Case:
   `if len(string) <= 1: return True`
   A string with 0 or 1 character is trivially a palindrome.

2. Mismatch Check (Early Exit):
   `if string[0] != string[-1]: return False`
   If the outermost characters differ, the string cannot be a palindrome.

3. Recursive Step:
   `return self.check_palindrome(string[1:-1])`
   Slices off both the first and last characters and checks the inner substring.

Call Stack Lifecycle Trace (for string = "madams"):
---------------------------------------------------
Call 1: check_palindrome("madams")
- len("madams") = 6 (> 1)
- First char string[0] = 'm', Last char string[-1] = 's'
- 'm' != 's' -> Returns False immediately (no further recursion needed).

Call Stack Lifecycle Trace (for string = "madam"):
--------------------------------------------------
Call 1: check_palindrome("madam") -> 'm' == 'm', calls check_palindrome("ada")
Call 2: check_palindrome("ada")   -> 'a' == 'a', calls check_palindrome("d")
Call 3: check_palindrome("d")     -> len("d") <= 1 -> Base case returns True!
Unwinds: Returns True to Call 2 -> Returns True to Call 1 -> Final True.

Complexity Analysis (Current Slicing Approach):
-----------------------------------------------
- Time Complexity:  O(N^2)
  - There are at most N / 2 recursive calls.
  - Slicing `string[1:-1]` allocates a new string copy of length (k - 2) in
    O(k) time on every step.
  - Total work: N + (N - 2) + (N - 4) + ... + 1 = O(N^2).
- Space Complexity: O(N^2) total memory allocated across slices (O(N) active
  call stack depth).

DSA Optimization Note (Two Explicit Index Pointers):
----------------------------------------------------
In production / LeetCode (e.g. LeetCode 125), slicing strings creates
unnecessary memory overhead. You can achieve optimal O(N) time and O(N) stack
space (or O(1) space iteratively) by passing index pointers:
    def check_palindrome_ptrs(self, s: str, left: int = 0, right: int = None):
        if right is None:
            right = len(s) - 1
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.check_palindrome_ptrs(s, left + 1, right - 1)
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def check_palindrome(self, string: str) -> bool:
        """Recursively check if a string is a palindrome by trimming ends."""
        # Base Case: Single-character or empty strings are palindromes
        if len(string) <= 1:
            return True

        # Early Exit: If boundary characters mismatch, it cannot be a palindrome
        if string[0] != string[-1]:
            return False

        # Recursive Step: Check the inner substring excluding the boundary characters
        return self.check_palindrome(string[1:-1])


# Instantiate the problem solver class
recursion_problems = RecursionProblems()


# Test with the non-palindrome string "madams"
print(recursion_problems.check_palindrome("madams"))