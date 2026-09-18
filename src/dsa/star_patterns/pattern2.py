"""Pattern 2: Right-Angled Triangle of Stars.

Example Output (for n = 4):
*
**
***
****

Core Idea:
- Number of rows = n.
- In row 0 (0-indexed), print 1 star.
- In row 1, print 2 stars.
- In row 'row', print (row + 1) stars.
"""

# Accept the input from the user
n = int(input("Enter any number: "))


# Trick find the rows and columns.
# The iterations are simple make that much rows when there are that much columns

# Outer loop: iterates through rows from 0 to n-1
for row in range(n):
    # Inner loop: prints (row + 1) stars for the current row
    for column in range(row + 1):
        print("*", end="")
    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs (row + 1) times: 1 + 2 + 3 + ... + n = n * (n + 1) / 2 = O(n^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
