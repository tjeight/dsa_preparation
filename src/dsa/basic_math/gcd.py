"""Problem: Find the Greatest Common Divisor (GCD) / Highest Common Factor (HCF).

The Greatest Common Divisor (GCD) of two integers is the largest positive
integer that divides both numbers without leaving a remainder.

Example 1:
    Input:  first_number = 20, second_number = 15
    Output: 5
    Explanation: Factors of 20: 1, 2, 4, 5, 10, 20.
                 Factors of 15: 1, 3, 5, 15.
                 Common factors: 1, 5 -> GCD = 5.

Example 2:
    Input:  first_number = 52, second_number = 10
    Output: 2

Approaches & Mathematical Foundations:
---------------------------------------
1. Brute Force Approach:
   - Iterate from min(a, b) down to 1.
   - The first integer that divides both a and b is the GCD.
   - Time Complexity: O(min(a, b)) -> Too slow for large 64-bit inputs.

2. Euclidean Algorithm by Subtraction:
   - Based on the principle that gcd(a, b) = gcd(a - b, b) where a > b.
   - Repeatedly subtract the smaller number from the larger number until equal.
   - Worst-case Time Complexity: O(max(a, b)) (e.g., gcd(10^9, 1) takes 10^9 steps).

3. Euclidean Algorithm by Modulo Division (Optimal - Implemented Below):
   - Repeated subtraction is equivalent to modulo division:
     gcd(a, b) = gcd(b, a % b)
   - When b becomes 0, the remaining non-zero number 'a' is the GCD.
   - Time Complexity:  O(log(min(a, b))) (By Lamé's Theorem: consecutive Fibonacci
     numbers produce the worst-case inputs, bounded logarithmically).
   - Space Complexity: O(1) auxiliary space.

Important DSA Identity (GCD & LCM Relationship):
------------------------------------------------
- Product Formula: a * b = gcd(a, b) * lcm(a, b)
- Therefore:       lcm(a, b) = (a * b) // gcd(a, b)

Dry Run (for first_number = 52, second_number = 10):
----------------------------------------------------
| Iteration | first_number (a) | second_number (b) | remainder (a % b) | Next (a, b) |
| :---:     | :---:            | :---:             | :---:             | :---:       |
| Init      | 52               | 10                | -                 | -           |
| 1         | 52               | 10                | 52 % 10 = 2       | a = 10, b = 2|
| 2         | 10               | 2                 | 10 % 2 = 0        | a = 2, b = 0 |
| Loop Ends | 2                | 0                 | -                 | GCD = 2     |
"""

# Accept the two integer inputs from the user
first_number: int = int(input("Enter any number: "))
second_number: int = int(input("Enter second number: "))


# This is the euclidean method
# Continue reducing until the second number (divisor) becomes 0
while second_number != 0:
    # Compute the remainder when first_number is divided by second_number
    remainder = first_number % second_number

    # Shift: the divisor becomes the new dividend
    first_number = second_number

    # Shift: the remainder becomes the new divisor
    second_number = remainder


# When second_number becomes 0, first_number holds the GCD

print(first_number)
