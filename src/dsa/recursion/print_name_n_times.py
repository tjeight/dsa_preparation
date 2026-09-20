"""Problem: Print a Dynamic Name N Times Using Parameterized Recursion.

This script demonstrates parameterized recursion where additional state
('name') is passed alongside the recursive reduction counter ('number').

The 3 Pillars of Recursion in this Implementation:
--------------------------------------------------
1. Base Case:
   Terminates recursion when the count reaches zero:
   `if number == 0: return`
   Prevents infinite recursion and call stack exhaustion.

2. Work / Processing:
   Outputs the user-provided string 'name' in the current execution frame:
   `print(name)`

3. Recursive Call (Subproblem Reduction):
   Calls `print_name_n_times` with the reduced counter `number - 1` while
   propagating the constant parameter `name`:
   `return print_name_n_times(number=number - 1, name=name)`

Call Stack Lifecycle Trace (for number = 3, name = "Alice"):
------------------------------------------------------------
Push Phase (Function Calls):
| print_name_n_times(number=0, name="Alice") |  <-- Base Case hit (returns None)
| print_name_n_times(number=1, name="Alice") |  <-- Prints "Alice"
| print_name_n_times(number=2, name="Alice") |  <-- Prints "Alice"
| print_name_n_times(number=3, name="Alice") |  <-- Prints "Alice"
+--------------------------------------------+
Pop Phase (Unwinding):
Each recursive frame returns None back to its caller up to main().

Complexity Analysis:
--------------------
- Time Complexity:  O(N) - Exactly N + 1 recursive calls are invoked.
- Space Complexity: O(N) - Auxiliary call stack space for N concurrent stack frames.
"""


def print_name_n_times(number: int, name: str):
    """Recursively print 'name' for 'number' iterations."""
    # Base Case: When the counter reaches 0, stop and return
    if number == 0:
        return

    # Work: Print the string provided by the user
    print(name)

    # Recursive Step: Decrement 'number' by 1 and pass 'name' forward
    return print_name_n_times(number=number - 1, name=name)


def main():
    """Prompt user for repetition count and name, then initiate recursion."""
    number: int = int(input("Enter  number : "))
    name: str = input("Enter your name: ")

    # Invoke the recursive function with keyword arguments
    print_name_n_times(name=name, number=number)


# Execute the main driver function
main()
