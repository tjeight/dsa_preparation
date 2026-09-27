"""Problem: Sum of Digits of a Number Using Functional Recursion.

Given a non-negative integer, compute the sum of its individual decimal digits
using recursion.

Examples:
    number = 101  -> 1 + 0 + 1 = 2
    number = 4321 -> 4 + 3 + 2 + 1 = 10
    number = 9    -> 9
    number = 0    -> 0

Mathematical & Recursive Strategy:
----------------------------------
1. Decimal Decomposition:
   - Last digit: `number % 10` (extracts least significant digit).
   - Remaining digits: `number // 10` (truncates the rightmost digit).

2. Base Case:
   `if number == 0: return 0`
   - When all digits have been extracted, the number reduces to 0.
   - 0 is the additive identity (adding 0 does not change the total sum).
   - Returns 0 to terminate recursion and start unwinding the stack.

3. Recursive Step (Functional Accumulation):
   `return number % 10 + self.sum_of_digits(number=number // 10)`
   - Computes: (Current Last Digit) + (Sum of Digits of Remaining Number).
   - Each stack frame waits for its child call to return, then adds its own
     last digit during the unwinding phase.

Call Stack Lifecycle Trace (for number = 101):
----------------------------------------------
Call 1: sum_of_digits(101)
- 101 != 0
- Last digit = 101 % 10 = 1
- Suspends: 1 + sum_of_digits(10)

Call 2: sum_of_digits(10)
- 10 != 0
- Last digit = 10 % 10 = 0
- Suspends: 0 + sum_of_digits(1)

Call 3: sum_of_digits(1)
- 1 != 0
- Last digit = 1 % 10 = 1
- Suspends: 1 + sum_of_digits(0)

Call 4: sum_of_digits(0)
- number == 0 -> BASE CASE REACHED!
- Returns 0 immediately.

Unwinding Phase:
- Call 3 resumes: 1 + 0 = 1 -> returns 1
- Call 2 resumes: 0 + 1 = 1 -> returns 1
- Call 1 resumes: 1 + 1 = 2 -> returns 2
Final Output: 2

Complexity Analysis:
--------------------
- Time Complexity:  O(log10(N)) or O(D)
  - An integer N has D = floor(log10(N)) + 1 digits.
  - In each step, the number is divided by 10 (number // 10).
  - Number of recursive calls is equal to the number of digits D.
  - Each call performs O(1) arithmetic operations (%, //, +).
  - Total Time: O(log10(N)) logarithmic time.
- Space Complexity: O(log10(N)) or O(D)
  - Requires D + 1 active stack frames on the Python call stack.

DSA Variations & Related Patterns:
----------------------------------
1. Parameterized (Tail-Recursive) Form:
   Passing an accumulator `total` allows accumulating on the way down:
       def sum_digits_tail(self, n: int, total: int = 0) -> int:
           if n == 0:
               return total
           return self.sum_digits_tail(n // 10, total + (n % 10))
2. Digital Root (LeetCode 258 - Add Digits):
   Repeatedly summing digits until a single digit remains can be computed in
   O(1) time using modulo 9 arithmetic (congruence formula):
       digital_root = 0 if n == 0 else 1 + (n - 1) % 9
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def sum_of_digits(self, number: int) -> int:
        """Recursively calculate the sum of decimal digits of a number."""
        # Base Case: When all digits are extracted, number becomes 0
        if number == 0:
            return 0

        # Functional Step: Add last digit to the sum of the remaining digits
        return number % 10 + self.sum_of_digits(number=number // 10)


# Instantiate the problem solver class
recursion_problems = RecursionProblems()


# Test with sample input number 101 (1 + 0 + 1 = 2)
print(recursion_problems.sum_of_digits(101))
