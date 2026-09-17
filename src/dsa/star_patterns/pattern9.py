number = int(input("Enter any number: "))

for row in range(1, number + 1):
    # Print leading spaces to center the stars.
    # Spaces decrease by 1 for every row.
    for space in range(number - row):
        print(" ", end="")

    # Print odd number of stars: 1, 3, 5, 7, ...
    # Formula: 2 * row - 1
    for column in range(1, row * 2):
        print("*", end="")

    # Move to the next line after completing each row.
    print()


"""
Time Complexity:
----------------
Outer loop runs N times.

For each row:
    - Spaces: N - row
    - Stars: 2 * row - 1

Total work across all rows is O(N²).

Therefore:
Time Complexity: O(N²)

Space Complexity: O(1)
"""


for row in range(number, 0, -1):
    # Print leading spaces to center the stars.
    # Spaces decrease by 1 for every row.
    for space in range(number - row):
        print(" ", end="")

    # Print odd number of stars: 1, 3, 5, 7, ...
    # Formula: 2 * row - 1
    for column in range(1, row * 2):
        print("*", end="")

    # Move to the next line after completing each row.
    print()


"""
Time Complexity:
----------------
Outer loop runs N times.

For each row:
    - Spaces: N - row
    - Stars: 2 * row - 1

Total work across all rows is O(N²).

Therefore:
Time Complexity: O(N²)

Space Complexity: O(1)
"""
