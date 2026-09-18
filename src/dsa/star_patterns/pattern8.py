"""Pattern 8: Inverted Pyramid / Inverted Equilateral Star Triangle.

Example Output (for number = 4):
*******
 *****
  ***
   *

Core Idea:
- Outer loop counts backwards from row = number down to 1 (step = -1).
- Each row consists of two parts:
  1. Leading spaces: (number - row) spaces (starts at 0, increases by 1 each row).
  2. Stars: (2 * row - 1) stars (starts at 2*number - 1, decreases by 2 each row).
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: counts down from number to 1
for row in range(number, 0, -1):
    # 1. Print leading spaces to center the stars.
    # Spaces increase by 1 for every downward row: (number - row)
    for space in range(number - row):
        print(" ", end="")

    # 2. Print odd number of stars: 2*number - 1, down to 1
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
Sum((N - row) + (2 * row - 1)) = O(N^2).

Therefore:
Time Complexity: O(N^2)

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
