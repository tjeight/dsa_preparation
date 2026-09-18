"""Pattern 16: Repeated Letter Alphabet Triangle (A, BB, CCC, DDDD).

Example Output (for number = 4):
A
BB
CCC
DDDD

Core Idea:
- Outer loop runs 'number' times (row from 0 to number - 1).
- In each row 'row', the letter to print is fixed: `chr(65 + row)`.
  - Row 0 prints 'A' repeated 1 time.
  - Row 1 prints 'B' repeated 2 times.
  - Row 'row' prints the corresponding alphabet (row + 1) times.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: prints the same character chr(65 + row) repeated (row + 1) times
    for col in range(row + 1):
        print(chr(65 + row), end="")
    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs: 1 + 2 + 3 + ... + N = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
