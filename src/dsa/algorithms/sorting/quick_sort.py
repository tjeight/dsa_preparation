"""Problem: Sort an Array Using Quick Sort (Lomuto Partitioning).

Quick Sort is an efficient, comparison-based divide-and-conquer sorting algorithm.
It works by selecting a 'pivot' element from the array and partitioning the
remaining elements into two sub-arrays according to whether they are less than
or greater than the pivot. The sub-arrays are then sorted recursively.

Examples:
    [5, 9, 36, 8, 22, 6, 4] -> [4, 5, 6, 8, 9, 22, 36]
    [5, 4, 3, 2, 1]         -> [1, 2, 3, 4, 5]
    [1, 2, 3]               -> [1, 2, 3]
    [42]                    -> [42]
    []                      -> []

Lomuto Partitioning Strategy:
-----------------------------
1. Pivot Selection:
   - Chooses the last element as pivot: `pivot = numbers[-1]`.

2. Partitioning Process:
   - Pointer `i = -1`: Marks the boundary of elements strictly smaller than pivot.
   - Pointer `j`: Scans from index `0` up to `len(numbers) - 2`.
   - If `numbers[j] < pivot`:
     - Increment `i` to expand the smaller-element zone.
     - Swap `numbers[i]` and `numbers[j]`.

3. Pivot Placement:
   - Swap `numbers[i + 1]` with `numbers[-1]`.
   - The pivot is now at its final sorted position `pivot_index = i + 1`.
   - All elements to its left are `< pivot`, and all to its right are `>= pivot`.

4. Divide & Conquer:
   - Recursively sort the left slice: `numbers[:pivot_index]`.
   - Recursively sort the right slice: `numbers[pivot_index + 1:]`.
   - Combine: `left + [pivot] + right`.

Step-by-Step Dry Run (numbers = [5, 9, 36, 8, 22, 6, 4], n = 7):
-----------------------------------------------------------------
Initial State: [5, 9, 36, 8, 22, 6, 4], pivot = 4, i = -1
- j=0: 5 < 4 (False)
- j=1: 9 < 4 (False)
- j=2: 36 < 4 (False)
- j=3: 8 < 4 (False)
- j=4: 22 < 4 (False)
- j=5: 6 < 4 (False)
- Swap pivot into position: swap numbers[0] (5) and numbers[-1] (4)
- Array after partition: [4 | 9, 36, 8, 22, 6, 5], pivot_index = 0
- Left subarray: numbers[:0] = [] (Base Case: returns [])
- Right subarray: numbers[1:] = [9, 36, 8, 22, 6, 5]

Subproblem right: quick_sort([9, 36, 8, 22, 6, 5]), pivot = 5
- All elements 9, 36, 8, 22, 6 >= 5 (i remains -1)
- Swap pivot into position: swap numbers[0] (9) and numbers[-1] (5)
- Array: [5 | 36, 8, 22, 6, 9], pivot_index = 0
- Left: [], Right: [36, 8, 22, 6, 9]

Subproblem right: quick_sort([36, 8, 22, 6, 9]), pivot = 9
- j=1: 8 < 9  -> i=0 -> swap numbers[0] (36) and numbers[1] (8) -> [8, 36, 22, 6, 9]
- j=3: 6 < 9  -> i=1 -> swap numbers[1] (36) and numbers[3] (6) -> [8, 6, 22, 36, 9]
- Swap pivot: swap numbers[2] (22) and numbers[-1] (9) -> [8, 6, 9, 36, 22]
- Left: quick_sort([8, 6]) -> [6, 8]
- Right: quick_sort([36, 22]) -> [22, 36]
- Combined: [6, 8] + [9] + [22, 36] = [6, 8, 9, 22, 36]

Final Combined Array: [4] + [5] + [6, 8, 9, 22, 36] = [4, 5, 6, 8, 9, 22, 36]

Complexity Analysis:
--------------------
- Time Complexity:
  - Best Case:    O(N log N) (Occurs when pivot splits array into equal halves)
  - Average Case: O(N log N) (Expected time over all input permutations)
  - Worst Case:   O(N^2) (Occurs when pivot is always the smallest or largest
                  element, e.g. already sorted array with last-element pivot)
- Auxiliary Space:
  - Call Stack Depth: O(log N) average, O(N) worst case.
  - Slicing & Concatenation Memory: O(N log N) average auxiliary heap memory.
- Stability: Unstable (Long-distance swaps can reorder identical elements).

DSA Optimization Note (In-Place Pointer-Based QuickSort):
---------------------------------------------------------
In production or technical interviews, QuickSort is typically implemented
in-place using index boundaries `low` and `high` to avoid memory allocations
from slicing (`numbers[:]`) and list concatenation (`+`):
    def quick_sort_inplace(arr: list[int], low: int, high: int):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_inplace(arr, low, pi - 1)
            quick_sort_inplace(arr, pi + 1, high)
- Memory: Drops from O(N log N) to O(1) auxiliary heap space.
- Pivot Strategy: Randomized pivot or 'Median-of-Three' avoids the O(N^2)
  degradation on already sorted arrays.
"""


def quick_sort(numbers: list[int]):
    """Recursively sort a list of integers using Lomuto Quick Sort."""
    # Base Case: Lists with 0 or 1 element are already sorted
    if len(numbers) <= 1:
        return numbers

    # Step 1 is to choose the pivot (last element in Lomuto's scheme)
    pivot = numbers[-1]

    # i tracks the boundary of elements strictly smaller than pivot
    i = -1
    for j in range(len(numbers) - 1):
        if numbers[j] < pivot:
            # swap current smaller element into the left partition
            i = i + 1
            numbers[i], numbers[j] = numbers[j], numbers[i]

    # swap the pivot into its correct final sorted position
    numbers[i + 1], numbers[-1] = numbers[-1], numbers[i + 1]

    # get the pivot index
    pivot_index = i + 1

    # Sort the before the pivot and after the pivot recursively
    left = quick_sort(numbers=numbers[:pivot_index])
    right = quick_sort(numbers=numbers[pivot_index + 1 :])

    # Combine the sorted left partition, pivot, and sorted right partition
    return left + [pivot] + right


# Example input list containing unsorted integers
numbers: list[int] = [5, 9, 36, 8, 22, 6, 4]


# Execute quick sort and print the resulting sorted list
print(quick_sort(numbers=numbers))
