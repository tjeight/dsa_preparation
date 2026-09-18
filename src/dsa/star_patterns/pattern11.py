"""Pattern 11: Binary Number Triangle (Alternating 1s and 0s).

Example Output (for number = 4):
1
01
101
0101

Core Idea:
- The starting value of each row depends on its row index (0-indexed):
  - If row is even (0, 2, 4, ...): start with 1.
  - If row is odd (1, 3, 5, ...): start with 0.
- For each column in that row, alternate between 1 and 0
  using `to_print = 1 - to_print`.
"""

# Accept the input from the user
number = int(input("Enter any number: "))


to_print = 1
# Outer loop: iterates through rows from 0 to number - 1
for row in range(number):
    # Determine the starting bit: 1 for even rows, 0 for odd rows
    to_print = 1 if row % 2 == 0 else 0

    # Inner loop: prints (row + 1) alternating digits for the current row
    for col in range(row + 1):
        print(to_print, end="")
        # Toggle bit: 1 becomes 0, and 0 becomes 1
        to_print = 1 - to_print

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs: 1 + 2 + 3 + ... + N = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
