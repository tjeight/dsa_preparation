"""Problem: Intersection of Two Sorted Arrays.

Given two arrays `nums1` and `nums2`, find their intersection.
The intersection consists of common elements present in both arrays.
When both arrays are sorted in ascending order, the intersection can be
computed efficiently in linear time using a two-pointer approach.

Examples:
    Input:  nums1 = [1, 2, 2, 3, 4], nums2 = [2, 2, 3, 5]
    Output: [2, 2, 3]

    Input:  nums1 = [1, 3, 5, 9], nums2 = [5, 9, 8]
    Output: [5, 9]

    Input:  nums1 = [1, 2, 3], nums2 = [4, 5, 6]
    Output: []

Algorithm Strategy (Two-Pointer Linear Scan):
---------------------------------------------
1. Precondition (Sorted Invariant):
   - The two-pointer intersection strategy relies on both input arrays
     being sorted in non-decreasing order.
2. Pointer Invariants:
   - `i`: Pointer for `nums1` starting at index 0.
   - `j`: Pointer for `nums2` starting at index 0.
   - `intersection_array`: Output list accumulating common elements.
3. Simultaneous Traversal (while i < len(nums1) and j < len(nums2)):
   - Case 1 (`nums1[i] == nums2[j]`):
     - Common element found. Append `nums1[i]` to `intersection_array`.
     - Advance both pointers: `i += 1`, `j += 1`.
   - Case 2 (`nums1[i] < nums2[j]`):
     - The value at `nums1[i]` is smaller than `nums2[j]`. Because `nums1` is
       sorted, no subsequent element in `nums2` can match `nums1[i]`.
     - Advance `i += 1`.
   - Case 3 (`nums1[i] > nums2[j]`):
     - The value at `nums2[j]` is smaller than `nums1[i]`. Because `nums2` is
       sorted, no subsequent element in `nums1` can match `nums2[j]`.
     - Advance `j += 1`.
4. Early Termination:
   - Once either array is exhausted, no further mutual elements can exist.
   - Return `intersection_array`.

Step-by-Step Dry Run (nums1 = [1, 3, 5, 9], nums2 = [5, 9, 8]):
----------------------------------------------------------------
Initial: i = 0, j = 0, intersection_array = []
- Step 1: nums1[0] = 1, nums2[0] = 5.
          nums1[i] < nums2[j] (1 < 5) -> i += 1 (i = 1).
- Step 2: nums1[1] = 3, nums2[0] = 5.
          nums1[i] < nums2[j] (3 < 5) -> i += 1 (i = 2).
- Step 3: nums1[2] = 5, nums2[0] = 5.
          nums1[i] == nums2[j] (5 == 5) -> Append 5.
          i += 1 (i = 3), j += 1 (j = 1).
          intersection_array = [5].
- Step 4: nums1[3] = 9, nums2[1] = 9.
          nums1[i] == nums2[j] (9 == 9) -> Append 9.
          i += 1 (i = 4), j += 1 (j = 2).
          intersection_array = [5, 9].
Loop ends since i = 4 == len(nums1).
Final Return: [5, 9]

Complexity Analysis:
--------------------
- Time Complexity: O(N + M)
  - N = len(nums1), M = len(nums2).
  - In each step, at least one pointer (i or j) increments.
  - At most N + M total comparisons and iterations.
- Auxiliary Space: O(1) (excluding output array)
  - Operates using only two integer pointers (`i`, `j`).
  - Output space for `intersection_array`: O(min(N, M)) in worst case.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Nested Loop with Visited Array):
   - For each element in nums1, linearly scan nums2.
   - Maintain a visited boolean array for nums2 to avoid reusing elements.
   - Time: O(N * M), Auxiliary Space: O(M).
2. Better Approach (Hash Map / Frequency Counter):
   - Count frequencies of elements in nums1 using a hash map.
   - Iterate through nums2, decrementing counts and appending matched elements.
   - Time: O(N + M), Auxiliary Space: O(N).
3. Optimal Approach (Two-Pointer Scan - Current Implementation):
   - Assumes sorted inputs; processes both lists linearly without extra memory.
   - Time: O(N + M), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing array intersection algorithms."""

    def intersectionOfArrays(self, nums1, nums2):
        """Compute the intersection of two sorted arrays using two pointers.

        Args:
            nums1: First sorted list of integers.
            nums2: Second sorted list of integers.

        Returns:
            A list containing common elements present in both arrays.
        """
        # Pointer for nums1
        i = 0
        # Pointer for nums2
        j = 0
        # Output list for common elements
        intersection_array = []

        # Traverse both arrays simultaneously until one is exhausted
        while i < len(nums1) and j < len(nums2):
            # Case 1: Match found, record element and advance both pointers
            if nums1[i] == nums2[j]:
                intersection_array.append(nums1[i])
                i += 1
                j += 1
            # Case 2: nums1 element is smaller, advance pointer i
            elif nums1[i] < nums2[j]:
                i += 1
            # Case 3: nums2 element is smaller, advance pointer j
            else:
                j += 1

        return intersection_array


# Instantiate the solution class
solution = Solution()

# Example input arrays
nums1 = [1, 3, 5, 9]
nums2 = [5, 9, 8]

# Execute and print array intersection (Expected output: [5, 9])
print(solution.intersectionOfArrays(nums1=nums1, nums2=nums2))
