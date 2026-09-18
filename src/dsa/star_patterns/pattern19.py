"""Pattern 19: Symmetric Hollow Diamond / Split Diamond Pattern.

Example Output (for number = 4):
********
***  ***
**    **
*      *
*      *
**    **
***  ***
********

Core Idea:
- Split into two mirrored symmetric halves:
  1. Top Half:
     - Left stars: (number - row)
     - Middle spaces: row * 2
     - Right stars: (number - row)
  2. Bottom Half:
     - Left stars: (row + 1)
     - Middle spaces: (number * 2) - ((row * 2) + 2)
     - Right stars: (row + 1)
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# ========================================================
# TOP HALF: Stars decrease towards center, spaces increase
# ========================================================
for row in range(number):
    # 1. Left stars: (number - row)
    for col in range(number - row):
        print("*", end="")

    # 2. Middle spaces: starts at 0, increases by 2 per row
    for space in range(row * 2):
        print(" ", end="")

    # 3. Right stars: (number - row)
    for right_col in range(number - row):
        print("*", end="")

    # Move to the next line after completing the row
    print()

# ===========================================================
# BOTTOM HALF: Stars increase towards edges, spaces decrease
# ===========================================================
for row in range(number):
    # 1. Left stars: (row + 1)
    for col in range(row + 1):
        print("*", end="")

    # 2. Middle spaces: starts at 2*(number - 1), decreases by 2 per row
    for space in range((number * 2) - ((row * 2) + 2)):
        print(" ", end="")

    # 3. Right stars: (row + 1)
    for right_col in range(row + 1):
        print("*", end="")

    # Move to the next line after completing the row
    print()


"""
Time Complexity: O(N^2)
- Top half runs N rows, each with 2*N total characters (stars + spaces) = O(N^2).
- Bottom half runs N rows, each with 2*N total characters = O(N^2).
- Total time complexity = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
