"""Problem: Count the Number of Digits in an Integer.

Given an integer 'number', determine the total number of digits it contains.

Example 1:
    Input:  number = 7789
    Output: 4

Example 2:
    Input:  number = 1
    Output: 1

Approaches Implemented:
-----------------------
1. Iterative Division (Brute Force / Standard):
   - Repeatedly divide the number by 10 using integer division (//= 10) to
     strip the last digit until the number becomes 0.
   - Increment a counter for every division.
   - Time Complexity:  O(log10(N)) - number of iterations equals number of digits.
   - Space Complexity: O(1) - uses only a single counter variable.

2. Logarithmic Formula (Optimal Mathematical Approach):
   - By definition of base-10 logarithms:
     floor(log10(N)) gives the highest power of 10 that fits into N.
   - Adding 1 yields the exact count of digits:
     count = floor(log10(N)) + 1
   - Example: N = 7789 -> log10(7789) ≈ 3.8915 -> floor(3.8915) = 3 -> 3 + 1 = 4.
   - Example: N = 100  -> log10(100)  = 2.0     -> floor(2.0)    = 2 -> 2 + 1 = 3.
   - Time Complexity:  O(1) - executed in constant time via CPU FPU.
   - Space Complexity: O(1) - no extra memory allocated.

Note on Edge Cases:
-------------------
- Zero (N = 0): Contains 1 digit. (Note: math.log10(0) is undefined / ValueError).
- Negative Numbers: Take abs(number) before counting digits.
"""

import math

# Accept the integer input from the user
number: int = int(input("Enter a number: "))

# ============================================================================
# APPROACH 1: Iterative Division by 10
# ============================================================================
# Make a copy of 'number' so the original input value remains preserved
new_number = number

# Counter to keep track of the number of digits
count = 0

# Loop until all digits have been truncated (new_number reduced to 0)
while new_number > 0:
    # Integer division by 10 strips off the least significant (last) digit
    # e.g., 7789 // 10 = 778 -> 778 // 10 = 77 -> 77 // 10 = 7 -> 7 // 10 = 0
    new_number //= 10

    # Increment digit count for each digit removed
    count += 1

# Output the result obtained from Approach 1
print(count)


# ============================================================================
# APPROACH 2: Optimal Mathematical Formula (Log10)
# ============================================================================
# Formula: floor(log10(number)) + 1
# - math.log10(number): calculates the logarithm of 'number' to base 10.
# - math.floor(...): rounds down to the nearest integer.
# - + 1: offsets the 0-indexed power to represent the count of digits.
# - Runs in O(1) time complexity.
new_count = math.floor(math.log10(number)) + 1

# Output the result obtained from Approach 2
print(new_count)
