# Star & Number Patterns in Python

This folder contains implementations of the **22 foundational pattern problems** (popularized in DSA sheets like Striver's A2Z DSA Course). Patterns build intuition for nested loops, coordinate geometry in grids, indexing math, symmetry, and ASCII character arithmetic.

---

## 🧠 The 4 Golden Rules for Solving Any Pattern

Whenever you encounter a pattern problem:
1. **Outer Loop**: Determine the total number of rows ($N$, $2N-1$, etc.).
2. **Inner Loop Breakdown**: In each row, observe what needs to be printed from left to right:
   - Leading spaces
   - Stars, numbers, or characters
   - Middle gaps (if hollow or butterfly)
   - Mirror/reverse stars, numbers, or characters
3. **Formula Derivation**: Connect the column count or space count mathematically to the current row index (`row` or `i`).
   - Increasing: `row + 1`
   - Decreasing: `N - row`
   - Odd progression: `2 * row + 1` or `2 * row - 1`
   - Gaps: `2 * (N - row)`
4. **Symmetry & Boundary Conditions**:
   - Check if the pattern splits into an upper and lower half.
   - For hollow shapes or borders, check boundary coordinates (`row == 0 or row == N-1 or col == 0 or col == N-1`).

---

## 📚 Complete Catalog of Patterns

| Pattern | Name | Type | Key Formula / Technique |
| :--- | :--- | :--- | :--- |
| [Pattern 1](#pattern-1-solid-square) | Solid Square | Stars | `range(n)` x `range(n)` |
| [Pattern 2](#pattern-2-right-angled-triangle) | Right-Angled Triangle | Stars | `row + 1` stars |
| [Pattern 3](#pattern-3-numbered-right-angled-triangle) | Numbered Right Triangle | Numbers | `col` from `1` to `row + 1` |
| [Pattern 4](#pattern-4-repeated-number-triangle) | Repeated Number Triangle | Numbers | `row` printed `row` times |
| [Pattern 5](#pattern-5-inverted-numbered-triangle) | Inverted Numbered Triangle | Numbers | `col` from `1` to `N - row` |
| [Pattern 6](#pattern-6-inverted-star-triangle) | Inverted Star Triangle | Stars | Stars from `N` down to `row + 1` |
| [Pattern 7](#pattern-7-full-pyramid) | Full Star Pyramid | Stars + Spaces | Spaces: `N - row`, Stars: `2*row - 1` |
| [Pattern 8](#pattern-8-inverted-pyramid) | Inverted Star Pyramid | Stars + Spaces | Spaces: `N - row`, Stars: `2*row - 1` |
| [Pattern 9](#pattern-9-diamond-star-pattern) | Diamond Star Pattern | Stars + Spaces | Pattern 7 + Pattern 8 |
| [Pattern 10](#pattern-10-half-diamond--sideways-triangle) | Half Diamond | Stars | Upper triangle + Lower triangle |
| [Pattern 11](#pattern-11-binary-number-triangle) | Binary Number Triangle | 0/1 Alternating | Toggle `to_print = 1 - to_print` |
| [Pattern 12](#pattern-12-number-crown--valley) | Number Crown / Valley | Numbers + Spaces | Left numbers, `2*(N-row)` spaces, right numbers |
| [Pattern 13](#pattern-13-floyds-triangle) | Floyd's Triangle | Numbers | Continuous running counter `to_print += 1` |
| [Pattern 14](#pattern-14-increasing-alphabet-triangle) | Increasing Alphabet Triangle | Characters | `chr(65 + col)` |
| [Pattern 15](#pattern-15-inverted-alphabet-triangle) | Inverted Alphabet Triangle | Characters | `chr(65 + col)` for `N - row` chars |
| [Pattern 16](#pattern-16-repeated-alphabet-triangle) | Repeated Alphabet Triangle | Characters | `chr(65 + row)` repeated `row + 1` times |
| [Pattern 17](#pattern-17-palindromic-alphabet-pyramid) | Palindromic Alphabet Pyramid | Characters + Spaces | Spaces: `N - row`, Ascending chars, Descending chars |
| [Pattern 18](#pattern-18-inverted-alphabet-triangle-from-n) | Reverse Alphabet Triangle | Characters | `chr(65 + (N - col))` |
| [Pattern 19](#pattern-19-symmetric-hollow-diamond) | Symmetric Hollow Diamond | Stars + Spaces | Top & Bottom mirrored: Stars, spaces, stars |
| [Pattern 20](#pattern-20-butterfly-star-pattern) | Butterfly Star Pattern | Stars + Spaces | Hourglass space center, wings expand and contract |
| [Pattern 21](#pattern-21-hollow-square) | Hollow Square | Boundary | `row in (0, N-1) or col in (0, N-1)` |
| [Pattern 22](#pattern-22-concentric-number-squares) | Concentric Number Squares | Matrix Distance | `N - min(row, col, size - 1 - row, size - 1 - col)` |

---

### Pattern 1: Solid Square
- **File**: [`pattern1.py`](pattern1.py)
- **Visual Output** ($N = 4$):
  ```text
  ****
  ****
  ****
  ****
  ```
- **Logic**:
  - Outer loop runs $N$ times (for each row).
  - Inner loop runs $N$ times (for each column), printing `'*'`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 2: Right-Angled Triangle
- **File**: [`pattern2.py`](pattern2.py)
- **Visual Output** ($N = 4$):
  ```text
  *
  **
  ***
  ****
  ```
- **Logic**:
  - For row `row` (0-indexed from `0` to `N-1`), print `row + 1` stars.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 3: Numbered Right-Angled Triangle
- **File**: [`pattern3.py`](pattern3.py)
- **Visual Output** ($N = 4$):
  ```text
  1
  12
  123
  1234
  ```
- **Logic**:
  - Outer loop runs `row` from `1` to `N`.
  - Inner loop prints numbers from `1` to `row`. The printed digit is the column index itself.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 4: Repeated Number Triangle
- **File**: [`pattern4.py`](pattern4.py)
- **Visual Output** ($N = 4$):
  ```text
  1
  22
  333
  4444
  ```
- **Logic**:
  - Outer loop runs `row` from `1` to `N`.
  - Inner loop runs `row` times, printing the row index `row` repeatedly.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 5: Inverted Numbered Triangle
- **File**: [`pattern5.py`](pattern5.py)
- **Visual Output** ($N = 4$):
  ```text
  1234
  123
  12
  1
  ```
- **Logic**:
  - Outer loop runs `row` from `0` to `N-1`.
  - In each row, columns run from `1` up to `N - row`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 6: Inverted Star Triangle
- **File**: [`pattern6.py`](pattern6.py)
- **Visual Output** ($N = 4$):
  ```text
  ****
  ***
  **
  *
  ```
- **Logic**:
  - Outer loop runs `row` from `0` to `N-1`.
  - Inner loop steps downwards: `range(number, row, -1)`, printing `N - row` stars per row.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 7: Full Pyramid
- **File**: [`pattern7.py`](pattern7.py)
- **Visual Output** ($N = 4$):
  ```text
     *
    ***
   *****
  *******
  ```
- **Logic**:
  - For `row` from `1` to `N`:
    1. Print `N - row` leading spaces.
    2. Print `2 * row - 1` stars (odd series: 1, 3, 5, 7, ...).
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 8: Inverted Pyramid
- **File**: [`pattern8.py`](pattern8.py)
- **Visual Output** ($N = 4$):
  ```text
  *******
   *****
    ***
     *
  ```
- **Logic**:
  - Outer loop counts backwards: `row` from `N` down to `1`.
  - 1. Print `N - row` leading spaces (0, 1, 2, ...).
  - 2. Print `2 * row - 1` stars ($2N-1, \dots, 1$).
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 9: Diamond Star Pattern
- **File**: [`pattern9.py`](pattern9.py)
- **Visual Output** ($N = 4$):
  ```text
     *
    ***
   *****
  *******
  *******
   *****
    ***
     *
  ```
- **Logic**:
  - Concatenation of **Pattern 7** (erect pyramid) and **Pattern 8** (inverted pyramid).
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 10: Half Diamond / Sideways Triangle
- **File**: [`pattern10.py`](pattern10.py)
- **Visual Output** ($N = 4$):
  ```text
  *
  **
  ***
  ***
  **
  *
  ```
- **Logic**:
  - Upper half: `row` runs from `1` to `N-1`, printing `'*' * row`.
  - Lower half: `row` runs from `N-1` down to `1`, printing `'*' * row`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 11: Binary Number Triangle
- **File**: [`pattern11.py`](pattern11.py)
- **Visual Output** ($N = 4$):
  ```text
  1
  01
  101
  0101
  ```
- **Logic**:
  - Starting bit depends on row parity:
    - Even row (`row % 2 == 0`): starts with `1`.
    - Odd row (`row % 2 != 0`): starts with `0`.
  - Within each row, toggle each step using `to_print = 1 - to_print`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 12: Number Crown / Valley
- **File**: [`pattern12.py`](pattern12.py)
- **Visual Output** ($N = 4$):
  ```text
  1      1
  12    21
  123  321
  12344321
  ```
- **Logic**:
  - Each row consists of 3 distinct regions:
    1. **Left wing**: Numbers from `1` to `row`.
    2. **Middle gap**: `2 * (N - row)` spaces.
    3. **Right wing**: Numbers in reverse from `row` down to `1`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 13: Floyd's Triangle
- **File**: [`pattern13.py`](pattern13.py)
- **Visual Output** ($N = 4$):
  ```text
  1 
  2 3 
  4 5 6 
  7 8 9 10 
  ```
- **Logic**:
  - Maintain a global continuous counter `to_print = 1`.
  - Row `row` prints `row + 1` numbers, incrementing `to_print` after every number.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 14: Increasing Alphabet Triangle
- **File**: [`pattern14.py`](pattern14.py)
- **Visual Output** ($N = 4$):
  ```text
  A
  AB
  ABC
  ABCD
  ```
- **Logic**:
  - ASCII value of `'A'` is `65`.
  - In each row `row` (0-indexed), print `chr(65 + col)` for `col` from `0` to `row`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 15: Inverted Alphabet Triangle
- **File**: [`pattern15.py`](pattern15.py)
- **Visual Output** ($N = 4$):
  ```text
  ABCD
  ABC
  AB
  A
  ```
- **Logic**:
  - In each row `row`, print `N - row` letters starting from `'A'` (`chr(65 + col)`).
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 16: Repeated Alphabet Triangle
- **File**: [`pattern16.py`](pattern16.py)
- **Visual Output** ($N = 4$):
  ```text
  A
  BB
  CCC
  DDDD
  ```
- **Logic**:
  - The character is fixed for each row: `chr(65 + row)`.
  - Repeat that character `row + 1` times.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 17: Palindromic Alphabet Pyramid
- **File**: [`pattern17.py`](pattern17.py)
- **Visual Output** ($N = 4$):
  ```text
     A
    ABA
   ABCBA
  ABCDCBA
  ```
- **Logic**:
  - 1. Print `N - row` leading spaces.
  - 2. Print ascending characters from `'A'` (`col = 0`) to `'A' + row`.
  - 3. Print descending characters from `'A' + row - 1` down to `'A'`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 18: Inverted Alphabet Triangle from N-th Letter
- **File**: [`pattern18.py`](pattern18.py)
- **Visual Output** ($N = 5$):
  ```text
  E 
  D E 
  C D E 
  B C D E 
  A B C D E 
  ```
- **Logic**:
  - Outer loop `row` from `1` to `N`.
  - Inner loop counts down from `row` to `1`, printing `chr(65 + (N - col))`.
  - Starts at $N$-th letter (`'E'` for $N=5$) and expands backwards to `'A'`.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 19: Symmetric Hollow Diamond
- **File**: [`pattern19.py`](pattern19.py)
- **Visual Output** ($N = 4$):
  ```text
  ********
  ***  ***
  **    **
  *      *
  *      *
  **    **
  ***  ***
  ********
  ```
- **Logic**:
  - **Top Half**: Left stars (`N - row`), spaces (`2 * row`), right stars (`N - row`).
  - **Bottom Half**: Left stars (`row + 1`), spaces (`2*(N - row - 1)`), right stars (`row + 1`).
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 20: Butterfly Star Pattern
- **File**: [`pattern20.py`](pattern20.py)
- **Visual Output** ($N = 4$):
  ```text
  *      *
  **    **
  ***  ***
  ********
  ***  ***
  **    **
  *      *
  ```
- **Logic**:
  - **Top Half** (`row` from `0` to `N-1`):
    - Left stars: `row + 1`
    - Spaces: `2 * (N - row - 1)`
    - Right stars: `row + 1`
  - **Bottom Half** (`row` from `1` to `N-1`, avoids repeating the center row):
    - Left stars: `N - row`
    - Spaces: `2 * row`
    - Right stars: `N - row`
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 21: Hollow Square
- **File**: [`pattern21.py`](pattern21.py)
- **Visual Output** ($N = 4$):
  ```text
  ****
  *  *
  *  *
  ****
  ```
- **Logic**:
  - Iterate over an $N \times N$ matrix.
  - Print `'*'` if on the boundary: `row == 0 or row == N - 1 or col == 0 or col == N - 1`.
  - Print `' '` for all internal cells.
- **Complexity**: Time: $O(N^2)$, Auxiliary Space: $O(1)$.

---

### Pattern 22: Concentric Number Squares / Number Spiral
- **File**: [`pattern22.py`](pattern22.py)
- **Visual Output** ($N = 4$):
  ```text
  4 4 4 4 4 4 4 
  4 3 3 3 3 3 4 
  4 3 2 2 2 3 4 
  4 3 2 1 2 3 4 
  4 3 2 2 2 3 4 
  4 3 3 3 3 3 4 
  4 4 4 4 4 4 4 
  ```
- **Logic**:
  - Matrix size is $(2N - 1) \times (2N - 1)$.
  - For each cell `(row, col)`, compute the minimum distance to the 4 outer edges:
    $$\text{distance} = \min(\text{row}, \text{col}, \text{size} - 1 - \text{row}, \text{size} - 1 - \text{col})$$
  - The cell value is:
    $$\text{value} = N - \text{distance}$$
  - Outer border (distance 0) $\to N$. Center cell (distance $N-1$) $\to 1$.
- **Complexity**: Time: $O((2N - 1)^2) = O(N^2)$, Auxiliary Space: $O(1)$.
