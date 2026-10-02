"""Problem: Find Missing Number (LeetCode #268).

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,
return the only number in the range that is missing from the array.

Examples:
    Input:  nums = [0, 1, 5, 2, 3]
    Output: 4
    Explanation: n = 5 since there are 5 numbers. The range is [0, 5].
                 All numbers are present except 4.

    Input:  nums = [3, 0, 1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers. The range is [0, 3].
                 All numbers are present except 2.

    Input:  nums = [0, 1]
    Output: 2

    Input:  nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    Output: 8

Algorithm Strategy (Mathematical Sum / Gauss's Formula):
--------------------------------------------------------
1. Determine Expected Range:
   - An array with `n` elements drawn from `[0, n]` contains every number
     except exactly one missing value.
2. Calculate Expected Sum (Gauss's Summation):
   - The sum of integers from 0 to n is:
     total = n * (n + 1) // 2
3. Calculate Actual Sum:
   - Sum all elements currently present in `nums`.
4. Difference:
   - The missing number is strictly the difference:
     missing = total - sum_of

Step-by-Step Dry Run (nums = [0, 1, 5, 2, 3]):
-----------------------------------------------
1. Array length n = len(nums) = 5.
2. Expected sum:
   total = (5 * (5 + 1)) // 2 = (5 * 6) // 2 = 30 // 2 = 15.
3. Actual sum:
   sum_of = sum([0, 1, 5, 2, 3]) = 0 + 1 + 5 + 2 + 3 = 11.
4. Missing number calculation:
   total - sum_of = 15 - 11 = 4.
Final Return: 4

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - `len(nums)` takes O(1) time.
  - Mathematical formula `n * (n + 1) // 2` executes in O(1) time.
  - `sum(nums)` iterates through all N elements once in O(N) time.
  - Total Time: O(N).
- Auxiliary Space: O(1)
  - Operates purely with scalar arithmetic variables (`n`, `total`, `sum_of`).
  - No auxiliary data structures or memory allocations.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Linear Search):
   - For every i from 0 to n, linearly search nums for i.
   - Time: O(N^2), Space: O(1).
2. Better Approach (Hash Set / Frequency Array):
   - Store elements in a hash set or boolean array of size n + 1.
   - Time: O(N), Space: O(N).
3. Optimal Approach 1 (Sum Formula - Current Implementation):
   - Uses Gauss's formula total - sum(nums).
   - Time: O(N), Space: O(1).
   - Note: In Python, integers have arbitrary precision (no 32-bit overflow).
4. Optimal Approach 2 (Bitwise XOR):
   - XOR all indices 0..n and XOR all elements in nums.
   - Identical numbers cancel out (x ^ x = 0), leaving only the missing number.
   - Time: O(N), Space: O(1). Avoids numeric overflow in C++/Java.
"""


class Solution:
    """Solution class providing array inspection and number finding algorithms."""

    def find_missing_number(self, nums: list):
        """Find the missing number in the range [0, n] using summation.

        Args:
            nums: List of distinct integers in the range [0, n].

        Returns:
            The missing integer from the range [0, n].
        """
        # Number of elements present in the array (range is 0 to n)
        n = len(nums)

        # Expected sum of all numbers from 0 to n using Gauss's formula
        total = (n * (n + 1)) // 2

        # Actual sum of the elements present in the array
        sum_of = sum(nums)

        # The difference yields the missing number
        return total - sum_of


# Instantiate the solution class
solution = Solution()

# Example input array where n = 5 and missing number is 4
nums = [0, 1, 5, 2, 3]

# Execute and print the missing number (Expected output: 4)
print(solution.find_missing_number(nums=nums))
