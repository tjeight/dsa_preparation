"""Problem: Max Consecutive Ones (LeetCode #485).

Given a binary array `nums`, return the maximum number of consecutive 1s
in the array.

A binary array contains only 0s and 1s.

Examples:
    Input: nums = [1, 1, 0, 1, 1, 1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.

    Input: nums = [1, 0, 1, 1, 0, 1]
    Output: 2

    Input: nums = [0, 0, 0]
    Output: 0

    Input: nums = [1, 1, 1, 1]
    Output: 4

Algorithm Strategy (Single-Pass Linear Counter):
-------------------------------------------------
1. Maintain two scalar variables:
   - `count`: Tracks the current streak of consecutive 1s.
   - `max_ones`: Tracks the global maximum streak found so far.
2. Iterate through each element `num` in `nums`:
   - If `num == 0`:
     - Streak ended. Compare and update `max_ones = max(max_ones, count)`.
     - Reset `count = 0`.
   - Else (`num == 1`):
     - Streak continues. Increment `count += 1`.
3. Post-Loop Boundary Check:
   - If the array ends with 1s (e.g., [..., 1, 1, 1]), the loop terminates
     without encountering a 0. An explicit final check updates `max_ones`
     with any remaining active streak.

Step-by-Step Dry Run (nums = [1, 1, 0, 0, 1, 1, 1, 1]):
--------------------------------------------------------
Initial: max_ones = 0, count = 0
- Index 0 (num = 1): count = 1
- Index 1 (num = 1): count = 2
- Index 2 (num = 0): count > max_ones (2 > 0) -> max_ones = 2, count = 0
- Index 3 (num = 0): count > max_ones (0 > 2 False), count = 0
- Index 4 (num = 1): count = 1
- Index 5 (num = 1): count = 2
- Index 6 (num = 1): count = 3
- Index 7 (num = 1): count = 4
Loop ends.
Post-loop check: count > max_ones (4 > 2 True) -> max_ones = 4
Final Return: 4

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - We traverse the array of N elements exactly once.
  - Each element involves O(1) comparison and arithmetic operations.
- Auxiliary Space: O(1)
  - Uses only two scalar integer variables (`max_ones`, `count`).
  - No auxiliary data structures or array copies are allocated.
"""


class Solution:
    """Solution class providing array inspection algorithms."""

    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        """Find the maximum number of consecutive 1s in a binary array.

        Args:
            nums: List of binary integers (0s and 1s).

        Returns:
            The maximum count of consecutive 1s found in the array.
        """
        # Global maximum streak of consecutive 1s found so far
        max_ones = 0
        # Current active streak counter of consecutive 1s
        count = 0

        # Traverse each element in the binary array
        for num in nums:
            if num == 0:
                # 0 encountered: active streak is broken
                # Update global maximum if current streak exceeds it
                if count > max_ones:
                    max_ones = count
                # Reset active streak counter for subsequent 1s
                count = 0
            else:
                # 1 encountered: extend current active streak
                count += 1

        # Post-loop boundary check:
        # Handles cases where the array ends with a streak of 1s
        if count > max_ones:
            max_ones = count

        return max_ones


# Example binary array input
nums = [1, 1, 0, 0, 1, 1, 1, 1]

# Instantiate the solution class
solution = Solution()

# Execute and print the maximum consecutive 1s (Expected output: 4)
print(solution.findMaxConsecutiveOnes(nums=nums))
