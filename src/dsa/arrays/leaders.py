"""Problem: Leaders in an Array.

Given an integer array `nums`, find all the leaders in the array.
An element is a Leader if it is strictly greater than all the elements
to its right side. The rightmost element is always a leader.
The resulting leaders should be returned in their original relative
order from left to right.

Examples:
    Input:  nums = [1, 2, 5, 3, 1, 2]
    Output: [5, 3, 2]
    Explanation:
        - 5 is greater than [3, 1, 2] -> Leader.
        - 3 is greater than [1, 2]    -> Leader.
        - 2 is the rightmost element  -> Leader.

    Input:  nums = [16, 17, 4, 3, 5, 2]
    Output: [17, 5, 2]

    Input:  nums = [1, 2, 3, 4, 5]
    Output: [5]

    Input:  nums = [5, 4, 3, 2, 1]
    Output: [5, 4, 3, 2, 1]

Algorithm Strategy (Right-to-Left Linear Scan):
------------------------------------------------
1. Key Insight:
   - Scanning from left to right requires checking all elements to the right,
     leading to O(N^2) brute force.
   - Scanning backwards (right to left) allows maintaining a running maximum
     of all elements seen so far (`max_right`).
2. Initialization:
   - The rightmost element `nums[-1]` is always a leader since no elements
     exist to its right.
   - Initialize `leaders = [nums[-1]]` and `max_right = nums[-1]`.
3. Backward Traversal:
   - Iterate backwards from index `len(nums) - 2` down to index `0`.
   - If `nums[i] > max_right`:
     - `nums[i]` is strictly greater than every element to its right.
     - Append `nums[i]` to `leaders`.
     - Update `max_right = nums[i]`.
4. Restore Original Order:
   - Since elements were collected from right to left, reverse `leaders`
     before returning: `list(reversed(leaders))`.

Step-by-Step Dry Run (nums = [1, 2, 5, 3, 1, 2]):
--------------------------------------------------
N = 6. Initial: leaders = [2], max_right = 2.
- i = 4 (nums[4] = 1): 1 > 2 False -> Skip. max_right = 2.
- i = 3 (nums[3] = 3): 3 > 2 True  -> leaders = [2, 3], max_right = 3.
- i = 2 (nums[2] = 5): 5 > 3 True  -> leaders = [2, 3, 5], max_right = 5.
- i = 1 (nums[1] = 2): 2 > 5 False -> Skip. max_right = 5.
- i = 0 (nums[0] = 1): 1 > 5 False -> Skip. max_right = 5.
Loop ends.
Reversal: reversed([2, 3, 5]) -> [5, 3, 2].
Final Return: [5, 3, 2]

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - Single backward pass from N - 2 to 0: O(N) comparisons and updates.
  - Reversing the leaders list of size K (where K <= N): O(K).
  - Total Time: O(N).
- Auxiliary Space: O(1) (excluding output list)
  - Uses only scalar variable `max_right` and iteration index `i`.
  - Output space for `leaders`: O(N) in worst case (strictly decreasing array).

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Nested Loop):
   - For each element, linearly scan all elements to its right.
   - Time: O(N^2), Auxiliary Space: O(1).
2. Optimal Approach (Backward Scan - Current Implementation):
   - Track running maximum from right to left in a single pass.
   - Time: O(N), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing array inspection and leader algorithms."""

    def find_leaders(self, nums):
        """Find all leader elements in the array from left to right.

        Args:
            nums: List of integers to inspect.

        Returns:
            A list containing all leader elements in their original order.
        """
        leaders = []

        # The rightmost element is always a leader
        leaders.append(nums[-1])
        # Track the maximum element encountered from the right
        max_right = nums[-1]

        # Traverse backwards from the second-to-last element to index 0
        for i in range(len(nums) - 2, -1, -1):
            # If current element is strictly greater than maximum to its right
            if nums[i] > max_right:
                leaders.append(nums[i])
                max_right = nums[i]

        # Reverse the list to restore original left-to-right order
        return list(reversed(leaders))


# Instantiate the solution class
solution = Solution()

# Example input array
nums = [1, 2, 5, 3, 1, 2]

# Execute and print the leaders in the array (Expected output: [5, 3, 2])
print(solution.find_leaders(nums=nums))
