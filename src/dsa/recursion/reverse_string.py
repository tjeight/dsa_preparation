"""Problem: Reverse a String Using Recursion.

Given a string 'string', reverse the order of its characters using recursive
decomposition.

Example:
    Input:  string = "Tejas"
    Output: "sajeT"

Recursion Strategy (Tail Extraction via Slicing):
-------------------------------------------------
1. Base Case:
   `if len(string) == 0: return ""`
   An empty string reversed is an empty string.

2. Recursive Step:
   `string[-1] + self.reverse_string(string[:-1])`
   Takes the last character `string[-1]` and prepends it to the recursively
   reversed prefix slice `string[:-1]` (everything except the last character).
   The character concatenations occur during the call stack UNWINDING phase.

Call Stack Lifecycle Trace (for string = "Tejas"):
--------------------------------------------------
Descent Phase (Pushing stack frames):
| reverse_string("")      | -> Base Case reached (returns "")
| reverse_string("T")     | -> Waits for reverse("") to evaluate 'T' + ""
| reverse_string("Te")    | -> Waits for reverse("T") to evaluate 'e' + "T"
| reverse_string("Tej")   | -> Waits for reverse("Te") to evaluate 'j' + "eT"
| reverse_string("Teja")  | -> Waits for reverse("Tej") to evaluate 'a' + "jeT"
| reverse_string("Tejas") | -> Waits for reverse("Teja") to evaluate 's' + "ajeT"
+-------------------------+
Unwinding Phase (Evaluating string concatenations):
- reverse("") returns ""
- reverse("T") returns 'T' + "" = "T"
- reverse("Te") returns 'e' + "T" = "eT"
- reverse("Tej") returns 'j' + "eT" = "jeT"
- reverse("Teja") returns 'a' + "jeT" = "ajeT"
- reverse("Tejas") returns 's' + "ajeT" = "sajeT" -> Final output

Complexity Analysis (Current Slicing Approach):
-----------------------------------------------
- Time Complexity:  O(N^2)
  - There are N + 1 recursive calls.
  - Slicing `string[:-1]` and string concatenation (`+`) both create new
    string allocations of size O(k) at each level.
  - Total work: N + (N - 1) + ... + 1 = O(N^2).
- Space Complexity: O(N^2) total memory allocated for intermediate sliced
  and concatenated strings (O(N) active call stack depth).

DSA Optimization Note (Two-Pointer In-Place Swap on List):
----------------------------------------------------------
In Python, strings are immutable. For optimal O(N) time and O(N) auxiliary
space (LeetCode 344), convert the string to a list of characters and swap in-place:
    def reverse_helper(self, chars: list, left: int, right: int) -> None:
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        self.reverse_helper(chars, left + 1, right - 1)
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def reverse_string(self, string: str) -> str:
        """Reverse a string recursively using tail extraction and slicing."""
        # Base Case: Reversing an empty string yields an empty string
        if len(string) == 0:
            return ""

        # Recursive Step: Last character + reversed remainder of the string
        return string[-1] + self.reverse_string(string[:-1])


# Example input string
string = "Tejas"

# Instantiate the problem solver class
recursion_problems = RecursionProblems()

# Compute and output the reversed string
print(recursion_problems.reverse_string(string))
