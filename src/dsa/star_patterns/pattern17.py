"""Pattern 17: Palindromic Alphabet Pyramid.

Example Output (for number = 4):
    A
   ABA
  ABCBA
 ABCDCBA

Core Idea:
- Outer loop runs from row = 0 to number - 1.
- Each row consists of 3 sections:
  1. Leading spaces: spaces // 2 = (number - row) spaces to center the pyramid.
  2. Ascending characters: from 'A' up to 'A' + row (col = 0 to row).
  3. Descending characters: from 'A' + row - 1 back down to 'A'
     (reverse = row - 1 down to 0).
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: controls rows (0 to number - 1)
for row in range(number):
    # Total spaces allocated for padding
    spaces = 2 * (number - row)

    # 1. Print leading spaces to center-align the pyramid
    for left_space in range(spaces // 2):
        print(" ", end="")

    # 2. Print characters in ascending order from 'A' to the peak character
    for col in range(row + 1):
        print(chr(65 + col), end="")

    # 3. Print characters in descending order from peak - 1 down to 'A'
    for reverse in range(row - 1, -1, -1):
        print(chr(65 + reverse), end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Leading spaces: N - row iterations.
- Ascending characters: row + 1 iterations.
- Descending characters: row iterations.
- Total work per row = (N - row) + (2 * row + 1) = N + row + 1 = O(N).
- Total time across N rows = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
