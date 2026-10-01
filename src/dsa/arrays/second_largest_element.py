"""Problem: Find the Second Largest Element in an Array.

Given an array of integers, find and return the second largest distinct element.
If no distinct second largest element exists (e.g. all elements are identical
or array length < 2), handle appropriately.

Examples:
    [1, 2, 3, 58, 5]          -> 5  (Largest is 58, second largest is 5)
    [12, 35, 1, 10, 34, 1]     -> 34 (Largest is 35, second largest is 34)
    [10, 10, 10]              -> -inf (No distinct second largest)
    [5]                       -> -inf (Single element array)

Algorithm Strategy (Single-Pass Simultaneous Tracking):
-------------------------------------------------------
1. Trackers:
   - `first_largest`: Tracks the highest value found so far.
   - `second_largest`: Tracks the second highest distinct value found so far.

2. Traversal & Invariant Updates:
   - For each element `num`:
     - Case 1 (`num > first_largest`):
       A new global maximum is found. Demote `first_largest` to
       `second_largest`, then update `first_largest = num`.
     - Case 2 (`num > second_largest and num != first_largest`):
       `num` is strictly between `second_largest` and `first_largest`.
       Update `second_largest = num`.
     - Case 3 (`num <= second_largest` or `num == first_largest`):
       Duplicate or too small; ignore.

Step-by-Step Dry Run (nums = [1, 2, 3, 58, 5]):
------------------------------------------------
Initial: first_largest = -inf, second_largest = +inf
- num = 1:
  1 > -inf -> second_largest = -inf, first_largest = 1
- num = 2:
  2 > 1    -> second_largest = 1,    first_largest = 2
- num = 3:
  3 > 2    -> second_largest = 2,    first_largest = 3
- num = 58:
  58 > 3   -> second_largest = 3,    first_largest = 58
- num = 5:
  5 < 58 (not largest)
  5 > 3 and 5 != 58 -> second_largest = 5
Final Return: 5

Complexity Analysis:
--------------------
- Time Complexity:
  - Best, Average, Worst Case: O(N) (Single linear pass across N elements)
  - At most 2 comparisons per element.
- Auxiliary Space: O(1) (Maintains only two scalar tracker variables)

Comparison of Approaches (Striver's DSA Progression):
-----------------------------------------------------
1. Brute Force (Sorting):
   Sort the array in O(N log N) time, then scan backward to find the first
   element strictly smaller than the maximum. Modifies or duplicates the array.
2. Better Approach (Two-Pass Linear Scan):
   Pass 1: Find the largest element in O(N).
   Pass 2: Find the maximum element strictly less than largest in O(N).
   Total: 2 passes, O(N) time.
3. Optimal Approach (Single-Pass - Current Implementation):
   Maintains both maximums concurrently in a single traversal.
   Total: 1 pass, at most 2N comparisons, O(N) time, O(1) space.
"""


class Solution:
    """Solution class providing array inspection algorithms."""

    def find_second_largest_element(self, nums):
        """Find the second largest distinct element using a single-pass scan."""
        # Initialize trackers
        first_largest = float("-inf")
        second_largest = float("inf")

        for num in nums:
            # Case 1: Found a new global maximum
            if num > first_largest:
                second_largest = first_largest
                first_largest = num
            # Case 2: Found an element between first and second largest
            elif num > second_largest and num != first_largest:
                second_largest = num

        return second_largest


# Example input list
nums = [1, 2, 3, 58, 5]

# Instantiate the solution class
solution = Solution()

# Execute and print the second largest element (Expected output: 5)
print(solution.find_second_largest_element(nums=nums))
