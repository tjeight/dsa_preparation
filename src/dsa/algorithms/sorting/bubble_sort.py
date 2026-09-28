"""Problem: Sort an Array Using Bubble Sort.

Bubble Sort is an elementary comparison-based sorting algorithm that repeatedly
steps through the list, compares adjacent elements, and swaps them if they are
in the wrong order (numbers[j] > numbers[j + 1]).

The algorithm gets its name because smaller elements gradually "bubble" to the
top (beginning of the list) while larger elements sink to the bottom (end of the
list) after each pass.

Examples:
    [52, 69, 3, 82, 4, 16, 54] -> [3, 4, 16, 52, 54, 69, 82]
    [5, 1, 4, 2, 8]             -> [1, 2, 4, 5, 8]
    [1, 2, 3]                   -> [1, 2, 3]
    [42]                        -> [42]
    []                          -> []

Algorithm Mechanics:
--------------------
1. Outer Loop (`i` from 0 to `n - 1`):
   - Controls the number of passes across the list.
   - After pass `i`, the largest `i + 1` elements are guaranteed to have
     bubbled up to their final resting positions at `numbers[n - 1 - i...n - 1]`.

2. Inner Loop (`j` from 0 to `n - i - 2` via `range(n - i - 1)`):
   - Compares adjacent pairs `numbers[j]` and `numbers[j + 1]`.
   - If `numbers[j] > numbers[j + 1]`, they are swapped in-place.
   - The upper bound `n - i - 1` avoids re-checking already sorted elements at
     the tail.

Step-by-Step Dry Run (numbers = [52, 69, 3, 82, 4, 16, 54], n = 7):
-------------------------------------------------------------------
Pass 0 (i = 0, j from 0 to 5):
- j=0: 52 vs 69 -> 52 <= 69 -> No swap
- j=1: 69 vs 3  -> 69 > 3   -> Swap! [52, 3, 69, 82, 4, 16, 54]
- j=2: 69 vs 82 -> 69 <= 82 -> No swap
- j=3: 82 vs 4  -> 82 > 4   -> Swap! [52, 3, 69, 4, 82, 16, 54]
- j=4: 82 vs 16 -> 82 > 16  -> Swap! [52, 3, 69, 4, 16, 82, 54]
- j=5: 82 vs 54 -> 82 > 54  -> Swap! [52, 3, 69, 4, 16, 54, 82]
-> 82 bubbled to index 6: [52, 3, 69, 4, 16, 54 | 82]

Pass 1 (i = 1, j from 0 to 4):
- j=0: 52 vs 3  -> 52 > 3   -> Swap! [3, 52, 69, 4, 16, 54, 82]
- j=1: 52 vs 69 -> 52 <= 69 -> No swap
- j=2: 69 vs 4  -> 69 > 4   -> Swap! [3, 52, 4, 69, 16, 54, 82]
- j=3: 69 vs 16 -> 69 > 16  -> Swap! [3, 52, 4, 16, 69, 54, 82]
- j=4: 69 vs 54 -> 69 > 54  -> Swap! [3, 52, 4, 16, 54, 69, 82]
-> 69 bubbled to index 5: [3, 52, 4, 16, 54 | 69, 82]

Pass 2 (i = 2, j from 0 to 3):
- j=0: 3 vs 52  -> 3 <= 52  -> No swap
- j=1: 52 vs 4  -> 52 > 4   -> Swap! [3, 4, 52, 16, 54, 69, 82]
- j=2: 52 vs 16 -> 52 > 16  -> Swap! [3, 4, 16, 52, 54, 69, 82]
- j=3: 52 vs 54 -> 52 <= 54 -> No swap
-> 54 bubbled to index 4: [3, 4, 16, 52 | 54, 69, 82]

Pass 3 to 6: Remaining passes verify sorted order without further swaps.
Final Output: [3, 4, 16, 52, 54, 69, 82]

Complexity Analysis:
--------------------
- Comparisons:
  - (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 = O(N^2).
- Time Complexity:
  - Best Case:    O(N^2) (Standard form executes all iterations)
  - Average Case: O(N^2)
  - Worst Case:   O(N^2) (Reverse sorted array produces maximum swaps)
- Auxiliary Space: O(1) (In-place sort modifying the array by reference).
- Stability: Stable (Strict inequality `>` ensures equal elements never swap).

DSA Optimization Note (Early Exit Flag):
----------------------------------------
In an optimized Bubble Sort, introduce a `swapped` boolean flag. If a full pass
completes with no swaps, the array is already sorted and we can break early:
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        if not swapped:
            break
Benefit: Improves best-case time complexity to O(N) linear time for already
sorted or nearly sorted arrays.
"""


def bubble_sort(numbers: list[int]) -> list[int]:
    """Sort a list of integers in ascending order using Bubble Sort."""
    n: int = len(numbers)

    # Base Case / Guard Clause: Lists of length 0 or 1 are already sorted
    if n <= 1:
        return numbers

    # Outer loop: Number of bubbling passes (n passes in standard form)
    for i in range(n):
        # Inner loop: Compare adjacent elements up to unsorted boundary (n - i - 1)
        for j in range(n - i - 1):
            # If current element exceeds next element, swap them
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


# Example input list containing unsorted integers
numbers: list[int] = [52, 69, 3, 82, 4, 16, 54]


# Execute bubble sort and print the resulting sorted list
print(bubble_sort(numbers=numbers))
