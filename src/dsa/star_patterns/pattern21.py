"""Pattern 21: Hollow Square Star Pattern.

Example Output (for number = 4):
****
*  *
*  *
****

Core Idea:
- Print an N x N grid.
- A star '*' is printed ONLY on the boundary cells:
  - Top border: row == 0
  - Bottom border: row == number - 1
  - Left border: col == 0
  - Right border: col == number - 1
- All interior cells (where none of the above conditions hold) receive a space ' '.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: iterates through each row (0 to number - 1)
for row in range(number):
    # Inner loop: iterates through each column (0 to number - 1)
    for col in range(number):
        # Check if the current cell lies on the perimeter of the square
        if row == 0 or row == number - 1 or col == 0 or col == number - 1:
            print("*", end="")
        else:
            # Interior hollow space
            print(" ", end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs N times.
- Total iterations = N * N = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
