"""Problem: Sum of Array Elements Using Recursion.

Given an array (list) of integers, calculate the sum of all elements using
recursive decomposition.

Example:
    Input:  numbers = [1, 2, 3]
    Output: 6
    Explanation: 1 + 2 + 3 = 6

Recursion Strategy (Head Recursion via Slicing):
------------------------------------------------
1. Base Case:
   `if len(numbers) == 0: return 0`
   An empty array has a sum of 0 (additive identity).

2. Recursive Step:
   `numbers[0] + self.sum_of_array_elements(numbers[1:])`
   Decomposes the problem into:
   (First element) + (Sum of the remainder of the array).
   The actual additions occur during the call stack UNWINDING phase.

Call Stack Lifecycle Trace (for numbers = [1, 2, 3]):
-----------------------------------------------------
Descent Phase (Pushing stack frames):
| sum_of_array_elements([])     | -> Base Case reached (returns 0)
| sum_of_array_elements([3])    | -> Waits for sum([]) to evaluate 3 + sum([])
| sum_of_array_elements([2, 3]) | -> Waits for sum([3]) to evaluate 2 + sum([3])
| sum_of_array_elements([1..3]) | -> Waits for sum([2, 3]) to evaluate 1 + sum(...)
+-------------------------------+
Unwinding Phase (Evaluating additions):
- sum([]) returns 0
- sum([3]) returns 3 + 0 = 3
- sum([2, 3]) returns 2 + 3 = 5
- sum([1, 2, 3]) returns 1 + 5 = 6 -> Final result printed

Complexity Analysis (Current Slicing Approach):
-----------------------------------------------
- Time Complexity:  O(N^2)
  - There are N + 1 recursive calls.
  - Slicing `numbers[1:]` creates a shallow copy of length (k - 1) in O(k) time.
  - Total work: N + (N - 1) + (N - 2) + ... + 1 = O(N^2).
- Space Complexity: O(N^2) total memory allocated for list slices across all
  calls (O(N) active call stack depth).

DSA Optimization Note (Index-Based Pointer Approach):
-----------------------------------------------------
To achieve optimal O(N) time and O(N) auxiliary space, avoid list slicing by
passing an index pointer instead:
    def sum_array_optimal(self, numbers: list, idx: int = 0) -> int:
        if idx == len(numbers):
            return 0
        return numbers[idx] + self.sum_array_optimal(numbers, idx + 1)
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def sum_of_array_elements(self, numbers: list) -> int:
        """Calculate the sum of array elements using list-slicing recursion."""
        # Base Case: Sum of an empty list is 0
        if len(numbers) == 0:
            return 0

        # Recursive Step: First element + sum of the remaining sub-array
        return numbers[0] + self.sum_of_array_elements(numbers[1:])


# Example input array
numbers = [1, 2, 3]

# Instantiate the problem solver class
recursion_problems = RecursionProblems()

# Compute and output the recursive sum
print(recursion_problems.sum_of_array_elements(numbers))
