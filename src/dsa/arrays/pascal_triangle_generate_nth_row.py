"""Problem: Pascal's Triangle - Variation 2: Generate N-th Row (LeetCode #119).

Given an integer `r`, return the `r`-th row of Pascal's triangle.
When r = 4 (0-indexed row index 4, or 5th row), the output is [1, 4, 6, 4, 1].

In Pascal's triangle:
- Row 0: [1]
- Row 1: [1, 1]
- Row 2: [1, 2, 1]
- Row 3: [1, 3, 3, 1]
- Row 4: [1, 4, 6, 4, 1]

Examples:
    Input:  r = 4
    Output: [1, 4, 6, 4, 1]

    Input:  r = 0
    Output: [1]

    Input:  r = 1
    Output: [1, 1]

Algorithm Strategy (Iterative Row Transition / Space-Optimized DP):
-------------------------------------------------------------------
1. Space Optimization:
   - Instead of storing the complete 2D matrix (which requires O(R^2) memory),
     we only need the immediately preceding row to compute the next row.
2. Base State:
   - Initialize `previous_row = [1]`.
3. Iterative Row Construction (for i in range(1, r + 1)):
   - Initialize `new_row = []`.
   - Append leading boundary element `1`.
   - Compute interior elements:
     `new_row.append(previous_row[j - 1] + previous_row[j])` for `j` from 1 to `i - 1`.
   - Append trailing boundary element `1`.
   - Update `previous_row = new_row`.
4. Return `previous_row` after completing `r` transitions.

Step-by-Step Dry Run (r = 4):
-----------------------------
Initial: previous_row = [1]
- i = 1: new_row leading 1. j in range(1, 1) empty. new_row trailing 1.
         new_row = [1, 1] -> previous_row = [1, 1]
- i = 2: new_row leading 1.
         j = 1: prev[0] + prev[1] = 1 + 1 = 2.
         new_row trailing 1.
         new_row = [1, 2, 1] -> previous_row = [1, 2, 1]
- i = 3: new_row leading 1.
         j = 1: prev[0] + prev[1] = 1 + 2 = 3.
         j = 2: prev[1] + prev[2] = 2 + 1 = 3.
         new_row trailing 1.
         new_row = [1, 3, 3, 1] -> previous_row = [1, 3, 3, 1]
- i = 4: new_row leading 1.
         j = 1: prev[0] + prev[1] = 1 + 3 = 4.
         j = 2: prev[1] + prev[2] = 3 + 3 = 6.
         j = 3: prev[2] + prev[3] = 3 + 1 = 4.
         new_row trailing 1.
         new_row = [1, 4, 6, 4, 1] -> previous_row = [1, 4, 6, 4, 1]
Final Return: [1, 4, 6, 4, 1]

Complexity Analysis:
--------------------
- Time Complexity: O(R^2)
  - Computes row 1 (2 elements), row 2 (3 elements), ..., row R (R+1 elements).
  - Total additions: 1 + 2 + ... + R = R * (R + 1) / 2 = O(R^2).
- Auxiliary Space: O(R)
  - Stores only `previous_row` and `new_row` of length at most R + 1.
  - Achieves significant memory savings over O(R^2) full triangle generation.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Full Matrix Generation:
   - Generate all rows in a 2D matrix, return matrix[r].
   - Time: O(R^2), Auxiliary Space: O(R^2).
2. Space-Optimized DP (Current Implementation):
   - Transition iteratively maintaining only the prior row.
   - Time: O(R^2), Auxiliary Space: O(R).
3. Optimal Combinatorics Formula:
   - Compute each element using running multiplication:
     elem = prev_elem * (r - col + 1) // col.
   - Time: O(R), Auxiliary Space: O(1) (excluding output row).
"""


class Solution:
    """Solution class providing Pascal's triangle row generation algorithms."""

    def generate_nth_row_of_pascal_triangle(self, r):
        """Generate the r-th row of Pascal's triangle using iterative DP.

        Args:
            r: Row index to generate (0-indexed).

        Returns:
            List of integers representing the r-th row of Pascal's triangle.
        """
        # Base row for r = 0
        previous_row = [1]

        # Iteratively build each successive row up to r
        for i in range(1, r + 1):
            new_row = []

            # First element of every row is always 1
            new_row.append(1)

            # Compute interior elements by summing adjacent numbers from previous row
            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])

            # Last element of every row is always 1
            new_row.append(1)

            # Advance previous_row reference for next iteration
            previous_row = new_row

        return previous_row


# Instantiate the solution class
solution = Solution()

# Execute and print the 4th row (Expected output: [1, 4, 6, 4, 1])
print(solution.generate_nth_row_of_pascal_triangle(4))
