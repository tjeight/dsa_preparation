"""Problem: Linear Search Algorithm.

Linear Search (also known as Sequential Search) is the simplest searching
algorithm. It traverses an array or collection sequentially from the beginning,
inspecting each element one by one until either the target element is found or
the entire list has been exhausted.

Examples:
    nums = [10, 2.5, 63, 95, 5], target = 5  -> 4
    nums = [1, 2, 3, 4, 5],      target = 10 -> -1 (not found)
    nums = [7, 7, 7],            target = 7  -> 0 (first occurrence)
    nums = [],                   target = 1  -> -1 (empty array)

Algorithm Mechanics:
--------------------
1. Traversal:
   - Iterate through every valid index from 0 to len(nums) - 1.
2. Equality Comparison:
   - If `nums[index] == target`, immediately return `index` (Early Exit).
3. Fallback:
   - If the entire loop finishes without encountering `target`, return `-1` to
     signal that the target element is not present.

Step-by-Step Dry Run (nums = [10, 2.5, 63, 95, 5], target = 5):
----------------------------------------------------------------
Index 0: nums[0] = 10  != 5 -> Continue
Index 1: nums[1] = 2.5 != 5 -> Continue
Index 2: nums[2] = 63  != 5 -> Continue
Index 3: nums[3] = 95  != 5 -> Continue
Index 4: nums[4] = 5   == 5 -> Target matched! Return index 4 immediately.

Complexity Analysis:
--------------------
- Time Complexity:
  - Best Case:    O(1) (Target is found at the very first index, nums[0])
  - Average Case: O(N) (Target is found near the middle; ~N / 2 comparisons)
  - Worst Case:   O(N) (Target is at the last index or not present in the list)
- Auxiliary Space: O(1) (In-place search; uses a single loop counter variable)

When to Use Linear Search vs Binary Search:
------------------------------------------
- Unsorted Data: Linear Search is the primary search strategy when elements
  are unsorted and sorting them first ($O(N \log N)$) would be wasteful.
- Small Datasets: For small lists ($N \le 64$), linear search often beats more
  complex algorithms due to cache prefetching and minimal overhead.
- Non-Random Access: Works on data structures lacking random indexing (e.g.,
  Singly Linked Lists or real-time data streams).
- Python Built-in Equivalents:
  - Membership check: `target in nums` (Returns bool, O(N))
  - Index lookup:     `nums.index(target)` (Returns index or raises ValueError)
"""


class Solution:
    """Solution class providing searching algorithms."""

    def linear_search(self, nums, target):
        """Sequentially search for target in nums; return index or -1."""
        # Traverse each index from 0 to len(nums) - 1
        for index in range(len(nums)):
            # Check if current element matches the target
            if nums[index] == target:
                return index

        # Target was not found in the entire list
        return -1


# Input array containing mixed numeric types
numbers = [10, 2.5, 63, 95, 5]


# Instantiate solution class
solution = Solution()


# Perform linear search for target 5 (Expected output: 4)
print(solution.linear_search(nums=numbers, target=5))
