"""Problem: Check if a String is a Palindrome Using Recursion.

A string is a palindrome if it reads the same forward and backward.
Examples: "madam" -> True, "racecar" -> True, "hello" -> False.

Strategy Implemented (Reverse and Compare):
-------------------------------------------
1. Helper function `reverse_string(string)`:
   - Base Case: Empty string returns "".
   - Recursive Step: Extracts the last character `string[-1]` and prepends it
     to the recursively reversed prefix `string[:-1]`.
2. Main function `check_palindrome(string)`:
   - Reverses the string using the helper.
   - Compares the reversed string against the original string.
   - If `reversed == original`, returns True; otherwise False.

Call Stack Trace for Reversing "madam":
---------------------------------------
Descent Phase (Pushing frames):
| reverse_string("")      | -> Base Case reached (returns "")
| reverse_string("m")     | -> Waits for reverse("") to evaluate 'm' + ""
| reverse_string("ma")    | -> Waits for reverse("m") to evaluate 'a' + "m"
| reverse_string("mad")   | -> Waits for reverse("ma") to evaluate 'd' + "am"
| reverse_string("mada")  | -> Waits for reverse("mad") to evaluate 'a' + "dam"
| reverse_string("madam") | -> Waits for reverse("mada") to evaluate 'm' + "adam"
+-------------------------+
Unwinding Phase (Evaluating string concatenations):
- Evaluates back up to "madam"
- Final Comparison: "madam" == "madam" -> True

Complexity Analysis (Current Implementation):
---------------------------------------------
- Time Complexity:  O(N^2)
  - Reversing via slicing (`string[:-1]`) and string concatenation takes
    N + (N - 1) + ... + 1 = O(N^2) time.
  - Final string comparison takes O(N) time.
  - Overall Time Complexity: O(N^2).
- Space Complexity: O(N^2) total memory allocated for intermediate sliced
  and concatenated strings (O(N) active call stack depth).

DSA Optimization Note (Two-Pointer In-Place Recursion):
-------------------------------------------------------
In interview settings (e.g. LeetCode 125), reversing the whole string is
unnecessary. A more optimal recursive approach compares outer characters
and narrows inward:
    def is_palindrome_optimal(self, s: str, left: int = 0, right: int = None):
        if right is None:
            right = len(s) - 1
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return self.is_palindrome_optimal(s, left + 1, right - 1)
- Time Complexity:  O(N) (at most N/2 comparisons)
- Space Complexity: O(N) call stack frames (or O(1) iteratively)
"""


class RecursionProblems:
    """Collection of recursive string and array manipulation algorithms."""

    def reverse_string(self, string: str):
        """Recursively reverse 'string' using tail extraction and slicing."""
        # Base Case: An empty string reversed is an empty string
        if len(string) == 0:
            return ""

        # Recursive Step: Prepend last character to reversed remainder
        return string[-1] + self.reverse_string(string=string[:-1])

    def check_palindrome(self, string: str) -> bool:
        """Check if 'string' is a palindrome by comparing with its reverse."""
        # Compare the recursively reversed string with the original string
        if self.reverse_string(string=string) == string:
            return True
        else:
            return False


# Instantiate the problem solver class
recursion_problems = RecursionProblems()


# Test with the palindrome string "madam"
print(recursion_problems.check_palindrome("madam"))
