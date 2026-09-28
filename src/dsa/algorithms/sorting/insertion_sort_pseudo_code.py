"""Pseudocode & Reference Implementation: Insertion Sort.

This module provides standard, language-agnostic pseudocode alongside an
executable Python reference implementation for Insertion Sort.

================================================================================
ALGORITHM PSEUDOCODE (CLRS Standard)
================================================================================

ALGORITHM InsertionSort(A):
    Input: Array A of n elements (0-indexed)
    Output: Array A sorted in non-decreasing order

    n ← length(A)

    // Outer loop: pick elements starting from index 1
    FOR i ← 1 TO n - 1 DO:
        key ← A[i]
        j ← i - 1

        // Inner while loop: shift elements of sorted prefix that are > key
        WHILE j ≥ 0 AND A[j] > key DO:
            A[j + 1] ← A[j]
            j ← j - 1
        END WHILE

        // Place the key into its correct sorted slot
        A[j + 1] ← key
    END FOR

    RETURN A

================================================================================
LINE-BY-LINE PSEUDOCODE BREAKDOWN
================================================================================
1. `n ← length(A)`:
   Retrieve total length of array.
2. `FOR i ← 1 TO n - 1 DO`:
   A[0] is trivially a 1-element sorted prefix. Loop selects each subsequent
   unsorted element.
3. `key ← A[i]`:
   Store the current element to be inserted into the sorted prefix.
4. `j ← i - 1`:
   Point to the rightmost index of the sorted prefix.
5. `WHILE j ≥ 0 AND A[j] > key DO`:
   Traverse backward through the sorted prefix. If an element is strictly
   greater than `key`, it must be moved one position to the right.
6. `A[j + 1] ← A[j]; j ← j - 1`:
   Shift element rightward, opening an insertion vacancy, and advance backward.
7. `A[j + 1] ← key`:
   Insert the key into the vacant position (where A[j] <= key or j = -1).

================================================================================
COMPLEXITY MATRIX
================================================================================
- Time Complexity:
  - Best Case:    O(N) (Already sorted; inner while loop fails in O(1))
  - Average Case: O(N^2) (Shifts ~i/2 elements on average)
  - Worst Case:   O(N^2) (Reverse-sorted input)
- Auxiliary Space: O(1) (In-place sort)
- Stability:       Stable (Strict inequality > preserves duplicate ordering)
"""


def insertion_sort_pseudo_code(numbers: list[int]) -> list[int]:
    """Sort a list of integers using textbook Insertion Sort pseudocode."""
    n: int = len(numbers)

    # Base Case / Guard Clause: 0 or 1 element is already sorted
    if n <= 1:
        return numbers

    # FOR i FROM 1 TO n - 1 DO
    for i in range(1, n):
        # key = A[i]
        key: int = numbers[i]
        j: int = i - 1

        # WHILE j >= 0 AND A[j] > key DO
        while j >= 0 and numbers[j] > key:
            # A[j + 1] = A[j]
            numbers[j + 1] = numbers[j]
            j -= 1

        # A[j + 1] = key
        numbers[j + 1] = key

    return numbers


# Example execution
if __name__ == "__main__":
    sample: list[int] = [12, 11, 13, 5, 6]
    print(f"Original: {sample}")
    sorted_sample: list[int] = insertion_sort_pseudo_code(numbers=sample)
    print(f"Sorted:   {sorted_sample}")
