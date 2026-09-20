"""Problem: Check if a Number is a Palindrome (LeetCode 9).

A palindrome number is an integer that reads the same forward and backward.
For example, 121 is a palindrome, while 123 is not.

Example 1:
    Input:  number = 121
    Output: "The number is a palindrome."
    Explanation: Reading from left to right: 121. From right to left: 121.

Example 2:
    Input:  number = -121
    Output: "The number is not a palindrome."
    Explanation: From left to right: -121. From right to left: 121-.
                 All negative numbers are non-palindromic due to the minus sign.

Example 3:
    Input:  number = 10
    Output: "The number is not a palindrome."
    Explanation: Reads 01 from right to left, which is not equal to 10.

Algorithm & Mathematical Principle:
-----------------------------------
1. Store a copy of the input: original_number = number.
2. Reverse the digits mathematically:
   - Extract the rightmost digit: remainder = number % 10
   - Append to reversed accumulator: reverse = reverse * 10 + remainder
   - Remove the rightmost digit: number //= 10
   - Repeat until number == 0.
3. Compare the reconstructed reversed number with original_number:
   - If reverse == original_number -> Palindrome.
   - Otherwise -> Not a palindrome.

Dry Run (for number = 121):
---------------------------
| Iteration | remainder (num % 10) | reverse (rev * 10 + rem) | number (num // 10) |
| :---:     | :---:                | :---:                    | :---:              |
| Init      | -                    | 0                        | 121                |
| 1         | 1                    | 0 * 10 + 1 = 1           | 12                 |
| 2         | 2                    | 1 * 10 + 2 = 12          | 1                  |
| 3         | 1                    | 12 * 10 + 1 = 121        | 0 (Loop ends)      |

Comparison: reverse (121) == original_number (121) -> True (Palindrome)

Complexity Analysis:
--------------------
- Time Complexity:  O(log10(N)) - The loop runs once for each digit in N.
- Space Complexity: O(1) - Uses constant extra space (only scalar variables).

Key Edge Cases to Consider:
---------------------------
1. Negative Numbers (number < 0): Always False due to leading '-'.
2. Numbers ending in 0 (e.g., 10, 100): Cannot be palindromes (except 0 itself)
   because the reversed number cannot have a leading zero.
3. Single-digit numbers (0 to 9): Always palindromes.
4. Optimal LeetCode Approach: You can stop reversing at the halfway point
   (when number <= reverse) to check without reversing the full number.
"""

# Accept the integer input from the user
number: int = int(input("Enter a number: "))

# Preserve a copy of the initial input to compare against the reversed result
original_number = number

# Display the initial number before starting the reversal
print("Original number", original_number)

# Variable to accumulate the reversed number, initialized to 0
reverse = 0

# Extract and reverse digits one by one until number becomes 0
while number > 0:
    # Step 1: Extract the rightmost (least significant) digit
    remainder = number % 10

    # Step 2: Shift existing reversed digits left by * 10 and add the remainder
    reverse = reverse * 10 + remainder

    # Step 3: Remove the rightmost digit using integer floor division
    number //= 10

# Check whether the reversed value matches the original input
if reverse == original_number:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
