"""Pattern 18: Inverted Alphabet Triangle from N-th Letter.

Example Output (for number = 5):
E 
D E 
C D E 
B C D E 
A B C D E 

Core Idea:
- The base letter is the N-th uppercase letter (e.g., for N=5, 'E').
- In row 1: print 'E'.
- In row 2: start at 'D' and end at 'E'.
- In row 'row': start at chr(65 + number - row) and count up to chr(65 + number - 1).
- The inner loop iterates col from row down to 1,
  computing character `chr(65 + (number - col))`.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Outer loop: controls row count from 1 to number
for row in range(1, number + 1):
    # Inner loop: col counts down from row to 1,
    # producing ascending characters starting from (number - row)
    for col in range(row, 0, -1):
        print(chr(65 + (number - col)), end=" ")

    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Inner loop runs: 1 + 2 + 3 + ... + N = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
