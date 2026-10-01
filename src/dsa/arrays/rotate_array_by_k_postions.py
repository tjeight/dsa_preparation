"""Problem: Left Rotate an Array by K Positions.

Given an array of integers `nums` and a non-negative integer `k`, rotate the array
to the left by `k` positions. Elements shifted beyond the left boundary wrap
around to the end of the array.

Examples:
    Input:  nums = [1, 2, 3, 4, 5], k = 2
    Output: [3, 4, 5, 1, 2]

    Input:  nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    Output: [4, 5, 6, 7, 1, 2, 3]

    Input:  nums = [1, 2], k = 5
    Output: [2, 1]  (Since k = 5 % 2 = 1)

Algorithm Strategy (Temporary Buffer / Slicing Approach):
----------------------------------------------------------
1. Modulo Reduction:
   - If `k >= len(nums)`, rotating `len(nums)` times yields the identical array.
   - Effective rotation: `k = k % len(nums)`.
2. Temporary Buffer:
   - Extract the first `k` elements that will wrap to the back:
     `sliced_array = nums[:k]`.
3. Shift Remaining Elements:
   - Shift the remaining `N - k` elements leftward by `k` steps:
     `nums[i] = nums[i + k]` for `i` from `0` to `N - k - 1`.
4. Copy Buffer to Tail:
   - Place the buffered `k` elements into the last `k` positions:
     `nums[len(nums) - k + i] = sliced_array[i]` for `i` in `range(k)`.
5. Return the mutated list.

Step-by-Step Dry Run (nums = [1, 2, 3, 4, 5], k = 2):
------------------------------------------------------
N = 5, k = 2 % 5 = 2.
1. sliced_array = nums[:2] = [1, 2]
2. Shifting loop: i in range(5 - 2 = 3) -> [0, 1, 2]
   - i = 0: nums[0] = nums[0 + 2] (3) -> [3, 2, 3, 4, 5]
   - i = 1: nums[1] = nums[1 + 2] (4) -> [3, 4, 3, 4, 5]
   - i = 2: nums[2] = nums[2 + 2] (5) -> [3, 4, 5, 4, 5]
3. Copy-back loop: i in range(2) -> [0, 1]
   - i = 0: nums[5 - 2 + 0] = nums[3] = sliced_array[0] (1) -> [3, 4, 5, 1, 5]
   - i = 1: nums[5 - 2 + 1] = nums[4] = sliced_array[1] (2) -> [3, 4, 5, 1, 2]
Final Return: [3, 4, 5, 1, 2]

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - Slicing first k elements: O(k)
  - Shifting (N - k) elements: O(N - k)
  - Copying k elements back: O(k)
  - Total Time: O(k + (N - k) + k) = O(N + k) = O(N) since k < N.
- Auxiliary Space: O(k)
  - Requires a temporary list `sliced_array` storing k elements.
  - In worst case (k close to N), requires O(N) auxiliary space.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Iterative Rotation):
   - Left rotate by 1 position repeated k times.
   - Time: O(k * N), Space: O(1). Inefficient for large k.
2. Better Approach (Temporary Buffer - Current Implementation):
   - Save k elements, shift remaining (N - k), restore k elements.
   - Time: O(N), Space: O(k). Simple and fast.
3. Optimal Approach (Reversal Algorithm):
   - Reverse first k elements: nums[0:k].
   - Reverse remaining elements: nums[k:N].
   - Reverse the entire array: nums[0:N].
   - Time: O(N), Space: O(1) in-place without auxiliary buffer.
"""


class Solution:
    """Solution class providing array manipulation algorithms."""

    def rotateArray(self, nums, k):
        """Rotate the array to the left by k positions.

        Args:
            nums: List of integers to rotate.
            k: Number of positions to rotate left.

        Returns:
            The rotated list (mutated in-place).
        """
        # First find the actual rotation needed
        k = k % len(nums)

        # Slice the array into two parts
        sliced_array = nums[:k]

        # Shift remaining (len(nums) - k) elements to the beginning
        for i in range(len(nums) - k):
            nums[i] = nums[i + k]

        # Copy the buffered first k elements to the end of the array
        for i in range(k):
            nums[len(nums) - k + i] = sliced_array[i]

        return nums


# Example input array and rotation count
nums = [1, 2, 3, 4, 5]
k = 2

# Instantiate the solution class
solution = Solution()

# Execute and print rotated array (Expected output: [3, 4, 5, 1, 2])
print(solution.rotateArray(nums=nums, k=k))
