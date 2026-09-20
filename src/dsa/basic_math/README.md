# Basic Mathematics for DSA & Coding Interviews

This directory contains foundational number-theory and mathematical algorithms commonly tested in technical interviews (such as Striver's A2Z DSA Sheet and LeetCode).

---

## 📂 Catalog of Problems

| Problem | Script | Core Mathematical Concept | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :---: | :---: |
| **Count Digits** | [`count_digits.py`](count_digits.py) | $\lfloor \log_{10}(N) \rfloor + 1$ or iterative `//= 10` | $O(1)$ (log) / $O(\log_{10} N)$ | $O(1)$ |
| **Reverse an Integer** | [`reverse_number.py`](reverse_number.py) | Modulo `% 10` and `rev * 10 + rem` | $O(\log_{10} N)$ | $O(1)$ |
| **Palindrome Number** | [`palindrome_number.py`](palindrome_number.py) | Full / half integer reversal comparison | $O(\log_{10} N)$ | $O(1)$ |
| **GCD / HCF** | [`gcd.py`](gcd.py) | Euclidean Algorithm: $\gcd(b, a \pmod b)$ | $O(\log(\min(a, b)))$ | $O(1)$ |
| **Armstrong Number** | [`armstrong.py`](armstrong.py) | Sum of digits raised to power of $k$: $\sum d_i^k = N$ | $O(\log_{10} N)$ | $O(1)$ |
| **All Divisors** | [`all_divisors.py`](all_divisors.py) | Conjugate factor pairs up to $\sqrt{N}$ | $O(\sqrt{N})$ | $O(\sqrt{N})$ |
| **Prime Check** | [`prime.py`](prime.py) | Trial division up to $\lfloor\sqrt{N}\rfloor$ | $O(\sqrt{N})$ | $O(1)$ |

---

## 🧠 Detailed Problem Breakdowns

### 1. Count Digits
- **File**: [`count_digits.py`](count_digits.py)
- **Problem**: Count the number of decimal digits in integer $N$.
- **Optimal Formula**:
  $$\text{count} = \lfloor \log_{10}(N) \rfloor + 1$$
  - Example: For $N = 7789$, $\log_{10}(7789) \approx 3.891 \implies \lfloor 3.891 \rfloor + 1 = 4$.
  - Special Case: $N = 0 \implies \text{count} = 1$ (since $\log_{10}(0)$ is undefined).
- **Iterative Approach**:
  Continuously divide by 10 (`number //= 10`) until 0, incrementing a counter. Runs in $O(\log_{10} N)$ time.

---

### 2. Reverse an Integer
- **File**: [`reverse_number.py`](reverse_number.py)
- **Problem**: Reverse the digits of integer $N$ mathematically without converting to a string.
- **Algorithm**:
  ```python
  reverse = 0
  while number > 0:
      remainder = number % 10          # Extract rightmost digit
      reverse = reverse * 10 + remainder  # Shift left and append
      number //= 10                    # Truncate rightmost digit
  ```
- **Interview Note (LeetCode 7)**: In 32-bit environments (C++/Java), check for integer overflow against $[ -2^{31}, 2^{31} - 1 ]$ before multiplying by 10.

---

### 3. Palindrome Number
- **File**: [`palindrome_number.py`](palindrome_number.py)
- **Problem**: Determine whether integer $N$ reads identically forwards and backwards (LeetCode 9).
- **Edge Cases**:
  - Negative numbers (e.g. $-121$): Always `False` because the negative sign `'-'` breaks symmetry.
  - Numbers ending in 0 (e.g. $10$): Always `False` (except $0$ itself), because no standard positive number starts with 0.
- **Algorithm**: Reverse $N$ mathematically and verify `reverse == original_number`.

---

### 4. Greatest Common Divisor (GCD / HCF)
- **File**: [`gcd.py`](gcd.py)
- **Problem**: Find the largest integer dividing both $a$ and $b$ evenly.
- **Optimal Method (Euclidean Algorithm by Modulo Division)**:
  $$\gcd(a, b) = \gcd(b, a \pmod b)$$
  - Repeatedly apply until $b = 0$; the remaining value of $a$ is the GCD.
  - **Time Complexity**: $O(\log(\min(a, b)))$ (bounded by Lamé's Theorem).
- **Key Relationship to LCM**:
  $$a \times b = \gcd(a, b) \times \text{lcm}(a, b) \implies \text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$

---

### 5. Armstrong Number (Narcissistic Number)
- **File**: [`armstrong.py`](armstrong.py)
- **Problem**: An Armstrong number of $k$ digits equals the sum of each digit raised to the power $k$.
  $$\sum_{i=1}^k d_i^k = N$$
- **Examples**:
  - $153 \implies 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$ (True)
  - $1634 \implies 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ (True)
  - $35 \implies 3^2 + 5^2 = 9 + 25 = 34 \ne 35$ (False)

---

### 6. All Divisors of a Number
- **File**: [`all_divisors.py`](all_divisors.py)
- **Problem**: Return all unique factors of $N$.
- **Optimal Symmetrical Pair Property**:
  If $i$ divides $N$, then $\frac{N}{i}$ also divides $N$:
  $$i \times \left(\frac{N}{i}\right) = N$$
  - Every factor pair has at least one factor $\le \sqrt{N}$.
  - Loop only from $1$ to $\lfloor\sqrt{N}\rfloor$ (`math.isqrt(N)`).
  - Time drops from $O(N)$ to $O(\sqrt{N})$ (for $N = 10^9$, checks $31,622$ iterations instead of $10^9$).

---

### 7. Check for Prime
- **File**: [`prime.py`](prime.py)
- **Problem**: Verify if $N > 1$ has no positive divisors other than $1$ and itself.
- **Trial Division up to $\sqrt{N}$**:
  - If composite, $N = a \times b$. If both $a > \sqrt{N}$ and $b > \sqrt{N}$, then $a \times b > N$ (contradiction).
  - Thus, testing integers in $[2, \lfloor\sqrt{N}\rfloor]$ guarantees correctness in $O(\sqrt{N})$ time.
