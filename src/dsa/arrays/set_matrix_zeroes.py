"""Problem: Set Matrix Zeroes (LeetCode #73).

Given an `m x n` integer matrix, if an element is 0, set its entire row and
column to 0's.

Examples:
    Input: matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    Output: [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]

    Input: matrix = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    Output: [
        [0, 0, 0, 0],
        [0, 4, 5, 0],
        [0, 3, 1, 0]
    ]

Algorithm Strategy (Snapshot Matrix Copy / Brute-Force Baseline):
-----------------------------------------------------------------
1. The Cascading Zero Problem:
   - If a cell is set to 0 in-place during traversal, subsequent checks
     would mistake that new zero for an original zero, inadvertently zeroing
     out the entire matrix.
2. Snapshot Matrix Copy:
   - Create a reference copy: `copied_matrix = [row[:] for row in matrix]`.
   - The snapshot preserves the exact locations of genuine zeroes.
3. Propagation Phase:
   - Traverse every cell `(row, col)` in `copied_matrix`.
   - When `copied_matrix[row][col] == 0`:
     - Overwrite entire column `col` in `matrix` with 0.
     - Overwrite entire row `row` in `matrix` with 0.
4. Return modified `matrix`.

Step-by-Step Dry Run (matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]):
-------------------------------------------------------------------
M = 3, N = 3.
copied_matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

Scan copied_matrix:
- row=0, col in [0, 1, 2]: all 1s -> no action.
- row=1, col=0: 1 -> no action.
- row=1, col=1: 0 detected!
  - Zero column 1 in matrix: matrix[0][1] = 0, matrix[1][1] = 0, matrix[2][1] = 0
  - Zero row 1 in matrix:    matrix[1][0] = 0, matrix[1][1] = 0, matrix[1][2] = 0
- row=1, col=2: 1 -> no action.
- row=2, col in [0, 1, 2]: all 1s -> no action.

Final Matrix State:
  [1, 0, 1]
  [0, 0, 0]
  [1, 0, 1]

Complexity Analysis:
--------------------
- Time Complexity: O(M * N + K * (M + N))
  - Deep copy takes O(M * N).
  - Traversal scans M * N cells.
  - For K original zeroes, setting rows and columns takes O(K * (M + N)).
  - Worst Case (all zeroes): O(M * N * (M + N)).
- Auxiliary Space: O(M * N)
  - `copied_matrix` duplicates the entire M x N matrix.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Snapshot Matrix (Current Implementation):
   - Duplicate original matrix to reference initial zeroes.
   - Time: O(M * N * (M + N)), Auxiliary Space: O(M * N).
2. Better Approach (Row & Column Marker Arrays):
   - Use two auxiliary 1D arrays: row_marker of size M, col_marker of size N.
   - Pass 1: Mark rows and columns containing zeroes.
   - Pass 2: Set matrix[i][j] = 0 if row_marker[i] or col_marker[j] is set.
   - Time: O(M * N), Auxiliary Space: O(M + N).
3. Optimal Approach (In-Place First Row & Column Markers):
   - Use matrix's first row and first column as the marker arrays.
   - Use a scalar variable `col0` for column 0.
   - Time: O(M * N), Auxiliary Space: O(1) in-place.
"""


class Solution:
    """Solution class providing matrix zeroing algorithms."""

    def set_matrix_zeroes(self, matrix: list):
        """Set entire row and column to zeroes if a cell is 0 using a matrix snapshot.

        Args:
            matrix: 2D list of integers to mutate in-place.

        Returns:
            The mutated matrix with corresponding rows and columns set to zero.
        """
        # Create a deep copy snapshot to record original zero positions
        copied_matrix = [row[:] for row in matrix]

        # Scan each cell in the snapshot
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # If cell was originally zero, propagate zeroes across row and column
                if copied_matrix[row][col] == 0:
                    # Zero out the entire column
                    for i in range(len(matrix)):
                        matrix[i][col] = 0

                    # Zero out the entire row
                    for j in range(len(matrix[row])):
                        matrix[row][j] = 0

        return matrix


# Instantiate the solution class
solution = Solution()

# Example 3x3 matrix input
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# Execute and print matrix with zeroes propagated
# Expected: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(solution.set_matrix_zeroes(matrix=matrix))
