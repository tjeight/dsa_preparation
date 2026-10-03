"""Problem: Pascal's Triangle - Element at (Row r, Column c) (1-indexed).

Given row number `r` and column number `c` (1-indexed), find and return the
element at that specific position in Pascal's triangle.

Examples:
    Input:  r = 4, c = 2
    Output: 3
    Explanation: Row 4 of Pascal's triangle is [1, 3, 3, 1].
                 The 2nd element is 3.

    Input:  r = 5, c = 3
    Output: 6
    Explanation: Row 5 is [1, 4, 6, 4, 1]. The 3rd element is 6.

    Input:  r = 1, c = 1
    Output: 1

Algorithm Strategy (Full Generation vs Mathematical Formula):
-------------------------------------------------------------
1. Current Approach (Full Row Generation):
   - Helper `generate_pascal_triangle(n)`:
     Constructs all rows from 1 up to `r` using dynamic programming:
     `new_row[j] = previous_row[j - 1] + previous_row[j]`.
   - Indexing:
     Pascal's triangle is 1-indexed in problem definition. Convert to 0-indexed:
     `return pascal_triangle[r - 1][c - 1]`.
   - Time Complexity: O(R^2).
   - Space Complexity: O(R^2).

2. Optimal Approach (Combinatorics nCr Shortcut):
   - In Pascal's triangle, element at (r, c) equals:
     C(r - 1, c - 1) = (r - 1)! / ((c - 1)! * (r - c)!)
   - Can be computed in O(c) time and O(1) space:
     res = 1
     for i in range(c - 1):
         res = res * (r - 1 - i) // (i + 1)
   - Bypasses generating intermediate rows completely.

Step-by-Step Dry Run (r = 4, c = 2):
------------------------------------
1. Call `generate_pascal_triangle(n = 4)`:
   - Row 1: [1]
   - Row 2: [1, 1]
   - Row 3: [1, 2, 1]
   - Row 4: [1, 3, 3, 1]
2. Lookup:
   - Target position in 0-indexed matrix: [r - 1][c - 1] = [3][1].
   - Value at Row 4 (index 3), Column 2 (index 1) is 3.
3. Mathematical Verification:
   - C(4 - 1, 2 - 1) = C(3, 1) = 3! / (1! * 2!) = 3.
Final Return: 3

Complexity Analysis:
--------------------
- Current Approach:
  - Time Complexity: O(R^2) (generates R rows with R*(R+1)/2 elements).
  - Auxiliary Space: O(R^2) (stores all R rows in memory).
- Optimal Combinatorics Approach:
  - Time Complexity: O(C).
  - Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing Pascal's triangle query algorithms."""

    def generate_pascal_triangle(self, n):
        """Generate first n rows of Pascal's triangle using dynamic programming.

        Args:
            n: Number of rows to generate.

        Returns:
            2D list representing the first n rows of Pascal's triangle.
        """
        pascal_triangle = []

        for i in range(1, n + 1):
            new_row = []
            new_row.append(1)

            if i > 1:
                previous_row = pascal_triangle[-1]
                for j in range(1, i - 1):
                    new_row.append(previous_row[j - 1] + previous_row[j])
                new_row.append(1)

            pascal_triangle.append(new_row)
        return pascal_triangle

    def getRthCthElement(self, r, c):
        """Retrieve element at row r and column c (1-indexed).

        Args:
            r: 1-indexed row number.
            c: 1-indexed column number.

        Returns:
            The integer element located at row r and column c.
        """
        pascal_triangle = self.generate_pascal_triangle(n=r)

        return pascal_triangle[r-1][c-1]


# Instantiate the solution class
solution = Solution()

# 1-indexed row and column coordinates
r = 4
c = 2

# Execute and print the element at position (r, c) (Expected output: 3)
print(solution.getRthCthElement(c=c, r=r))
