"""Problem: Reverse an Integer (Digit Reversal).

Given an integer 'number', reverse its digits using mathematical operations
(without converting to string).

Example 1:
    Input:  number = 1234
    Output: 4321

Example 2:
    Input:  number = 7789
    Output: 9877

Example 3:
    Input:  number = 10400
    Output: 401  (trailing zeroes are dropped in integer representation)

Algorithm & Mathematical Principle:
-----------------------------------
1. Extract the last digit of 'number' using modulo arithmetic:
   remainder = number % 10
2. Shift the existing reversed number to the left by one decimal place
   and add the newly extracted digit:
   reverse = reverse * 10 + remainder
3. Strip off the last digit from 'number' using integer division:
   number //= 10
4. Repeat steps 1-3 until number becomes 0.

Dry Run (for number = 7789):
----------------------------
| Iteration | remainder (num % 10) | reverse (rev * 10 + rem) | number (num // 10) |
| :---:     | :---:                | :---:                    | :---:              |
| Init      | -                    | 0                        | 7789               |
| 1         | 9                    | 0 * 10 + 9 = 9           | 778                |
| 2         | 8                    | 9 * 10 + 8 = 98          | 77                 |
| 3         | 7                    | 98 * 10 + 7 = 987        | 7                  |
| 4         | 7                    | 987 * 10 + 7 = 9877      | 0 (Loop ends)      |

Complexity Analysis:
--------------------
- Time Complexity:  O(log10(N)) - The loop runs once for every digit in N.
- Space Complexity: O(1) - Uses constant extra space (only scalar variables).

Interview Notes (LeetCode 7 - Reverse Integer):
-----------------------------------------------
- In Python, integers have arbitrary precision, so overflow does not crash.
- In languages with fixed 32-bit integers (C++/Java), check for overflow
  against INT_MAX (2^31 - 1) and INT_MIN (-2^31) before multiplying by 10.
- For negative numbers, record the sign, work with abs(number), and reapply.
"""

# Accept the integer input from the user
number: int = int(input("Enter a number: "))

# Preserve a copy of the initial input for reference or display
original_number = number

# Display the initial number before starting reversal
print("Original number", original_number)

# Variable to accumulate the reversed number, initialized to 0
reverse = 0

# Continue processing until all digits of 'number' have been consumed
while number > 0:
    # Step 1: Extract the rightmost (least significant) digit
    remainder = number % 10

    # Step 2: Push existing digits left by multiplying by 10, then append remainder
    reverse = reverse * 10 + remainder

    # Step 3: Remove the rightmost digit using integer floor division
    number //= 10

# Display the final reversed number
print("Reverse number", reverse)
