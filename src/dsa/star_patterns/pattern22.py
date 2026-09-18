"""Pattern 22: Concentric Number Squares / Number Spiral.

Example Output (for number = 4):
4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 

Core Idea:
- Total dimension of the grid: size = 2 * number - 1.
- Each cell (row, col) has 4 distances to the outer boundary edges:
  1. Top edge: row
  2. Left edge: col
  3. Bottom edge: size - 1 - row
  4. Right edge: size - 1 - col
- The distance from the closest boundary is:
  min(row, col, size - 1 - row, size - 1 - col).
- Outer border (distance = 0) -> value = number - 0 = number.
- Next inner layer (distance = 1) -> value = number - 1.
- Innermost center (distance = number - 1) -> value = number - (number - 1) = 1.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Total width and height of the concentric square matrix
size = 2 * number - 1

# Outer loop: iterates over all rows in the (2*N - 1) x (2*N - 1) grid
for row in range(size):
    # Inner loop: iterates over all columns in the row
    for col in range(size):
        # Find the minimum distance from the current cell to any of the 4 outer borders
        distance = min(row, col, size - 1 - row, size - 1 - col)

        # Outer layer = number, next layer = number - 1, ... down to 1 at the center
        value = number - distance

        print(value, end=" ")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O((2*N - 1)^2) = O(N^2)
- Total cells = (2*N - 1) * (2*N - 1) = 4*N^2 - 4*N + 1 = O(N^2).
- Each cell performs O(1) min and arithmetic calculations.

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
