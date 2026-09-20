"""Problem: Check if a Number is Prime (Trial Division).

A prime number is a natural number strictly greater than 1 that has exactly
two distinct positive divisors: 1 and itself.
Numbers greater than 1 that are not prime are called composite numbers.

Example 1:
    Input:  number = 11
    Output: "Number is prime"
    Explanation: Factors of 11 are only 1 and 11.

Example 2:
    Input:  number = 35
    Output: "Number is composite"
    Explanation: 35 has factors 1, 5, 7, 35 -> divisible by 5 and 7.

Example 3:
    Input:  number = 2
    Output: "Number is prime"
    Explanation: 2 is the smallest and only even prime number.

Mathematical Principle & Approaches:
-------------------------------------
1. Brute Force Approach:
   - Check divisibility by all integers from 2 to N - 1.
   - Time Complexity: O(N) -> Infeasible for large numbers (e.g., N = 10^9).

2. Optimal Square-Root Trial Division (Implemented Below):
   - If N is composite, it must have at least one factor pair (a, b) such that
     a * b = N.
   - If both a and b were strictly greater than sqrt(N), then:
     a * b > sqrt(N) * sqrt(N) = N, which is a contradiction.
   - Therefore, at least one factor MUST be <= sqrt(N).
   - Thus, if no integer in the range [2, floor(sqrt(N))] divides N,
     then N has no non-trivial factors and must be PRIME!
   - Time Complexity:  O(sqrt(N)) (for N = 10^9, checks at most 31,622 numbers).
   - Space Complexity: O(1) auxiliary memory.

Dry Run (for number = 17, isqrt(17) = 4):
-----------------------------------------
| i | 17 % i == 0? | Action / Decision                        |
|---|--------------|------------------------------------------|
| 2 | False        | 17 % 2 != 0 -> Continue                  |
| 3 | False        | 17 % 3 != 0 -> Continue                  |
| 4 | False        | 17 % 4 != 0 -> Continue                  |
| - | -            | Loop finishes: no divisor found -> PRIME |

Dry Run (for number = 35, isqrt(35) = 5):
-----------------------------------------
| i | 35 % i == 0? | Action / Decision                        |
|---|--------------|------------------------------------------|
| 2 | False        | 35 % 2 != 0 -> Continue                  |
| 3 | False        | 35 % 3 != 0 -> Continue                  |
| 4 | False        | 35 % 4 != 0 -> Continue                  |
| 5 | True         | 35 % 5 == 0 -> Early exit: COMPOSITE     |

Complexity Analysis:
--------------------
- Time Complexity:  O(sqrt(N)) - Loop tests divisors up to floor(sqrt(N)).
- Space Complexity: O(1) - Constant auxiliary memory.
"""


def check_prime(number: int) -> bool:
    """Check whether 'number' is a prime number in O(sqrt(N)) time."""
    # Base Case: 2 is the smallest prime and the only even prime
    if number == 2:
        return True

    import math

    # Test all possible divisor candidates from 2 up to floor(sqrt(number))
    for i in range(2, math.isqrt(number) + 1):
        # If any integer divides 'number' evenly, it is composite
        if number % i == 0:
            return False

    # If no factor was found up to sqrt(number), the number is prime
    return True


def main():
    """Accept input number, validate bounds, and display primality result."""
    # Accept user input integer
    number: int = int(input("Enter any number: "))

    # 0, 1, and negative numbers are neither prime nor composite
    if number < 2:
        print("Number should be greater than 0 or 1")
        return

    # Check primality via trial division up to sqrt(number)
    is_prime = check_prime(number=number)

    # Print the final result
    if is_prime:
        print("Number is prime")
    else:
        print("Number is composite")


# Execute the driver function
main()
