"""Pseudocode & Reference Implementation: Merge Sort.

This module provides standard, language-agnostic pseudocode alongside an
executable Python reference implementation for Merge Sort.

================================================================================
ALGORITHM PSEUDOCODE (Divide and Conquer)
================================================================================

ALGORITHM MergeSort(A):
    Input: Array A of n elements
    Output: Array A sorted in non-decreasing order

    IF length(A) ≤ 1 THEN:
        RETURN A
    END IF

    // Divide: Find midpoint and partition into left and right halves
    mid ← length(A) / 2
    left ← MergeSort(A[0 ... mid - 1])
    right ← MergeSort(A[mid ... length(A) - 1])

    // Combine: Merge the two sorted halves
    RETURN Merge(left, right)


ALGORITHM Merge(left, right):
    Input: Two sorted arrays 'left' and 'right'
    Output: Single sorted array combining 'left' and 'right'

    result ← empty list
    i ← 0
    j ← 0

    // Compare elements from both lists and append the smaller value
    WHILE i < length(left) AND j < length(right) DO:
        IF left[i] ≤ right[j] THEN:
            APPEND left[i] TO result
            i ← i + 1
        ELSE:
            APPEND right[j] TO result
            j ← j + 1
        END IF
    END WHILE

    // Append any remaining elements
    APPEND remaining elements of left TO result
    APPEND remaining elements of right TO result

    RETURN result

================================================================================
LINE-BY-LINE PSEUDOCODE BREAKDOWN
================================================================================
1. `IF length(A) ≤ 1 THEN RETURN A`:
   Base Case: Arrays with 0 or 1 element are trivially sorted.
2. `mid ← length(A) / 2`:
   Calculates split point to bisect the problem size.
3. `left ← MergeSort(...); right ← MergeSort(...)`:
   Recursively solves smaller subproblems (log2(N) levels deep).
4. `Merge(left, right)`:
   Combines two sorted sublists in O(N) linear time using two pointers i and j.
5. `IF left[i] ≤ right[j]`:
   Using `<=` ensures stability by prioritizing left duplicates over right ones.

================================================================================
COMPLEXITY MATRIX
================================================================================
- Time Complexity:
  - Best Case:    O(N log N)
  - Average Case: O(N log N)
  - Worst Case:   O(N log N) (Guaranteed across all inputs)
- Auxiliary Space: O(N) (For merging buffer)
- Call Stack:      O(log N) frames
- Stability:       Stable
"""


def merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted sublists into a single sorted list using two pointers."""
    result: list[int] = []
    i: int = 0
    j: int = 0

    # WHILE i < length(left) AND j < length(right) DO
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort_pseudo_code(numbers: list[int]) -> list[int]:
    """Recursively sort a list of integers using textbook Merge Sort pseudocode."""
    # Base Case: Array with 0 or 1 element is already sorted
    if len(numbers) <= 1:
        return numbers

    # mid = length(A) / 2
    mid: int = len(numbers) // 2

    # Recursively sort left and right halves
    left: list[int] = merge_sort_pseudo_code(numbers=numbers[:mid])
    right: list[int] = merge_sort_pseudo_code(numbers=numbers[mid:])

    # Combine step
    return merge(left=left, right=right)


# Example execution
if __name__ == "__main__":
    sample: list[int] = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original: {sample}")
    sorted_sample: list[int] = merge_sort_pseudo_code(numbers=sample)
    print(f"Sorted:   {sorted_sample}")
