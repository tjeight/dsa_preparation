"""Problem: Find the Largest Element in an Array.

Given an array of integers, find and return the maximum (largest) element.

Examples:
    [5, 83, 93, 0, 56]   -> 93
    [1, 2, 3, 4, 5]      -> 5
    [-10, -3, -50, -2]   -> -2 (handles negative numbers)
    [42]                 -> 42 (single element)

Algorithm Strategy (Single-Pass Linear Scan):
---------------------------------------------
1. Initialization:
   - Initialize `max_number = numbers[0]`.
   - Initializing to the first element (rather than 0 or a fixed constant)
     guarantees correct results even if all elements in the array are negative.

2. Linear Traversal:
   - Iterate from index 1 to len(numbers) - 1.
   - Compare each element `numbers[i]` with the running `max_number`.
   - If `numbers[i] > max_number`, update `max_number = numbers[i]`.

3. Invariant:
   - At the end of iteration `i`, `max_number` holds the maximum value of the
     subarray `numbers[0...i]`.
   - After completing the full pass, `max_number` is the global maximum.

Step-by-Step Dry Run (numbers = [5, 83, 93, 0, 56], n = 5):
------------------------------------------------------------
Initial: max_number = numbers[0] = 5
i = 1: numbers[1] = 83 -> 83 > 5  (True)  -> max_number = 83
i = 2: numbers[2] = 93 -> 93 > 83 (True)  -> max_number = 93
i = 3: numbers[3] = 0  -> 0 > 93  (False) -> max_number = 93
i = 4: numbers[4] = 56 -> 56 > 93 (False) -> max_number = 93
Final Result: 93

Complexity Analysis:
--------------------
- Time Complexity:
  - Best Case:    O(N) (Must inspect every element at least once)
  - Average Case: O(N)
  - Worst Case:   O(N)
  - Theoretical Lower Bound: Finding the maximum of N unsorted elements
    requires at least N - 1 comparisons (adversary argument / tournament bound).
- Auxiliary Space: O(1) (In-place; requires a single accumulator variable)

Alternative Approaches & Python Equivalents:
--------------------------------------------
- Brute Force via Sorting: Sort the array in O(N log N) and take the last
  element. Slower and unnecessarily mutates the array or allocates memory.
- Python Built-in: `max(numbers)` is implemented internally in C and executes
  the same O(N) single-pass linear scan with lower interpreter overhead.
"""


class Solution:
    """Solution class providing array inspection algorithms."""

    def find_largest_element(self, numbers: list[int]) -> int:
        """Find the maximum element in a list of integers via linear scan."""
        # Initialize running maximum with the first element
        max_number = numbers[0]

        # Scan remaining elements from index 1 to the end
        for i in range(1, len(numbers)):
            # Update running maximum if a larger element is found
            if numbers[i] > max_number:
                max_number = numbers[i]

        return max_number


# Instantiate the solution class
solution = Solution()

# Example input array
numbers = [5, 83, 93, 0, 56]

# Execute linear scan and print the largest element (Expected output: 93)
print(solution.find_largest_element(numbers=numbers))
