"""Pseudocode & Reference Implementation: Quick Sort.

This module provides standard, language-agnostic pseudocode alongside an
executable Python reference implementation for Quick Sort (Lomuto Partition).

================================================================================
ALGORITHM PSEUDOCODE (CLRS / Lomuto Partitioning)
================================================================================

ALGORITHM QuickSort(A, low, high):
    Input: Array A, starting index 'low', ending index 'high'
    Output: Array A sorted in-place between indices 'low' and 'high'

    IF low < high THEN:
        pivot_index ← Partition(A, low, high)
        QuickSort(A, low, pivot_index - 1)
        QuickSort(A, pivot_index + 1, high)
    END IF


ALGORITHM Partition(A, low, high):
    Input: Array A, starting index 'low', ending index 'high'
    Output: Final index of the placed pivot element

    pivot ← A[high]             // Choose last element as pivot
    i ← low - 1                 // Boundary for elements smaller than pivot

    FOR j ← low TO high - 1 DO:
        IF A[j] < pivot THEN:
            i ← i + 1
            SWAP A[i] WITH A[j]
        END IF
    END FOR

    SWAP A[i + 1] WITH A[high]  // Move pivot to its correct sorted slot
    RETURN i + 1                // Return pivot position

================================================================================
LINE-BY-LINE PSEUDOCODE BREAKDOWN
================================================================================
1. `IF low < high THEN`:
   Base Case: Single-element or empty range requires no sorting.
2. `pivot ← A[high]`:
   Lomuto scheme designates the last element in the partition as the pivot.
3. `i ← low - 1`:
   Tracks the upper boundary of the smaller-than-pivot subarray.
4. `FOR j ← low TO high - 1 DO`:
   Examines each element. If `A[j] < pivot`, increment `i` and swap `A[i]` and
   `A[j]`, keeping smaller values on the left.
5. `SWAP A[i + 1] WITH A[high]`:
   Places pivot directly between the smaller elements (<= i) and larger
   elements (>= i + 2).
6. `QuickSort(A, low, pivot_index - 1); QuickSort(A, pivot_index + 1, high)`:
   Recursively sorts the partitions to the left and right of the pivot.

================================================================================
COMPLEXITY MATRIX
================================================================================
- Time Complexity:
  - Best Case:    O(N log N) (Pivot splits array into equal halves)
  - Average Case: O(N log N) (Randomized/general inputs)
  - Worst Case:   O(N^2) (Already sorted array with extreme pivot)
- Auxiliary Space:
  - Call Stack:   O(log N) average, O(N) worst case
  - Heap Memory:  O(1) (In-place index-based sorting)
- Stability:       Unstable
"""


def partition(numbers: list[int], low: int, high: int) -> int:
    """Partition subarray numbers[low...high] around pivot numbers[high]."""
    # pivot = A[high]
    pivot: int = numbers[high]

    # i = low - 1
    i: int = low - 1

    # FOR j FROM low TO high - 1 DO
    for j in range(low, high):
        # IF A[j] < pivot THEN
        if numbers[j] < pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    # SWAP A[i + 1] WITH A[high]
    numbers[i + 1], numbers[high] = numbers[high], numbers[i + 1]

    # RETURN i + 1
    return i + 1


def quick_sort_pseudo_code(
    numbers: list[int], low: int = 0, high: int | None = None
) -> list[int]:
    """Recursively sort a list of integers in-place using QuickSort pseudocode."""
    if high is None:
        high = len(numbers) - 1

    # IF low < high THEN
    if low < high:
        # pivot_index = Partition(A, low, high)
        pivot_index: int = partition(numbers=numbers, low=low, high=high)

        # QuickSort(A, low, pivot_index - 1)
        quick_sort_pseudo_code(numbers=numbers, low=low, high=pivot_index - 1)

        # QuickSort(A, pivot_index + 1, high)
        quick_sort_pseudo_code(numbers=numbers, low=pivot_index + 1, high=high)

    return numbers


# Example execution
if __name__ == "__main__":
    sample: list[int] = [10, 80, 30, 90, 40, 50, 70]
    print(f"Original: {sample}")
    sorted_sample: list[int] = quick_sort_pseudo_code(numbers=sample)
    print(f"Sorted:   {sorted_sample}")
