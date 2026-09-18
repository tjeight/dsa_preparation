"""Pattern 12: Number Crown / Valley Pattern.

Example Output (for number = 4):
1      1
12    21
123  321
12344321

Core Idea:
Each row (1-indexed, row from 1 to number) contains 3 segments:
1. Increasing numbers: 1 to row.
2. Middle spaces: 2 * (number - row) spaces.
3. Decreasing numbers: row down to 1 (mirror symmetry).
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: controls row index from 1 to number
for row in range(1, number + 1):
    # 1. Left wing: print numbers in ascending order from 1 to row
    for col in range(1, row + 1):
        print(col, end="")

    # 2. Middle gap: print spaces decreasing as row increases: 2 * (number - row)
    for space in range(2 * (number - row)):
        print(" ", end="")

    # 3. Right wing: print numbers in descending order from row down to 1
    for reverse in range(row, 0, -1):
        print(reverse, end="")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- In each row: row (left) + 2*(N - row) (spaces) + row (right) = 2*N total characters.
- Total operations = N * 2*N = 2*N^2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
