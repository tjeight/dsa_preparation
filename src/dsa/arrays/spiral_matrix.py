"""Problem: Spiral Matrix (LeetCode #54).

Given an `m x n` matrix, return all elements of the matrix in clockwise
spiral order.

Examples:
    Input: matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    Input: matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    Input: matrix = [[1, 2, 3]]
    Output: [1, 2, 3]

Algorithm Strategy (Layer-by-Layer Boundary Shrinking):
-------------------------------------------------------
1. Maintain 4 Boundary Pointers:
   - `top_row = 0`: Starting row of current outer layer.
   - `bottom_row = len(matrix) - 1`: Ending row of current outer layer.
   - `left_column = 0`: Starting column of current outer layer.
   - `right_column = len(matrix[0]) - 1`: Ending column of current outer layer.

2. Clockwise Traversal per Layer:
   Loop while `top_row <= bottom_row` and `left_column <= right_column`:
   - Step 1 (Left to Right):
     Traverse across `top_row` from `left_column` to `right_column`.
     Increment `top_row += 1` to close the processed row.
   - Step 2 (Top to Bottom):
     Traverse down `right_column` from `top_row` to `bottom_row`.
     Decrement `right_column -= 1` to close the processed column.
   - Step 3 (Right to Left):
     Guard: `if top_row <= bottom_row:` (verifies row boundary remains valid).
     Traverse across `bottom_row` from `right_column` down to `left_column`.
     Decrement `bottom_row -= 1` to close the processed row.
   - Step 4 (Bottom to Top):
     Guard: `if left_column <= right_column:` (verifies column boundary remains valid).
     Traverse up `left_column` from `bottom_row` down to `top_row`.
     Increment `left_column += 1` to close the processed column.

3. Return `result` when all layers have collapsed.

Step-by-Step Dry Run (matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
-------------------------------------------------------------------
Initial Boundaries: top_row = 0, bottom_row = 2, left_column = 0, right_column = 2.
Layer 1:
- Step 1 (Left -> Right along top_row=0):
  col in [0, 1, 2] -> append 1, 2, 3. top_row becomes 1.
- Step 2 (Top -> Bottom along right_column=2):
  row in [1, 2]    -> append 6, 9.    right_column becomes 1.
- Step 3 (Right -> Left along bottom_row=2):
  top_row (1) <= bottom_row (2) True:
  col in [1, 0]    -> append 8, 7.    bottom_row becomes 1.
- Step 4 (Bottom -> Top along left_column=0):
  left_col (0) <= right_col (1) True:
  row in [1]       -> append 4.       left_column becomes 1.

Layer 2 (top_row=1, bottom_row=1, left_column=1, right_column=1):
- Step 1 (Left -> Right along top_row=1):
  col in [1]       -> append 5.       top_row becomes 2.
- Step 2: row in range(2, 2) is empty. right_column becomes 0.
- Step 3: top_row (2) <= bottom_row (1) False.
- Step 4: left_column (1) <= right_column (0) False.

Loop terminates.
Final Return: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Complexity Analysis:
--------------------
- Time Complexity: O(M * N)
  - Every element of the M x N matrix is visited exactly once.
- Auxiliary Space: O(1) (excluding output array)
  - Modifies only 4 boundary scalar pointers (`top_row`, `bottom_row`,
    `left_column`, `right_column`).
  - Output space for `result`: O(M * N).
"""


class Solution:
    """Solution class providing 2D matrix traversal algorithms."""

    def spiralOrder(self, matrix):
        """Return all elements of the matrix in clockwise spiral order.

        Args:
            matrix: 2D list of integers of dimensions m x n.

        Returns:
            A list containing matrix elements traversed in clockwise spiral order.
        """
        result = []

        top_row = 0
        left_column = 0
        bottom_row = len(matrix) - 1
        right_column = len(matrix[0]) - 1

        while top_row <= bottom_row and left_column <= right_column:
            # First step: traverse from left to right along top_row
            for column_iterator in range(left_column, right_column + 1):
                result.append(matrix[top_row][column_iterator])

            # Top row completed; shift boundary downward
            top_row += 1

            # Second step: traverse from top to bottom along right_column
            for row_iterator in range(top_row, bottom_row + 1):
                result.append(matrix[row_iterator][right_column])

            # Right column completed; shift boundary leftward
            right_column -= 1

            # Third step: traverse from right to left along bottom_row
            # Guard check ensures row boundary has not crossed
            if top_row <= bottom_row:
                for column_iterator in range(right_column, left_column - 1, -1):
                    result.append(matrix[bottom_row][column_iterator])

                # Bottom row completed; shift boundary upward
                bottom_row -= 1

            # Fourth step: traverse from bottom to top along left_column
            # Guard check ensures column boundary has not crossed
            if left_column <= right_column:
                for row_iterator in range(bottom_row, top_row - 1, -1):
                    result.append(matrix[row_iterator][left_column])

                # Left column completed; shift boundary rightward
                left_column += 1

        return result


# Instantiate the solution class
solution = Solution()

# Example 3x3 matrix input
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Execute and print spiral order traversal (Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5])
print(solution.spiralOrder(matrix=matrix))
