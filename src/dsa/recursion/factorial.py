"""Problem: Factorial of a Number Using Functional Recursion.

The factorial of a non-negative integer N (denoted as N!) is the product
of all positive integers less than or equal to N:
    N! = N * (N - 1) * (N - 2) * ... * 2 * 1
By mathematical convention:
    0! = 1
    1! = 1

Example 1:
    Input:  number = 4
    Output: 24
    Explanation: 4! = 4 * 3 * 2 * 1 = 24

Example 2:
    Input:  number = 5
    Output: 120
    Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120

Example 3:
    Input:  number = 0
    Output: 1

Recurrence Relation & Logic:
----------------------------
1. Base Case:
   `if number == 0 or number == 1: return 1`
   Halts recursion at the multiplicative identity (1).

2. Recursive Step (Functional):
   `return number * factorial(number - 1)`
   Multiplies the current integer by the factorial of the subproblem (N - 1).
   The actual multiplication occurs during the call stack UNWINDING phase.

Call Stack Lifecycle Trace (for number = 4):
--------------------------------------------
Descent Phase (Pushing stack frames):
| factorial(number=1) | -> Base Case reached (returns 1)
| factorial(number=2) | -> Waiting for factorial(1) to evaluate 2 * factorial(1)
| factorial(number=3) | -> Waiting for factorial(2) to evaluate 3 * factorial(2)
| factorial(number=4) | -> Waiting for factorial(3) to evaluate 4 * factorial(3)
+---------------------+
Unwinding Phase (Evaluating multiplication returns):
- factorial(1) returns 1
- factorial(2) returns 2 * 1 = 2
- factorial(3) returns 3 * 2 = 6
- factorial(4) returns 4 * 6 = 24 -> Output printed in main()

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N recursive function calls are invoked.
- Space Complexity: O(N) - Auxiliary call stack space for N concurrent stack frames.

Note on Python Arbitrary Precision:
-----------------------------------
Unlike languages with fixed 32-bit/64-bit integer limits (C++/Java), Python 3
automatically handles arbitrarily large integers, preventing integer overflow
even for large factorials (e.g., 50!).
"""


def factorial(number: int):
    """Compute N! recursively using functional decomposition."""
    # Base Case: Factorial of 0 and 1 is 1 (multiplicative identity)
    if number == 0 or number == 1:
        return 1

    # Recursive Step: Multiply current number by factorial of (number - 1)
    return number * factorial(number=number - 1)


def main():
    """Prompt user for N, compute factorial recursively, and print result."""
    number: int = int(input("Enter number: "))

    # Output the evaluated factorial
    print(factorial(number=number))


# Execute the driver function
main()
