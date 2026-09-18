"""Pattern 20: Butterfly Star Pattern.

Example Output (for number = 4):
*      *
**    **
***  ***
********
***  ***
**    **
*      *

Core Idea:
- Split into two halves:
  1. Upper Half (row from 0 to number - 1):
     - Left stars: (row + 1)
     - Middle spaces: (2 * number) - (2 * row + 2)
     - Right stars: (row + 1)
  2. Lower Half (row from 1 to number - 1, avoiding duplicating the center line):
     - Left stars: (number - row)
     - Middle spaces: row * 2
     - Right stars: (number - row)
"""

# Accept the input from the user
number = int(input("Enter any number: "))


# ========================================================
# TOP HALF: Stars expand outward, center gap closes
# ========================================================
for row in range(number):
    # 1. Left wing stars: increases with row (row + 1)
    for col in range(row + 1):
        print("*", end="")

    # 2. Middle gap spaces: 2 * (number - row - 1)
    for space in range((number * 2) - ((row * 2) + 2)):
        print(" ", end="")

    # 3. Right wing stars: increases with row (row + 1)
    for right_col in range(row + 1):
        print("*", end="")

    # Move to the next line after completing each row
    print()


# ==========================================================
# BOTTOM HALF: Stars shrink inward, center gap reopens
# Starts at row = 1 so the middle line (2*number stars) is not duplicated
# ==========================================================
for row in range(1, number):
    # 1. Left wing stars: decreases with row (number - row)
    for col in range(number - row):
        print("*", end="")

    # 2. Middle gap spaces: increases with row (row * 2)
    for space in range(row * 2):
        print(" ", end="")

    # 3. Right wing stars: decreases with row (number - row)
    for right_col in range(number - row):
        print("*", end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Top half prints N rows of 2*N characters = O(N^2).
- Bottom half prints (N - 1) rows of 2*N characters = O(N^2).
- Total time complexity = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
