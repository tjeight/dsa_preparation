"""Problem: Rearrange Array Elements by Sign (LeetCode #2149).

Given an integer array `nums` of even length with an equal count of positive
and negative integers, rearrange the elements such that:
1. Every consecutive pair has opposite signs.
2. The rearranged array begins with a positive integer.
3. The relative order of integers of the same sign is preserved (stability).

Examples:
    Input:  nums = [2, 4, 5, -1, -3, -4]
    Output: [2, -1, 4, -3, 5, -4]
    Explanation:
        Positive elements in order: [2, 4, 5]
        Negative elements in order: [-1, -3, -4]
        Alternating merge: [2, -1, 4, -3, 5, -4]

    Input:  nums = [3, 1, -2, -5, 2, -4]
    Output: [3, -2, 1, -5, 2, -4]

    Input:  nums = [-1, 1]
    Output: [1, -1]

Algorithm Strategy (Two-List Partition and Alternating Merge):
--------------------------------------------------------------
1. Partitioning:
   - Traverse `nums` and segregate elements into two separate auxiliary lists:
     - `positive`: Collects all numbers > 0 in order of appearance.
     - `negative`: Collects all numbers < 0 in order of appearance.
2. Alternating Merge:
   - Loop through index `i` from `0` to `len(positive) - 1`:
     - Append `positive[i]` to `result` (even positions: 0, 2, 4, ...).
     - Append `negative[i]` to `result` (odd positions: 1, 3, 5, ...).
3. Return:
   - Returns the interleaved `result` list.

Step-by-Step Dry Run (nums = [2, 4, 5, -1, -3, -4]):
----------------------------------------------------
Phase 1: Segregation into positive and negative lists:
- num = 2  > 0 -> positive = [2]
- num = 4  > 0 -> positive = [2, 4]
- num = 5  > 0 -> positive = [2, 4, 5]
- num = -1 < 0 -> negative = [-1]
- num = -3 < 0 -> negative = [-1, -3]
- num = -4 < 0 -> negative = [-1, -3, -4]

Phase 2: Alternating Interleave (i in range(3)):
- i = 0: append positive[0] (2), negative[0] (-1) -> [2, -1]
- i = 1: append positive[1] (4), negative[1] (-3) -> [2, -1, 4, -3]
- i = 2: append positive[2] (5), negative[2] (-4) -> [2, -1, 4, -3, 5, -4]

Final Return: [2, -1, 4, -3, 5, -4]

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - Phase 1: O(N) pass to filter elements into positive and negative lists.
  - Phase 2: O(N/2) loop interleaving elements into the result list.
  - Total Time: O(N + N/2) = O(N).
- Auxiliary Space: O(N)
  - Auxiliary lists `positive` and `negative` each take N / 2 elements -> O(N).
  - Output list `result` takes O(N) elements.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Two-Pass Segregation (Current Implementation):
   - Segregate into positive and negative lists, then interleave.
   - Time: O(N), Auxiliary Space: O(N).
   - Advantage: Highly intuitive and easily extensible to Variety 2 (unequal
     positive/negative counts).
2. Optimal Single-Pass Direct Placement:
   - Pre-allocate output array of size N: `ans = [0] * N`.
   - Maintain `pos_idx = 0` and `neg_idx = 1`.
   - In a single pass: if num > 0: ans[pos_idx] = num, pos_idx += 2;
     else: ans[neg_idx] = num, neg_idx += 2.
   - Time: O(N), Auxiliary Space: O(N) (avoids intermediate buffers).
"""


class Solution:
    """Solution class providing array rearrangement algorithms."""

    def sort_positive_and_negative(self, nums):
        """Rearrange array elements in alternating positive and negative order.

        Args:
            nums: List of integers with equal numbers of positive and negative values.

        Returns:
            A new list with elements alternating starting with a positive number.
        """
        positive = []
        negative = []

        # Segregate positive and negative integers preserving order
        for num in nums:
            if num > 0:
                positive.append(num)
            else:
                negative.append(num)

        # Merge both lists alternately starting with positive
        result = []
        for i in range(len(positive)):
            result.append(positive[i])
            result.append(negative[i])

        return result


# Instantiate the solution class
solution = Solution()

# Example input array with equal positive and negative counts
nums = [2, 4, 5, -1, -3, -4]

# Execute and print rearranged array (Expected output: [2, -1, 4, -3, 5, -4])
print(solution.sort_positive_and_negative(nums=nums))
