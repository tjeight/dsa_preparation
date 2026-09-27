"""Problem: In-Place Array Reversal Using Recursive Two-Pointer Technique.

Given an array (list) of elements, reverse its order in-place using recursion.
Instead of creating new list slices (which would allocate auxiliary memory),
this algorithm swaps symmetric elements from the boundaries inward using two
pointers (`left` and `right`) until they meet or cross.

Examples:
    [1, 2, 3, 6, 4] -> [4, 6, 3, 2, 1]
    [10, 20, 30]    -> [30, 20, 10]
    [5]             -> [5]
    []              -> []

Recursive Two-Pointer Strategy (Converging Boundary Pointers):
--------------------------------------------------------------
1. Pointers Initialization:
   - `left`: Points to the beginning index (0).
   - `right`: Points to the ending index (len(numbers) - 1).

2. Base Case:
   `if left >= right: return numbers`
   - When `left == right`, the pointers meet at the middle element of an
     odd-length list (the middle element is already in its correct position).
   - When `left > right`, the pointers cross in an even-length or empty list,
     meaning all boundary pairs have already been swapped.
   - Halts recursion and begins unwinding the call stack.

3. Current Step / Work (In-Place Swap):
   `numbers[left], numbers[right] = numbers[right], numbers[left]`
   - Python's tuple unpacking swaps the elements at indices `left` and `right`
     in O(1) time without requiring a temporary variable or extra memory.

4. Recursive Step:
   `return self.reverse_array(numbers, left=left + 1, right=right - 1)`
   - Moves `left` inward (rightward) by +1.
   - Moves `right` inward (leftward) by -1.
   - Recurses on the smaller subarray window between `left + 1` and `right - 1`.

Call Stack Lifecycle Trace (for numbers = [1, 2, 3, 6, 4], left = 0, right = 4):
--------------------------------------------------------------------------------
Call 1: reverse_array([1, 2, 3, 6, 4], left=0, right=4)
- 0 < 4 -> Swap numbers[0] and numbers[4] (1 <-> 4)
- Array state: [4, 2, 3, 6, 1]
- Recurses with left=1, right=3

Call 2: reverse_array([4, 2, 3, 6, 1], left=1, right=3)
- 1 < 3 -> Swap numbers[1] and numbers[3] (2 <-> 6)
- Array state: [4, 6, 3, 2, 1]
- Recurses with left=2, right=2

Call 3: reverse_array([4, 6, 3, 2, 1], left=2, right=2)
- left >= right (2 >= 2) -> BASE CASE REACHED!
- Returns numbers directly: [4, 6, 3, 2, 1]

Unwinding Phase:
- Call 2 receives [4, 6, 3, 2, 1] and returns it.
- Call 1 receives [4, 6, 3, 2, 1] and returns it to top-level caller.
Final Output: [4, 6, 3, 2, 1]

Complexity Analysis:
--------------------
- Time Complexity:  O(N)
  - At each step, 1 swap is performed and the search window narrows by 2.
  - Total recursive calls: floor(N / 2) + 1 = O(N).
  - Total operations: O(N) linear time.
- Space Complexity: O(N) Auxiliary Stack Space
  - Call stack depth reaches N / 2 frames.
  - Auxiliary Memory (Heap): O(1) since mutations occur in-place on the same
    list reference without creating copies or slices.

DSA Optimization & Single-Pointer Note:
---------------------------------------
1. Single-Pointer Recursive Alternative:
   Instead of two pointers (`left` and `right`), we can derive `right` using
   a single pointer `i` from 0 to N // 2:
       def reverse_single_ptr(self, arr: list, i: int = 0) -> list:
           n = len(arr)
           if i >= n // 2:
               return arr
           arr[i], arr[n - 1 - i] = arr[n - 1 - i], arr[i]
           return self.reverse_single_ptr(arr, i + 1)
2. Iterative Two-Pointer (Optimal Production Pattern):
   Iterative `while left < right:` achieves O(N) time with O(1) space,
   avoiding call stack frames and preventing RecursionError on large arrays.
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def reverse_array(self, numbers: list, left: int, right: int) -> list:
        """Recursively reverse a list in-place using two converging pointers."""
        # Base Case: Stop when pointers meet (odd length) or cross (even length)
        if left >= right:
            return numbers

        # In-Place Swap: Swap elements at current left and right boundaries
        numbers[left], numbers[right] = numbers[right], numbers[left]

        # Recursive Step: Recurse on inner subarray with narrowed boundary pointers
        return self.reverse_array(numbers, left=left + 1, right=right - 1)


# Instantiate the problem solver class
recursion_problems = RecursionProblems()


# Input list to reverse
numbers = [1, 2, 3, 6, 4]

# Execute two-pointer recursive reversal from 0 to len(numbers) - 1
print(recursion_problems.reverse_array(numbers=numbers, left=0, right=len(numbers) - 1))
