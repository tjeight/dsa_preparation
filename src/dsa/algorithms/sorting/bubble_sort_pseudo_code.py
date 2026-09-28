"""Pseudocode & Reference Implementation: Bubble Sort.

This module provides standard, language-agnostic pseudocode alongside an
executable Python reference implementation for Bubble Sort.

================================================================================
ALGORITHM PSEUDOCODE (Optimized with Early Exit Flag)
================================================================================

ALGORITHM BubbleSort(A):
    Input: Array A of n elements (0-indexed)
    Output: Array A sorted in non-decreasing order

    n ← length(A)

    // Outer loop: controls passes across the array
    FOR i ← 0 TO n - 1 DO:
        swapped ← FALSE

        // Inner loop: compare adjacent elements up to unsorted boundary
        FOR j ← 0 TO n - i - 2 DO:
            IF A[j] > A[j + 1] THEN:
                SWAP A[j] WITH A[j + 1]
                swapped ← TRUE
            END IF
        END FOR

        // Early Exit: if no swaps occurred, array is already sorted
        IF swapped IS FALSE THEN:
            BREAK
        END IF
    END FOR

    RETURN A

================================================================================
LINE-BY-LINE PSEUDOCODE BREAKDOWN
================================================================================
1. `n ← length(A)`:
   Retrieve array size.
2. `FOR i ← 0 TO n - 1 DO`:
   Each pass guarantees the next largest element settles into its correct
   position at the right end of the array.
3. `swapped ← FALSE`:
   Track if any inversions were fixed during this pass.
4. `FOR j ← 0 TO n - i - 2 DO`:
   Scan unsorted prefix. The boundary `n - i - 2` avoids redundant comparisons
   against already-sorted tail elements.
5. `IF A[j] > A[j + 1] THEN SWAP A[j] WITH A[j + 1]`:
   Adjacent comparison. If out of order, bubble the larger element to the right.
6. `IF swapped IS FALSE THEN BREAK`:
   If an entire pass made 0 swaps, the array is sorted. Halting early achieves
   O(N) linear time for sorted arrays.

================================================================================
COMPLEXITY MATRIX
================================================================================
- Time Complexity:
  - Best Case:    O(N) (Already sorted array with early exit flag)
  - Average Case: O(N^2)
  - Worst Case:   O(N^2) (Reverse sorted array)
- Auxiliary Space: O(1) (In-place sort)
- Stability:       Stable (Strict inequality > preserves duplicate ordering)
"""


def bubble_sort_pseudo_code(numbers: list[int]) -> list[int]:
    """Sort a list of integers using optimized Bubble Sort pseudocode."""
    n: int = len(numbers)

    # Base Case / Guard Clause: 0 or 1 element is already sorted
    if n <= 1:
        return numbers

    # FOR i FROM 0 TO n - 1 DO
    for i in range(n):
        # swapped = FALSE
        swapped: bool = False

        # FOR j FROM 0 TO n - i - 2 DO
        for j in range(n - i - 1):
            # IF A[j] > A[j + 1] THEN SWAP
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True

        # IF swapped IS FALSE THEN BREAK
        if not swapped:
            break

    return numbers


# Example execution
if __name__ == "__main__":
    sample: list[int] = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {sample}")
    sorted_sample: list[int] = bubble_sort_pseudo_code(numbers=sample)
    print(f"Sorted:   {sorted_sample}")
