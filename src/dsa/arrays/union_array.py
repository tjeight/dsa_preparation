"""Problem: Union of Two Sorted Arrays.

Given two sorted arrays `first_array` and `second_array`, find their union.
The union of two arrays contains all distinct elements from both arrays
arranged in sorted ascending order.

Examples:
    Input:  nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
    Output: [1, 2, 3, 4, 5, 7]

    Input:  nums1 = [2, 2, 3, 4, 5], nums2 = [1, 1, 2, 3, 4]
    Output: [1, 2, 3, 4, 5]

    Input:  nums1 = [1, 1, 1], nums2 = [2, 2, 2]
    Output: [1, 2]

Algorithm Strategy (Two-Pointer Linear Merge):
----------------------------------------------
1. Pointer Invariants:
   - `i`: Pointer for `first_array` starting at index 0.
   - `j`: Pointer for `second_array` starting at index 0.
   - `union_array`: Output list accumulating unique sorted elements.
2. Deduplication Invariant:
   - Since both inputs are sorted, the merged stream arrives in non-decreasing
     order.
   - An element `val` is unique if `union_array` is empty OR `val != union_array[-1]`.
3. Simultaneous Traversal (while i < N and j < M):
   - Case 1: `first_array[i] <= second_array[j]`:
     - If distinct, append `first_array[i]` to `union_array`.
     - Increment `i += 1`.
   - Case 2: `second_array[j] < first_array[i]`:
     - If distinct, append `second_array[j]` to `union_array`.
     - Increment `j += 1`.
4. Suffix Drains:
   - Append any remaining unique elements from `first_array` (while i < N).
   - Append any remaining unique elements from `second_array` (while j < M).
5. Return:
   - `union_array` with all distinct elements in ascending order.

Step-by-Step Dry Run (nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]):
-------------------------------------------------------------------
first_length = 5, second_length = 3.
- i=0, j=0: nums1[0]=1 <= nums2[0]=1. union_array empty -> append 1. i=1.
- i=1, j=0: nums1[1]=2 > nums2[0]=1. nums2[0]=1 == union[-1] -> skip. j=1.
- i=1, j=1: nums1[1]=2 <= nums2[1]=2. 2 != union[-1] -> append 2. i=2.
- i=2, j=1: nums1[2]=3 > nums2[1]=2. nums2[1]=2 == union[-1] -> skip. j=2.
- i=2, j=2: nums1[2]=3 <= nums2[2]=7. 3 != union[-1] -> append 3. i=3.
- i=3, j=2: nums1[3]=4 <= nums2[2]=7. 4 != union[-1] -> append 4. i=4.
- i=4, j=2: nums1[4]=5 <= nums2[2]=7. 5 != union[-1] -> append 5. i=5.
Main loop ends (i = 5).
Suffix nums2 drain:
- j=2: nums2[2]=7. 7 != union[-1] -> append 7. j=3.
Final Return: [1, 2, 3, 4, 5, 7]

Complexity Analysis:
--------------------
- Time Complexity: O(N + M)
  - Every iteration increments at least one pointer (i or j).
  - At most N + M total pointer advances.
  - Tail comparisons (`union_array[-1]`) and appends are O(1).
- Auxiliary Space: O(1) (excluding output array)
  - Operates using only two integer pointers (`i`, `j`).
  - Output space for `union_array`: O(N + M) in worst case (disjoint arrays).

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Set / Hash Map):
   - Insert all elements from both lists into a set, then sort.
   - Time: O((N + M) log(N + M)), Auxiliary Space: O(N + M).
2. Optimal (Two-Pointer Linear Merge - Current Implementation):
   - Directly exploits pre-sorted property in a single simultaneous pass.
   - Time: O(N + M), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing array merging and union algorithms."""

    def union_of_array(self, first_array, second_array):
        """Compute the sorted union of two sorted arrays without duplicates.

        Args:
            first_array: First sorted list of integers.
            second_array: Second sorted list of integers.

        Returns:
            A new list containing unique elements from both arrays in sorted order.
        """
        first_length = len(first_array)
        second_length = len(second_array)

        union_array = []
        i = 0
        j = 0

        # Traverse both arrays simultaneously comparing current elements
        while i < first_length and j < second_length:
            if first_array[i] <= second_array[j]:
                # Add element if union_array is empty or element is not duplicate
                if not union_array or first_array[i] != union_array[-1]:
                    union_array.append(first_array[i])
                i += 1
            else:
                # Add element if union_array is empty or element is not duplicate
                if not union_array or second_array[j] != union_array[-1]:
                    union_array.append(second_array[j])
                j += 1

        # Drain any remaining elements from first_array
        while i < first_length:
            if not union_array or first_array[i] != union_array[-1]:
                union_array.append(first_array[i])
            i += 1

        # Drain any remaining elements from second_array
        while j < second_length:
            if not union_array or second_array[j] != union_array[-1]:
                union_array.append(second_array[j])
            j += 1

        return union_array


# Instantiate the solution class
solution = Solution()

# Example sorted arrays
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 2, 7]

# Execute and print union of arrays (Expected output: [1, 2, 3, 4, 5, 7])
print(solution.union_of_array(first_array=nums1, second_array=nums2))
