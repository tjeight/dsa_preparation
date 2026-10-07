"""Problem: Rotate Image / Rotate Matrix by 90 Degrees Clockwise (LeetCode #48).

Given an `n x n` 2D matrix representing an image, rotate the image by 90 degrees
clockwise in-place without allocating another 2D matrix.

Examples:
    Input: matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Output: [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    Input: matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    Output: [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]

Algorithm Strategy (In-Place Transpose + Row Reversal):
-------------------------------------------------------
1. Mathematical Foundation:
   Rotating a matrix 90 degrees clockwise maps each element at (row, col)
   to (col, n - 1 - row).
   This transformation is equivalent to two consecutive matrix operations:
   - Step 1: Transpose the matrix -> maps (row, col) to (col, row).
   - Step 2: Reverse each row -> maps (col, row) to (col, n - 1 - row).

2. Transposition (Upper Triangle Swap):
   - Traverse all cells (row, col) where `row < col`.
   - Swap `matrix[row][col]` with `matrix[col][row]`.
   - The condition `row < col` ensures each pair is swapped exactly once.

3. Horizontal Reflection:
   - Reverse each row in-place: `matrix[row].reverse()`.

Step-by-Step Dry Run (matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
-------------------------------------------------------------------
Initial Matrix:
  [1, 2, 3]
  [4, 5, 6]
  [7, 8, 9]

Phase 1: Transpose (swap across main diagonal where row < col):
- row=0, col=1: swap matrix[0][1] (2) <-> matrix[1][0] (4)
- row=0, col=2: swap matrix[0][2] (3) <-> matrix[2][0] (7)
- row=1, col=2: swap matrix[1][2] (6) <-> matrix[2][1] (8)
Transposed State:
  [1, 4, 7]
  [2, 5, 8]
  [3, 6, 9]

Phase 2: Reverse each individual row:
- Row 0: [1, 4, 7] -> [7, 4, 1]
- Row 1: [2, 5, 8] -> [8, 5, 2]
- Row 2: [3, 6, 9] -> [9, 6, 3]

Final Result:
  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Complexity Analysis:
--------------------
- Time Complexity: O(N^2)
  - Transposition visits all N^2 cells and performs N*(N - 1)/2 swaps -> O(N^2).
  - Row reversal takes N * (N / 2) swaps -> O(N^2).
  - Total Time: O(N^2).
- Auxiliary Space: O(1)
  - Operates strictly in-place; modifies existing matrix with zero extra allocations.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (Auxiliary Matrix):
   - Allocate new N x N matrix: ans[col][n - 1 - row] = matrix[row][col].
   - Time: O(N^2), Auxiliary Space: O(N^2).
2. Optimal (In-Place Transpose & Reverse - Current Implementation):
   - Rotate in-place via diagonal transposition and row reversals.
   - Time: O(N^2), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing in-place 2D matrix transformation algorithms."""

    def rotate_matrix_by_90(self, matrix):
        """Rotate an n x n 2D matrix by 90 degrees clockwise in-place.

        Args:
            matrix: 2D square list of integers representing an image.

        Returns:
            The rotated matrix (mutated in-place).
        """
        rows = cols = len(matrix)

        # Step 1: Transpose the matrix by swapping elements across main diagonal
        for row in range(rows):
            for col in range(cols):
                # Only swap upper triangle elements to avoid double swapping
                if row < col:
                    matrix[row][col], matrix[col][row] = (
                        matrix[col][row],
                        matrix[row][col],
                    )

        # Step 2: Reverse each row horizontally to complete 90-degree clockwise rotation
        for row in range(rows):
            matrix[row].reverse()

        return matrix


# Instantiate the solution class
solution = Solution()

# Example 3x3 matrix input
# Execute and print rotated matrix (Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
print(solution.rotate_matrix_by_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
