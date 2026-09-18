"""Pattern 6: Inverted Right-Angled Triangle of Stars.

Example Output (for number = 4):
****
***
**
*

Core Idea:
- Outer loop runs 'number' times (row from 0 to number - 1).
- In each row, stars decrease by 1: (number - row) stars are printed.
- Implemented using range(number, row, -1).
"""

# Accept the input from the user
number = int(input("Enter any number: "))


# Trick find the rows and columns.
# The iterations are simple make that much rows when there are that much columns

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: counts down from number to row + 1, printing (number - row) stars
    for column in range(number, row, -1):
        print("*", end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs (n - row) times: n + (n - 1) + ... + 1 = n * (n + 1) / 2 = O(n^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
