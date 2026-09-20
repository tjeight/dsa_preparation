"""Problem: Print Numbers from N down to 1 Using Recursion.

Given an integer 'number', print all integers from 'number' down to 1 in
strictly descending order using recursive function calls.

Example:
    Input:  number = 5
    Output:
    5
    4
    3
    2
    1

Core Recursive Concepts:
------------------------
1. Base Case:
   `if start > number: return`
   Halts recursion when 'number' drops below the lower boundary 'start' (1).

2. Work / Processing:
   `print(number)`
   Prints the current value of 'number' before decrementing.

3. Recursive Call (Subproblem Reduction):
   `print_n_to_1(1, number - 1)`
   Reduces 'number' by 1 on each step, approaching the lower bound 'start'.

Call Stack Trace (for number = 3):
----------------------------------
Call Stack (Forward / Descent Phase):
| print_n_to_1(start=1, number=3) | -> Prints 3, calls print_n_to_1(1, 2)
| print_n_to_1(start=1, number=2) | -> Prints 2, calls print_n_to_1(1, 1)
| print_n_to_1(start=1, number=1) | -> Prints 1, calls print_n_to_1(1, 0)
| print_n_to_1(start=1, number=0) | -> Base Case hit (1 > 0), returns None
+---------------------------------+
Unwinding (Return Phase):
Each stack frame returns None up the call stack back to main().

Interview Insight (Forward Recursion vs. Backtracking):
-------------------------------------------------------
- Forward Recursion (Implemented here): Prints 'number' during the PUSH phase
  (before descending into the recursive call).
- Backtracking Approach (Alternative): If parameters are incremented instead:
      def print_n_to_1_backtrack(i, n):
          if i > n: return
          print_n_to_1_backtrack(i + 1, n)  # Recurse up to N
          print(i)                          # Print on the way back down (N..1)

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N + 1 recursive calls are executed.
- Space Complexity: O(N) - Auxiliary call stack space holding N stack frames.
"""


def print_n_to_1(start: int, number: int):
    """Recursively print integers from 'number' down to 'start'."""
    # Base Case: Terminate when 'number' drops below 'start' (e.g., number == 0)
    if start > number:
        return

    # Work: Print the current integer in descending order
    print(number)

    # Recursive Step: Decrement 'number' by 1 toward the base condition
    print_n_to_1(1, number - 1)


def main():
    """Prompt user for N and initiate recursive printing down to 1."""
    number = int(input("Enter number: "))

    # Start recursion from N down to 1
    print_n_to_1(1, number)


# Execute driver function
main()
