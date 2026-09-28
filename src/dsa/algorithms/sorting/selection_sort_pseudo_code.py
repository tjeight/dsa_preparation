"""Pseudocode & Reference Implementation: Selection Sort.

This module provides standard, language-agnostic pseudocode alongside an
executable Python reference implementation for Selection Sort.

================================================================================
ALGORITHM PSEUDOCODE (CLRS / Textbook Standard)
================================================================================

ALGORITHM SelectionSort(A):
    Input: Array A of n elements (0-indexed)
    Output: Array A sorted in non-decreasing order

    n ← length(A)

    // Outer loop: iterate through every boundary index
    FOR i ← 0 TO n - 2 DO:
        min_index ← i

        // Inner loop: search for the minimum element in unsorted suffix
        FOR j ← i + 1 TO n - 1 DO:
            IF A[j] < A[min_index] THEN:
                min_index ← j
            END IF
        END FOR

        // Swap the found minimum element with element at boundary index i
        IF min_index ≠ i THEN:
            SWAP A[i] WITH A[min_index]
        END IF
    END FOR

    RETURN A

================================================================================
LINE-BY-LINE PSEUDOCODE BREAKDOWN
================================================================================
1. `n ← length(A)`:
   Determine total number of elements.
2. `FOR i ← 0 TO n - 2 DO`:
   Advances the boundary of the sorted prefix. An array of size n needs at most
   n - 1 passes because the last remaining element is automatically sorted.
3. `min_index ← i`:
   Hypothesize that the current boundary element is the smallest.
4. `FOR j ← i + 1 TO n - 1 DO`:
   Scan the remaining unsorted subarray to find any smaller element.
5. `IF A[j] < A[min_index] THEN min_index ← j`:
   Update `min_index` whenever a strictly smaller value is found.
6. `IF min_index ≠ i THEN SWAP A[i] WITH A[min_index]`:
   Perform at most 1 swap per outer pass, placing the true minimum in slot i.

================================================================================
COMPLEXITY MATRIX
================================================================================
- Time Complexity:
  - Best Case:    O(N^2) (Always executes full inner scan)
  - Average Case: O(N^2)
  - Worst Case:   O(N^2)
- Auxiliary Space: O(1) (In-place sort)
- Total Swaps:     At most N - 1 swaps (O(N))
- Stability:       Unstable
"""


def selection_sort_pseudo_code(numbers: list[int]) -> list[int]:
    """Sort a list of integers using textbook Selection Sort pseudocode."""
    n: int = len(numbers)

    # Base Case / Guard Clause: 0 or 1 element is already sorted
    if n <= 1:
        return numbers

    # FOR i FROM 0 TO n - 2 DO
    for i in range(n - 1):
        # min_index = i
        min_index: int = i

        # FOR j FROM i + 1 TO n - 1 DO
        for j in range(i + 1, n):
            # IF A[j] < A[min_index] THEN min_index = j
            if numbers[j] < numbers[min_index]:
                min_index = j

        # IF min_index != i THEN SWAP A[i] WITH A[min_index]
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers


# Example execution
if __name__ == "__main__":
    sample: list[int] = [64, 25, 12, 22, 11]
    print(f"Original: {sample}")
    sorted_sample: list[int] = selection_sort_pseudo_code(numbers=sample)
    print(f"Sorted:   {sorted_sample}")
