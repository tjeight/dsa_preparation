"""Pattern 3: Right-Angled Triangle with Increasing Numbers per Row.

Example Output (for number = 4):
1
12
123
1234

Core Idea:
- Outer loop runs from 1 to number (1-indexed).
- In each row 'row', print numbers starting from 1 up to 'row'.
- The value printed is the column index itself.
"""

# Accept the input from the user
number = int(input("Enter any number: "))


# Trick find the rows and columns.
# The iterations are simple make that much rows when there are that much columns

# Outer loop: controls row index from 1 to number
for row in range(1, number + 1):
    # Inner loop: prints column numbers from 1 up to current row
    for column in range(1, row + 1):
        print(column, end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs: 1 + 2 + 3 + ... + n = n * (n + 1) / 2 = O(n^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
