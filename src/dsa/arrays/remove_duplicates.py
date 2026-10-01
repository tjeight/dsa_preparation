"""Problem: Remove Duplicates from Sorted Array (LeetCode #26).

Given an integer array `nums` sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order
of the elements must be preserved.

Return the number of unique elements `k`. The first `k` elements of `nums`
should hold the final unique elements. Elements beyond index `k - 1` are
don't-care values.

Examples:
    Input:  nums = [1, 1, 2]
    Output: 2, nums = [1, 2, _]

    Input:  nums = [0, 0, 3, 3, 5, 6]
    Output: 4, nums = [0, 3, 5, 6, _, _]

    Input:  nums = []
    Output: 0

    Input:  nums = [7]
    Output: 1, nums = [7]

Algorithm Strategy (Two-Pointer In-Place Placement):
----------------------------------------------------
1. Precondition & Sorted Invariant:
   - Because the array is sorted, identical values are strictly contiguous.
   - The first element `nums[0]` is always the first unique element.
2. Pointer Invariants:
   - `index` (slow pointer): Points to the destination index where the next
     unique element should be written. Initialized to 1.
   - `i` (fast pointer / scanner): Iterates through `range(1, len(nums))`.
3. Traversal:
   - Compare `nums[i]` with the previous element `nums[i - 1]`.
   - If `nums[i] != nums[i - 1]`:
     - A new distinct element is discovered.
     - Write it to the destination: `nums[index] = nums[i]`.
     - Increment `index += 1`.
   - If `nums[i] == nums[i - 1]`:
     - Duplicate value; ignore and continue scanning.
4. Return:
   - `index` represents the total count of unique elements, with `nums[0:index]`
     containing all unique elements in sorted order.

Step-by-Step Dry Run (nums = [0, 0, 3, 3, 5, 6]):
--------------------------------------------------
N = 6. Initial: index = 1.
- i = 1: nums[1] (0) == nums[0] (0) -> Duplicate. index remains 1.
- i = 2: nums[2] (3) != nums[1] (0) -> Unique found!
         nums[1] = nums[2] (3), index becomes 2.
         Array: [0, 3, 3, 3, 5, 6]
- i = 3: nums[3] (3) == nums[2] (3) -> Duplicate. index remains 2.
- i = 4: nums[4] (5) != nums[3] (3) -> Unique found!
         nums[2] = nums[4] (5), index becomes 3.
         Array: [0, 3, 5, 3, 5, 6]
- i = 5: nums[5] (6) != nums[4] (5) -> Unique found!
         nums[3] = nums[5] (6), index becomes 4.
         Array: [0, 3, 5, 6, 5, 6]
Loop ends.
Mutated Array: [0, 3, 5, 6, 5, 6] (First 4 elements [0, 3, 5, 6] are unique)
Final Return: 4

Complexity Analysis:
--------------------
- Time Complexity: O(N)
  - Single pass scanning N elements from index 1 to N - 1.
  - Each step does O(1) comparison and at most one write assignment.
- Auxiliary Space: O(1)
  - Modifies the array strictly in-place with two scalar pointers (`index`, `i`).

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Hash Set / TreeSet):
   - Insert all elements into a hash set / ordered set to deduplicate.
   - Copy unique elements back to nums.
   - Time: O(N) or O(N log N), Auxiliary Space: O(N).
2. Optimal (Two-Pointer In-Place - Current Implementation):
   - Exploits sorted order to overwrite duplicates in-place.
   - Time: O(N), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing array deduplication algorithms."""

    def remove_duplicates(self, nums):
        """Remove duplicates in-place from a sorted array.

        Args:
            nums: List of sorted integers (non-decreasing).

        Returns:
            The count of unique elements (k). The first k elements of nums
            contain the unique elements.
        """
        # Condition is array is sorted
        # Edge case: empty list contains 0 unique elements
        if not nums:
            return 0

        # Slow pointer: next position to place a unique element
        index = 1

        # Fast pointer: scan array starting from the second element
        for i in range(1, len(nums)):
            # If current element is different from previous, it is a new unique value
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1

        print(nums)
        return index


# Instantiate the solution class
solution = Solution()

# Example sorted array with duplicate elements
nums = [0, 0, 3, 3, 5, 6]

# Execute and print the number of unique elements (Expected output: 4)
print(solution.remove_duplicates(nums=nums))
