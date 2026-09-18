"""Pattern 10: Half Diamond / Sideways Triangle of Stars.

Example Output (for number = 4):
*
**
***
***
**
*

Core Idea:
- Split into two symmetric parts:
  1. Upper half: increasing rows of stars from 1 up to number - 1.
  2. Lower half: decreasing rows of stars from number - 1 down to 1.
- Uses string multiplication '*' * row for clean single-line row printing.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Part 1: Increasing pattern (row 1 up to number - 1)
for row in range(1, number):
    print("*" * row)

# Part 2: Decreasing stars (row number - 1 down to 1)
for row in range(number - 1, 0, -1):
    print("*" * row)


"""
Time Complexity: O(N^2)
- First loop prints 1 + 2 + ... + (N - 1) stars = O(N^2).
- Second loop prints (N - 1) + ... + 1 stars = O(N^2).
- Total time complexity = O(N^2).

Space Complexity: O(1) (or O(N) temporary string for each print buffer)
"""
