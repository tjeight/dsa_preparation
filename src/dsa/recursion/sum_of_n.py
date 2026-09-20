"""Problem: Sum of First N Natural Numbers Using Functional Recursion.

Given an integer 'number' (N), compute the sum of all integers from 1 up to N:
    Sum(N) = 1 + 2 + 3 + ... + N

Example 1:
    Input:  number = 4
    Output: 10
    Explanation: 1 + 2 + 3 + 4 = 10

Example 2:
    Input:  number = 5
    Output: 15
    Explanation: 1 + 2 + 3 + 4 + 5 = 15

Two Recursive Paradigms for Sum:
--------------------------------
1. Functional Recursion (Implemented Below):
   - The recursive function computes and returns the answer to its caller.
   - Recurrence Relation: Sum(N) = N + Sum(N - 1)
   - Base Case: Sum(0) = 0
   - The actual addition operations occur on the WAY BACK (unwinding/return phase).

2. Parameterized Recursion (Alternative):
   - Accumulate the running sum inside an extra parameter passed downward:
     def solve(i, current_sum):
         if i < 1:
             print(current_sum)
             return
         solve(i - 1, current_sum + i)

3. Mathematical Formula (Optimal O(1) in production):
   - Sum = N * (N + 1) // 2

Call Stack Lifecycle Trace (for number = 4):
--------------------------------------------
Descent Phase (Pushing frames):
| sum_of_n(number=0) | -> Base Case reached (returns 0)
| sum_of_n(number=1) | -> Waiting for sum_of_n(0) to compute 1 + sum_of_n(0)
| sum_of_n(number=2) | -> Waiting for sum_of_n(1) to compute 2 + sum_of_n(1)
| sum_of_n(number=3) | -> Waiting for sum_of_n(2) to compute 3 + sum_of_n(2)
| sum_of_n(number=4) | -> Waiting for sum_of_n(3) to compute 4 + sum_of_n(3)
+--------------------+
Unwinding Phase (Evaluating returns):
- sum_of_n(0) returns 0
- sum_of_n(1) returns 1 + 0 = 1
- sum_of_n(2) returns 2 + 1 = 3
- sum_of_n(3) returns 3 + 3 = 6
- sum_of_n(4) returns 4 + 6 = 10 -> Result printed in main()

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N + 1 recursive calls are made.
- Space Complexity: O(N) - Auxiliary call stack space for N concurrent stack frames.
"""


def sum_of_n(number: int):
    """Compute sum of integers from 1 to 'number' via functional recursion."""
    # Base Case: When number reaches 0, the additive identity 0 is returned
    if number == 0:
        return 0

    # Recursive Step: Current number + sum of the remaining (number - 1) elements
    return number + sum_of_n(number=number - 1)


def main():
    """Accept user input, compute recursive sum, and display result."""
    number: int = int(input("Enter number: "))

    # Output the accumulated recursive sum
    print(sum_of_n(number=number))


# Execute driver function
main()
