"""Pattern 13: Floyd's Triangle (Continuous Number Triangle).

Example Output (for number = 4):
1 
2 3 
4 5 6 
7 8 9 10 

Core Idea:
- Maintain a running counter `to_print` initialized to 1.
- In each row 'row' (0-indexed), print (row + 1) consecutive numbers.
- Increment `to_print` by 1 after printing each number so the
  sequence continues uninterrupted.
"""

# Accept the input from the user
number = int(input("Enter any number: "))

# Counter that maintains consecutive continuous numbers across all rows
to_print = 1

# Outer loop: iterates through rows (0 to number - 1)
for row in range(number):
    # Inner loop: prints (row + 1) numbers for the current row
    for col in range(row + 1):
        print(to_print, end=" ")
        to_print += 1
    # Move to the next line after completing each row
    print()


"""
Time Complexity: O(N^2)
- Outer loop runs N times.
- Total numbers printed = 1 + 2 + 3 + ... + N = N * (N + 1) / 2 = O(N^2).

Space Complexity: O(1)
- Uses constant auxiliary space.
"""
