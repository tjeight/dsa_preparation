"""Pattern 7: Full Pyramid / Equilateral Star Triangle.

Example Output (for number = 4):
   *
  ***
 *****
*******

Core Idea:
- Outer loop runs from row = 1 to number.
- Each row consists of two parts:
  1. Leading spaces: (number - row) spaces to center the pyramid.
  2. Stars: (2 * row - 1) stars (odd sequence: 1, 3, 5, 7, ...).
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: controls row numbers from 1 to number
for row in range(1, number + 1):
    # 1. Print leading spaces to center the stars.
    # Spaces decrease by 1 for every subsequent row: (number - row)
    for space in range(number - row):
        print(" ", end="")

    # 2. Print odd number of stars: 1, 3, 5, 7, ...
    # Formula: (2 * row - 1), represented by range(1, row * 2)
    for column in range(1, row * 2):
        print("*", end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity:
----------------
Outer loop runs N times.

For each row:
    - Spaces: N - row
    - Stars: 2 * row - 1

Total work across all rows:
Sum((N - row) + (2 * row - 1)) = Sum(N + row - 1) = O(N^2).

Therefore:
Time Complexity: O(N^2)

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
