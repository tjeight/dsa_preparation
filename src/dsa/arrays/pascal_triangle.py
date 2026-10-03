"""Problem: Pascal's Triangle (LeetCode #118).

Given an integer `n`, generate the first `n` rows of Pascal's triangle.

In Pascal's triangle:
- The first and last elements of every row are always 1.
- Each interior element is the sum of the two elements directly above it
  in the preceding row:
      pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

Examples:
    Input:  n = 5
    Output: [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    Input:  n = 1
    Output: [[1]]

Algorithm Strategy (Dynamic Programming / Row Construction):
------------------------------------------------------------
1. Outer Loop (Rows 1 to n):
   - For each row `i` from 1 to `n`:
     - Initialize `new_row = []`.
     - Append the leading boundary element `1`.
2. Previous Row Dependency:
   - For rows `i > 1`, retrieve the immediately preceding row:
     `previous_row = pascal_triangle[-1]`.
   - Calculate `i - 2` interior elements using `previous_row`:
     `new_row.append(previous_row[j - 1] + previous_row[j])` for `j` from 1 to `i - 2`.
   - Append the trailing boundary element `1`.
3. Row Append:
   - Append `new_row` to the master list `pascal_triangle`.

Step-by-Step Dry Run (n = 5):
-----------------------------
- i = 1: new_row = [1]
         pascal_triangle = [[1]]
- i = 2: new_row starts with [1]. Interior loop empty. Append trailing [1].
         new_row = [1, 1]
         pascal_triangle = [[1], [1, 1]]
- i = 3: prev = [1, 1]. Leading [1].
         j = 1: prev[0] + prev[1] = 1 + 1 = 2. Trailing [1].
         new_row = [1, 2, 1]
         pascal_triangle = [[1], [1, 1], [1, 2, 1]]
- i = 4: prev = [1, 2, 1]. Leading [1].
         j = 1: prev[0] + prev[1] = 1 + 2 = 3.
         j = 2: prev[1] + prev[2] = 2 + 1 = 3. Trailing [1].
         new_row = [1, 3, 3, 1]
         pascal_triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
- i = 5: prev = [1, 3, 3, 1]. Leading [1].
         j = 1: prev[0] + prev[1] = 1 + 3 = 4.
         j = 2: prev[1] + prev[2] = 3 + 3 = 6.
         j = 3: prev[2] + prev[3] = 3 + 1 = 4. Trailing [1].
         new_row = [1, 4, 6, 4, 1]
         pascal_triangle = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

Complexity Analysis:
--------------------
- Time Complexity: O(N^2)
  - Row 1 has 1 element, Row 2 has 2 elements, ..., Row N has N elements.
  - Total additions and insertions: 1 + 2 + 3 + ... + N = N * (N + 1) / 2.
  - Overall Time Complexity: O(N^2).
- Auxiliary Space: O(N^2)
  - Total elements stored in `pascal_triangle` across N rows is O(N^2).
  - Auxiliary space per row is O(N) for `new_row`.

Three Variations of Pascal's Triangle (Striver's DSA Hierarchy):
----------------------------------------------------------------
1. Variation 1 (Element at row R, column C):
   - Formula: (R - 1) C (C - 1) = (R-1)! / ((C-1)! * (R-C)!).
   - Computed in O(C) time and O(1) space.
2. Variation 2 (Generate specific N-th row):
   - Direct formula: elem = prev * (N - i) / i.
   - Computed in O(N) time and O(N) space.
3. Variation 3 (Generate complete triangle of N rows - Current):
   - Computed iteratively row by row from previous rows.
   - Computed in O(N^2) time and O(N^2) space.
"""

# Number of rows to generate
n = 5

# Master list storing all rows of Pascal's triangle
pascal_triangle = []

# Construct Pascal's triangle row by row from row 1 to n
for i in range(1, n + 1):
    new_row = []

    # First element of every row is always 1
    new_row.append(1)

    # First row has no previous row to compute interior elements from
    if i > 1:
        previous_row = pascal_triangle[-1]

        # Calculate interior elements by summing two adjacent numbers above
        for j in range(1, i - 1):
            new_row.append(previous_row[j - 1] + previous_row[j])

        # Last element of every row is always 1
        new_row.append(1)

    # Append current row to the triangle
    pascal_triangle.append(new_row)

# Print the generated Pascal's triangle
print(pascal_triangle)
