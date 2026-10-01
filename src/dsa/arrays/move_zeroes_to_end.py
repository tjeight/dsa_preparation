"""Problem: Move Zeroes to End (LeetCode #283).

Given an integer array `nums`, move all 0's to the end of the array while
maintaining the relative order of the non-zero elements. This operation
must be performed in-place without making a copy of the array.

Examples:
    Input:  nums = [0, 1, 4, 0, 5, 2]
    Output: [1, 4, 5, 2, 0, 0]

    Input:  nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

    Input:  nums = [0]
    Output: [0]

    Input:  nums = [1, 2, 3]
    Output: [1, 2, 3]

Algorithm Strategy (Two-Pointer In-Place Partitioning):
-------------------------------------------------------
1. Pointer Invariants:
   - `index` (slow pointer): Points to the target position where the next
     non-zero element should be placed (also marks the boundary of non-zeroes).
   - `i` (fast pointer / scanner): Iterates through every element from left
     to right across the array.
2. Traversal:
   - When `nums[i] != 0`:
     - Swap `nums[index]` and `nums[i]`.
     - If `index == i` (no zeroes encountered yet), swapping is a self-swap.
     - If `index < i` (zeroes encountered previously), this moves the non-zero
       element forward and pushes the zero backward.
     - Advance `index += 1`.
   - When `nums[i] == 0`:
     - Do nothing; `i` increments while `index` remains stationary at the zero.
3. Stability:
   - Non-zero elements are encountered in their original relative sequence and
     swapped sequentially to `index = 0, 1, 2, ...`, preserving relative order.

Step-by-Step Dry Run (nums = [0, 1, 4, 0, 5, 2]):
--------------------------------------------------
N = 6. Initial: index = 0.
- i = 0: nums[0] == 0 -> Skip. index remains 0. Array: [0, 1, 4, 0, 5, 2]
- i = 1: nums[1] = 1 != 0 -> Swap nums[0], nums[1] (0 <-> 1).
         Array: [1, 0, 4, 0, 5, 2]. index becomes 1.
- i = 2: nums[2] = 4 != 0 -> Swap nums[1], nums[2] (0 <-> 4).
         Array: [1, 4, 0, 0, 5, 2]. index becomes 2.
- i = 3: nums[3] == 0 -> Skip. index remains 2. Array: [1, 4, 0, 0, 5, 2]
- i = 4: nums[4] = 5 != 0 -> Swap nums[2], nums[4] (0 <-> 5).
         Array: [1, 4, 5, 0, 0, 2]. index becomes 3.
- i = 5: nums[5] = 2 != 0 -> Swap nums[3], nums[5] (0 <-> 2).
         Array: [1, 4, 5, 2, 0, 0]. index becomes 4.
Loop ends.
Final Return: [1, 4, 5, 2, 0, 0]

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - Single linear pass through N elements.
  - At most N swaps and comparisons, each taking O(1) time.
- Auxiliary Space: O(1)
  - In-place two-pointer permutation; uses only two scalar indices (`index`, `i`).

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Temporary Array):
   - Extract all non-zero elements into a temp list of size K: O(N) time.
   - Copy non-zeros back to nums[0..K-1] and fill nums[K..N-1] with 0s.
   - Time: O(N), Auxiliary Space: O(N).
2. Optimal (Two-Pointer In-Place Swap - Current Implementation):
   - Swaps non-zero elements into `index` while bubbling zeroes rightward.
   - Time: O(N), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing array manipulation algorithms."""

    def moveZeroesToEnd(self, nums):
        """Move all zeroes to the end of the array while preserving order.

        Args:
            nums: List of integers to partition in-place.

        Returns:
            The partitioned list with zeroes moved to the end.
        """
        # Pointer to the next position for a non-zero element
        index = 0

        # Fast pointer scanning through each element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap non-zero element into the target index position
                nums[index], nums[i] = nums[i], nums[index]
                index += 1

        return nums


# Instantiate the solution class
solution = Solution()

# Example input array
nums = [0, 1, 4, 0, 5, 2]

# Execute and print partitioned array (Expected output: [1, 4, 5, 2, 0, 0])
print(solution.moveZeroesToEnd(nums=nums))
