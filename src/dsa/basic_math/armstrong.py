"""Problem: Check if a Number is an Armstrong Number (Narcissistic Number).

An Armstrong number of order 'k' (where 'k' is the number of digits in N) is
a number that is equal to the sum of its own digits, each raised to the
power of 'k'.

Mathematical Definition:
------------------------
For a k-digit number N = d1 d2 d3 ... dk:
N is an Armstrong number if:
    (d1)^k + (d2)^k + (d3)^k + ... + (dk)^k = N

Example 1 (3-digit Armstrong Number):
    Input:  number = 153
    Digits: 3 (k = 3)
    Sum:    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    Output: "Number is armstrong"

Example 2 (4-digit Armstrong Number):
    Input:  number = 1634
    Digits: 4 (k = 4)
    Sum:    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
    Output: "Number is armstrong"

Example 3 (Non-Armstrong Number):
    Input:  number = 35
    Digits: 2 (k = 2)
    Sum:    3^2 + 5^2 = 9 + 25 = 34 != 35
    Output: "Number is not armstrong"

Algorithm:
----------
1. Count the number of digits (k) in the input integer:
   - If number == 0, count is 1.
   - Otherwise, k = floor(log10(number)) + 1.
2. Maintain an accumulator sum_of initialized to 0, and a copy temp = number.
3. Extract each digit from temp using modulo division (% 10), raise it to
   the power of k, add it to sum_of, and truncate temp using integer division (//= 10).
4. Compare sum_of with the original input number.

Dry Run (for number = 153, number_of_digits = 3):
-------------------------------------------------
| Iteration | temp | remainder (temp % 10) | remainder^k | sum_of (accumulated) |
| :---:     | :---:| :---:                 | :---:       | :---:                |
| Init      | 153  | -                     | -           | 0                    |
| 1         | 153  | 3                     | 3^3 = 27    | 0 + 27 = 27          |
| 2         | 15   | 5                     | 5^3 = 125   | 27 + 125 = 152       |
| 3         | 1    | 1                     | 1^3 = 1     | 152 + 1 = 153        |
| Loop Ends | 0    | -                     | -           | sum_of = 153         |

Comparison: sum_of (153) == number (153) -> True ("Number is armstrong")

Complexity Analysis:
--------------------
- Time Complexity:  O(log10(N)) - Finding digit count takes O(1), and the while
  loop runs once per digit (k = floor(log10(N)) + 1).
- Space Complexity: O(1) - Constant auxiliary memory.
"""

import math

# Accept the integer input from the user
number: int = int(input("Enter any number: "))


# Preserve a copy of the input so the original value is not destroyed during division
temp: int = number

# Determine the number of digits in 'number'
# - Case 0: log10(0) is undefined, so handle 0 explicitly as 1 digit.
# - Positive integers: use the mathematical identity floor(log10(N)) + 1.
if number == 0:
    number_of_digits: int = 1
else:
    number_of_digits: int = math.floor(math.log10(number)) + 1


# Accumulate the sum of each digit raised to the power of number_of_digits
sum_of: int = 0
while temp > 0:
    # Step 1: Extract the rightmost digit
    remainder = temp % 10

    # Step 2: Compute remainder^k and add to the running total
    sum_of += remainder**number_of_digits

    # Step 3: Strip off the rightmost digit
    temp //= 10


# Verify if the accumulated sum equals the original input number
if sum_of == number:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
