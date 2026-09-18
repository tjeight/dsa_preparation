"""Pattern 1: Solid Square / Grid of Stars.

Example Output (for n = 4):
****
****
****
****

Core Idea:
- Print a square grid with 'n' rows and 'n' columns.
- For every row, print 'n' stars followed by a newline.
"""

# Accept the input from the user
n = int(input("Enter any number: "))

# Outer loop: controls the number of rows (runs n times from 0 to n-1)
for i in range(n):
    # Inner loop: controls the number of columns (prints n stars in each row)
    for j in range(n):
        print("*", end="")
    # Move to the next line after completing the current row
    print()


"""
Time Complexity: O(n^2)
- Outer loop runs n times.
- Inner loop runs n times for each outer iteration.
- Total operations = n * n = n^2.

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
