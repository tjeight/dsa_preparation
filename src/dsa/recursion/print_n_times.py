"""Problem: Print a Name / Message N Times Using Recursion.

Recursion is a programming technique where a function calls itself to solve
smaller instances of the same problem until a base condition is reached.

The 3 Essential Pillars of Any Recursive Function:
--------------------------------------------------
1. Base Case:
   The terminating condition that halts further recursive calls.
   Here: `if number == 0: return`
   Without a base case, the function calls itself indefinitely until Python
   raises: `RecursionError: maximum recursion depth exceeded`.

2. Work / Processing in Current Call Frame:
   The action performed at the current state.
   Here: `print("Tejas")`

3. Recursive Call (State Transition):
   Invoking the function with a smaller subproblem moving toward the base case.
   Here: `print_n_times(number - 1)`

Recursion Tree / Call Stack Trace (for number = 3):
---------------------------------------------------
Call Stack (Push phase):
| print_n_times(0) |  <-- Hits Base Case (number == 0), returns None
| print_n_times(1) |  <-- Prints "Tejas", calls print_n_times(0)
| print_n_times(2) |  <-- Prints "Tejas", calls print_n_times(1)
| print_n_times(3) |  <-- Prints "Tejas", calls print_n_times(2)
+------------------+
Unwinding (Pop phase):
Each frame returns None up the call stack until main() resumes.

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N + 1 recursive calls are executed.
- Space Complexity: O(N) - Auxiliary stack space used by N recursive frames
  on the call stack simultaneously before reaching the base case.
"""


def print_n_times(number: int):
    """Recursively print 'Tejas' 'number' times."""
    # Base Case: Stop recursion when the counter reaches 0
    if number == 0:
        return

    # Work: Print the name for the current call frame
    print("Tejas")

    # Recursive Call: Transition to a smaller subproblem (number - 1)
    return print_n_times(number - 1)


def main():
    """Accept user input and initiate recursive execution."""
    number: int = int(input("Enter any number: "))

    print_n_times(number=number)


# Execute driver function
main()
