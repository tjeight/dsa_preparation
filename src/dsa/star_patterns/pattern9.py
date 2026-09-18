"""Pattern 9: Diamond Star Pattern (Combined Pyramid and Inverted Pyramid).

Example Output (for number = 4):
   *
  ***
 *****
*******
*******
 *****
  ***
   *

Core Idea:
- Combine Pattern 7 (erect pyramid) and Pattern 8 (inverted pyramid).
- Part 1: Outer loop from row = 1 to number prints the upper expanding half.
- Part 2: Outer loop from row = number down to 1 prints the lower shrinking half.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# ==========================================
# PART 1: Upper Erect Pyramid (Pattern 7)
# ==========================================
for row in range(1, number + 1):
    # Print leading spaces to center the stars.
    # Spaces decrease by 1 for every row: (number - row)
    for space in range(number - row):
        print(" ", end="")

    # Print odd number of stars: 1, 3, 5, 7, ...
    # Formula: 2 * row - 1
    for column in range(1, row * 2):
        print("*", end="")

    # Move to the next line after completing each row.
    print()


"""
Time Complexity (Part 1): O(N^2)
Space Complexity (Part 1): O(1)
"""


# ==========================================
# PART 2: Lower Inverted Pyramid (Pattern 8)
# ==========================================
for row in range(number, 0, -1):
    # Print leading spaces to center the stars.
    # Spaces increase by 1 for every row: (number - row)
    for space in range(number - row):
        print(" ", end="")

    # Print odd number of stars: 2*number - 1, down to 1
    # Formula: 2 * row - 1
    for column in range(1, row * 2):
        print("*", end="")

    # Move to the next line after completing each row.
    print()


"""
Overall Complexity:
-------------------
Time Complexity: O(N^2) + O(N^2) = O(N^2)
Space Complexity: O(1)
"""
