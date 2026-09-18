"""Pattern 15: Inverted Alphabet Triangle (ABCD, ABC, AB, A).

Example Output (for number = 4):
ABCD
ABC
AB
A

Core Idea:
- Outer loop runs 'number' times (row from 0 to number - 1).
- In each row 'row', print letters starting at 'A' (65) up to `number - row` letters.
- The number of characters decreases by 1 in each subsequent row.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: prints (number - row) letters starting from 'A' (col = 0)
    for col in range(number - row):
        print(chr(65 + col), end="")
    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs: N + (N - 1) + ... + 1 = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
