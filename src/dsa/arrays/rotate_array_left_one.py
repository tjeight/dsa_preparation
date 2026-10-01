"""Problem: Left Rotate an Array by One Place.

Given an array of integers `nums`, rotate the array to the left by one position
in-place. The first element moves to the last position, and all other elements
shift one position to the left.


Examples:
    Input:  nums = [1, 2, 3, 4, 5]
    Output: [2, 3, 4, 5, 1]

    Input:  nums = [3]
    Output: [3]

    Input:  nums = [-1, -2, -3]
    Output: [-2, -3, -1]

Algorithm Strategy (In-Place Shift with Temporary Buffer):
----------------------------------------------------------
1. Save the first element:
   - Store `nums[0]` in a scalar variable `temp`.
2. Shift remaining elements leftward:
   - Iterate through indices `i` from `0` to `len(nums) - 2`.
   - Copy the adjacent right neighbor to current position: `nums[i] = nums[i + 1]`.
3. Wrap around:
   - Place the saved first element `temp` at the final index: `nums[-1] = temp`.
4. Return the mutated list.

Step-by-Step Dry Run (nums = [1, 2, 3, 4, 5]):
----------------------------------------------
Length N = 5. Loop runs for i in range(4): [0, 1, 2, 3].
- Initial: temp = nums[0] = 1
- i = 0: nums[0] = nums[1] (2) -> array becomes [2, 2, 3, 4, 5]
- i = 1: nums[1] = nums[2] (3) -> array becomes [2, 3, 3, 4, 5]
- i = 2: nums[2] = nums[3] (4) -> array becomes [2, 3, 4, 4, 5]
- i = 3: nums[3] = nums[4] (5) -> array becomes [2, 3, 4, 5, 5]
Loop ends.
- Wrap around: nums[-1] = temp (1) -> array becomes [2, 3, 4, 5, 1]
Final Return: [2, 3, 4, 5, 1]

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - The loop performs exactly N - 1 shifting assignments.
  - Initial buffering and final assignment are O(1).
  - Total time: O(N).
- Auxiliary Space: O(1)
  - In-place mutation; requires only one scalar variable `temp`.
"""


class Solution:
    """Solution class providing array manipulation algorithms."""

    def rotateArrayByOne(self, nums):
        """Rotate the array to the left by one position in-place.

        Args:
            nums: List of integers to rotate.

        Returns:
            The rotated list (mutated in-place).
        """
        # Store the first element to prevent overwriting during left-shifts
        temp = nums[0]

        # Shift all elements from index 1 to N-1 one index to the left
        for i in range(len(nums) - 1):
            nums[i]= nums[i + 1]

        # Place the preserved first element at the end of the array
        nums[-1] = temp

        return nums


# Instantiate the solution class
solution = Solution()

# Example input array
nums = [1, 2, 3, 4, 5]

# Execute and print rotated array (Expected output: [2, 3, 4, 5, 1])
print(solution.rotateArrayByOne(nums=nums))
