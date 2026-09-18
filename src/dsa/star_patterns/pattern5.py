"""Pattern 5: Inverted Right-Angled Triangle with Numbers.

Example Output (for number = 4):
1234
123
12
1

Core Idea:
- Outer loop runs 'number' times (row from 0 to number - 1).
- In row 0: prints 1 to number (number digits).
- In row 1: prints 1 to number - 1 (number - 1 digits).
- In row 'row': prints 1 up to (number - row).
"""

# Accept the input from the user
number = int(input("Enter any number: "))


# Trick find the rows and columns.
# The iterations are simple make that much rows when there are that much columns

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: prints column numbers from 1 to (number - row)
    for column in range(1, (number - row) + 1):
        print(column, end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs: n + (n - 1) + ... + 1 = n * (n + 1) / 2 = O(n^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
