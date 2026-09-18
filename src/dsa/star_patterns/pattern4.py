"""Pattern 4: Right-Angled Triangle with Repeated Row Numbers.

Example Output (for number = 4):
1
22
333
4444

Core Idea:
- Outer loop runs from 1 to number (1-indexed).
- In each row 'row', print the row number repeated 'row' times.
- The value printed is constant for that row (the row index).
"""

# Accept the input from the user
number = int(input("Enter any number: "))


# Trick find the rows and columns.
# The iterations are simple make that much rows when there are that much columns

# Outer loop: controls row index from 1 to number
for row in range(1, number + 1):
    # Inner loop: repeats the current row number 'row' times
    for column in range(1, row + 1):
        print(row, end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs: 1 + 2 + 3 + ... + n = n * (n + 1) / 2 = O(n^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
