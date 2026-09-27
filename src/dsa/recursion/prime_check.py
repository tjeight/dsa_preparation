"""Problem: Check if a Number is Prime Using Recursion (Trial Division).

A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Examples:
    number = 18 -> False (divisible by 2, 3, 6, 9)
    number = 5  -> True  (only divisible by 1 and 5)
    number = 1  -> False (1 is neither prime nor composite)

Recursive Trial Division Strategy (Countdown from N - 1):
----------------------------------------------------------
1. Base Cases:
   - `if number <= 1: return False`
     Numbers <= 1 (negative, 0, 1) are non-prime.
   - `if number == 2: return True`
     2 is the smallest prime number.
   - `if divisor == 1: return True`
     If the divisor counts down to 1 without finding any factors, the number
     has no non-trivial divisors and is therefore PRIME.

2. Divisibility Check (Early Exit):
   - `if number % divisor == 0: return False`
     If any candidate evenly divides 'number', 'number' is COMPOSITE.

3. Recursive Step:
   - `return self.check_prime(number=number, divisor=divisor - 1)`
     Tests the next smaller divisor (countdown toward 1).

Call Stack Lifecycle Trace (for number = 5, divisor = 4):
---------------------------------------------------------
Call 1: check_prime(number=5, divisor=4) -> 5 % 4 != 0, calls check_prime(5, 3)
Call 2: check_prime(number=5, divisor=3) -> 5 % 3 != 0, calls check_prime(5, 2)
Call 3: check_prime(number=5, divisor=2) -> 5 % 2 != 0, calls check_prime(5, 1)
Call 4: check_prime(number=5, divisor=1) -> divisor == 1 (Base Case) -> True!
Unwinds: Returns True all the way back to caller.

Complexity Analysis (Current Implementation):
---------------------------------------------
- Time Complexity:  O(N) - In the worst case (prime numbers), the recursion
  tests N - 2 divisors from N - 1 down to 1.
- Space Complexity: O(N) - Auxiliary call stack space holding N stack frames.
  Note: For N > 1000, Python will raise RecursionError due to the default
  recursion limit (sys.getrecursionlimit()).

DSA Optimization Note (Square Root Bound):
------------------------------------------
Every composite number has a factor <= floor(sqrt(N)).
Instead of checking N - 1 down to 1 in O(N), test from 2 up to sqrt(N) in O(sqrt(N)):
    def check_prime_sqrt(self, number: int, divisor: int = 2) -> bool:
        if number <= 1: return False
        if divisor * divisor > number: return True
        if number % divisor == 0: return False
        return self.check_prime_sqrt(number, divisor + 1)
- Time Complexity:  O(sqrt(N)) (for N = 10^6, only tests up to 1000)
- Space Complexity: O(sqrt(N)) stack frames
"""


class RecursionProblems:
    """Collection of recursive problem-solving algorithms."""

    def check_prime(self, number: int, divisor: int) -> bool:
        """Recursively check primality by testing divisors down to 1."""
        # Base Case 1: Numbers less than or equal to 1 are not prime
        if number <= 1:
            return False

        # Base Case 2: 2 is the only even prime number
        if number == 2:
            return True

        # Base Case 3: If divisor reaches 1 without finding factors, number is prime
        if divisor == 1:
            return True

        # Early Exit: If number is evenly divisible by divisor, it is composite
        if number % divisor == 0:
            return False

        # Recursive Step: Test the next smaller divisor
        return self.check_prime(number=number, divisor=divisor - 1)


# Instantiate the problem solver class
recursion_problems = RecursionProblems()

# Example test number
number = 18

# Start trial division from (number - 1) down to 1
print(recursion_problems.check_prime(number=number, divisor=number - 1))
