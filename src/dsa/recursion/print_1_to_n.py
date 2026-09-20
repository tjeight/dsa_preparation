"""Problem: Print Numbers from 1 to N Using Recursion.

Given an integer 'number', print all integers from 1 up to 'number' in
strictly ascending order using recursive function calls.

Example:
    Input:  number = 5
    Output:
    1
    2
    3
    4
    5

Core Recursive Concepts:
------------------------
1. Base Case:
   `if start > number: return`
   Halts recursion when the counter 'start' surpasses the upper limit 'number'.

2. Work / Processing (Forward Phase):
   `print(start)`
   Prints the current value of 'start' before descending into the subproblem.

3. Recursive Call (State Transition):
   `print_1_to_n(start + 1, number)`
   Advances 'start' forward by +1 toward 'number'.

Call Stack Trace (for number = 3):
----------------------------------
Call Stack (Forward / Descent Phase):
| print_1_to_n(start=1, number=3) | -> Prints 1, calls print_1_to_n(2, 3)
| print_1_to_n(start=2, number=3) | -> Prints 2, calls print_1_to_n(3, 3)
| print_1_to_n(start=3, number=3) | -> Prints 3, calls print_1_to_n(4, 3)
| print_1_to_n(start=4, number=3) | -> Base Case hit (4 > 3), returns None
+---------------------------------+
Unwinding (Return Phase):
All stack frames return None up the call stack back to main().

Interview Insight (Forward Recursion vs. Backtracking):
-------------------------------------------------------
- Forward Recursion (Implemented here): Prints 'start' during the PUSH phase
  (before the recursive call).
- Backtracking Approach (Alternative): If parameters cannot be incremented,
  you can recurse first and print during the POP phase (unwinding):
      def print_1_to_n_backtrack(i):
          if i < 1: return
          print_1_to_n_backtrack(i - 1)  # Recurse down to 1
          print(i)                        # Print on the way back up

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N + 1 recursive calls are executed.
- Space Complexity: O(N) - Auxiliary call stack space holding N stack frames.
"""


def print_1_to_n(start: int, number: int):
    """Recursively print integers from 'start' up to 'number'."""
    # Base Case: Terminate when the current number exceeds the upper limit
    if start > number:
        return

    # Work: Print the current integer in ascending order
    print(start)

    # Recursive Call: Move to the next integer (start + 1)
    print_1_to_n(start + 1, number)


def main():
    """Prompt user for N and initiate recursive printing from 1."""
    number = int(input("Enter number: "))

    # Start recursion at 1 up to 'number'
    print_1_to_n(1, number)


# Execute driver function
main()
