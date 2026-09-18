"""Pattern 14: Increasing Alphabet Triangle (A, AB, ABC, ...).

Example Output (for number = 4):
A
AB
ABC
ABCD

Core Idea:
- ASCII code 65 corresponds to uppercase letter 'A'.
- In each row 'row' (0-indexed), print letters from 'A' up to the (row + 1)-th letter.
- Character printed: `chr(65 + col)`, which increments as column index increases.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: prints letters from 'A' (65 + 0) to 'A' + row (65 + row)
    for col in range(row + 1):
        print(chr(65 + col), end="")
    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs: 1 + 2 + 3 + ... + N = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
