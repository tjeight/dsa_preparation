"""Problem: Find All Divisors of a Given Number.

A divisor (or factor) of an integer N is an integer d such that N % d == 0
(i.e., d divides N completely without leaving a remainder).

Example 1:
    Input:  number = 36
    Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]

Example 2:
    Input:  number = 12
    Output: [1, 2, 3, 4, 6, 12]

Example 3 (Prime Number):
    Input:  number = 13
    Output: [1, 13]

Mathematical Foundations & Approaches:
--------------------------------------
1. Brute Force Approach:
   - Iterate from 1 all the way up to N.
   - For every i, if N % i == 0, add i to the divisors list.
   - Time Complexity: O(N) -> Inefficient for large inputs (e.g., N = 10^9 takes
     10^9 operations, exceeding the 1-second execution limit).

2. Optimal Square-Root Pair Approach (Implemented Below):
   - Divisors always appear in symmetrical pairs (conjugate factors):
     If 'i' divides N, then (N // i) must also divide N because:
     i * (N // i) == N.
   - For example, with N = 36:
     1 * 36 = 36
     2 * 18 = 36
     3 * 12 = 36
     4 * 9  = 36
     6 * 6  = 36  <-- Perfect square midpoint (sqrt(36) = 6)
   - Beyond sqrt(N), the pairs simply repeat in reverse (9*4, 12*3, 18*2, 36*1).
   - Therefore, we only need to iterate up to floor(sqrt(N)) (using math.isqrt(N)).
   - For perfect squares (like 6 * 6 = 36), both i and N // i are identical.
     Converting to a set deduplicates these cases cleanly.

Dry Run (for number = 36, isqrt(36) = 6):
-----------------------------------------
| i | 36 % i == 0? | Pair (i, 36 // i) | Divisors List Accumulated |
|---|--------------|-------------------|---------------------------|
| 1 | True         | (1, 36)           | [1, 36]                   |
| 2 | True         | (2, 18)           | [1, 36, 2, 18]            |
| 3 | True         | (3, 12)           | [..., 3, 12]              |
| 4 | True         | (4, 9)            | [..., 4, 9]               |
| 5 | False        | None              | [..., 4, 9]               |
| 6 | True         | (6, 6)            | [..., 6, 6]               |

Deduplication via set(): {1, 2, 3, 4, 6, 9, 12, 18, 36}
Sorted output:           [1, 2, 3, 4, 6, 9, 12, 18, 36]

Complexity Analysis:
--------------------
- Time Complexity:  O(sqrt(N)) - Loop runs at most sqrt(N) times.
  Sorting D divisors takes O(D log D), where D <= 2 * sqrt(N).
  Overall time remains O(sqrt(N)).
- Space Complexity: O(sqrt(N)) - To store the divisors in the list.
"""


# function to get all the divisors
def return_divisors(number: int) -> list:
    """Return an unsorted, unique list of all divisors of 'number' in O(sqrt(N))."""
    import math

    divisors: list = list()

    # Iterate from 1 up to floor(sqrt(number)) inclusive
    for i in range(1, math.isqrt(number) + 1):
        # If 'i' divides 'number' evenly, it is a divisor
        if number % i == 0:
            # 1. Append the smaller factor 'i'
            divisors.append(i)

            # also check for the other pair
            # 2. Append the paired factor 'number // i'
            # (Note: for perfect squares, i == number // i will be deduplicated below)
            divisors.append(number // i)

    # Use set() to eliminate duplicates (e.g., when i == number // i for square roots)
    return list(set(divisors))


def main():
    """Accept user input, compute all divisors, and print them in ascending order."""
    # Accept input integer from the user
    number: int = int(input("Enter any number: "))

    # Obtain all divisors in O(sqrt(N)) time
    divisors: list = return_divisors(number=number)

    # Sort the unique divisors in ascending order for clean display
    print(f"The divisors are {sorted(divisors)}")


# Execute the main driver function
main()
