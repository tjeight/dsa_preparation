"""Problem: Check if an Array is Sorted Using Recursion (Tail Slicing).

A list is sorted in non-decreasing (ascending) order if every element is less
than or equal to the element that follows it: numbers[i] <= numbers[i + 1].

Examples:
    [1, 2, 6, 9, 7, 5] -> False (because 9 > 7)
    [1, 2, 3, 4, 5]    -> True  (strictly increasing)
    [1, 2, 2, 4, 5]    -> True  (non-decreasing with duplicates)
    [42]               -> True  (single-element list is trivially sorted)
    []                 -> True  (empty list is vacuously sorted)

Recursive Slicing Strategy:
---------------------------
1. Base Case:
   `if len(numbers) <= 1: return True`
   - A list with 0 or 1 element is inherently sorted.
   - When recursion reaches this point, all preceding adjacent pairs have
     satisfied the non-decreasing condition.

2. Violation Check (Early Exit):
   `if numbers[0] > numbers[1]: return False`
   - Checks the first adjacent pair (`numbers[0]` and `numbers[1]`).
   - If `numbers[0] > numbers[1]`, the sorted order is violated, so recursion
     halts immediately and returns `False` without checking the rest.

3. Recursive Step:
   `return self.check_sorted(numbers[1:])`
   - Slices off the head element (`numbers[0]`) and recursively checks the
     remaining sublist (`numbers[1:]`).

Call Stack Lifecycle Trace (for numbers = [1, 2, 6, 9, 7, 5]):
--------------------------------------------------------------
Call 1: check_sorted([1, 2, 6, 9, 7, 5])
- 1 <= 2 -> Valid. Calls check_sorted([2, 6, 9, 7, 5])

Call 2: check_sorted([2, 6, 9, 7, 5])
- 2 <= 6 -> Valid. Calls check_sorted([6, 9, 7, 5])

Call 3: check_sorted([6, 9, 7, 5])
- 6 <= 9 -> Valid. Calls check_sorted([9, 7, 5])

Call 4: check_sorted([9, 7, 5])
- 9 > 7 -> Violation! Returns False immediately (Early Exit).

Unwinding Phase:
- Call 4 returns False to Call 3.
- Call 3 returns False to Call 2.
- Call 2 returns False to Call 1.
Final Output: False

Call Stack Trace for Sorted Case ([1, 2, 3]):
---------------------------------------------
Call 1: check_sorted([1, 2, 3]) -> 1 <= 2, calls check_sorted([2, 3])
Call 2: check_sorted([2, 3])    -> 2 <= 3, calls check_sorted([3])
Call 3: check_sorted([3])       -> len <= 1 (Base Case reached!) -> True
Unwinds: Returns True all the way back to the top-level caller.

Complexity Analysis (Current Slicing Approach):
-----------------------------------------------
- Time Complexity:  O(N^2) worst case
  - In the worst case (when the array is sorted), there are N recursive calls.
  - Slicing `numbers[1:]` creates a copy of length (k - 1) taking O(k) time.
  - Total time: (N - 1) + (N - 2) + ... + 1 = O(N^2).
  - Best Case: O(1) if the first two elements violate order (numbers[0] > numbers[1]).
- Space Complexity: O(N^2)
  - Active call stack depth: O(N) frames.
  - Intermediate list copies across all levels consume O(N^2) auxiliary heap
    memory before garbage collection.

DSA Optimization Note (Index Pointer Approach):
-----------------------------------------------
In production or coding interviews, avoid slicing lists during recursion.
Passing an integer `index` avoids list copying and achieves optimal O(N) time:
    def check_sorted_ptr(self, numbers: list, index: int = 0) -> bool:
        # Base case: reached or passed the last element
        if index >= len(numbers) - 1:
            return True
        # Mismatch check
        if numbers[index] > numbers[index + 1]:
            return False
        # Recursive step with pointer increment
        return self.check_sorted_ptr(numbers, index + 1)
- Time Complexity:  O(N) linear time (no list copies).
- Space Complexity: O(N) auxiliary call stack space (O(1) auxiliary heap).
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def check_sorted(self, numbers: list) -> bool:
        """Recursively verify if a list is sorted in non-decreasing order."""
        # Base Case: An empty list or single-element list is always sorted
        if len(numbers) <= 1:
            return True

        # Early Exit: If any adjacent pair violates order, array is not sorted
        if numbers[0] > numbers[1]:
            return False

        # Recursive Step: Check the rest of the list excluding the first element
        return self.check_sorted(numbers[1:])


# Instantiate the problem solver class
recursion_problems = RecursionProblems()

# Test array with out-of-order elements (9 > 7)
numbers = [1, 2, 6, 9, 7, 5]

# Output result of check_sorted (Expected: False)
print(recursion_problems.check_sorted(numbers))
