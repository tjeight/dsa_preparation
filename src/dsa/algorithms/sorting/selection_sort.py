"""Problem: Sort an Array Using Selection Sort.

Selection Sort is a comparison-based in-place sorting algorithm that divides the
input list into two parts:
1. A sorted sublist on the left (initially empty).
2. An unsorted sublist on the right (initially the entire list).

In each pass, the algorithm selects the minimum element from the unsorted sublist
and moves it to the end of the sorted sublist (index `i`).

Examples:
    [9, 52, 63, 5, 48, 5] -> [5, 5, 9, 48, 52, 63]
    [5, 4, 3, 2, 1]       -> [1, 2, 3, 4, 5]
    [1, 2, 3]             -> [1, 2, 3]
    [42]                  -> [42]
    []                    -> []

Algorithm Mechanics (Current Immediate-Swap / Exchange Variant):
---------------------------------------------------------------
1. Outer Loop (`i` from 0 to `n - 2`):
   - Designates index `i` as the target slot for the i-th smallest element.
   - Elements to the left of `i` (`numbers[0...i-1]`) are already sorted and in
     their final resting positions.

2. Inner Loop (`j` from `i + 1` to `n - 1`):
   - Scans the remaining unsorted suffix.
   - Whenever `numbers[i] > numbers[j]`, elements are swapped immediately.
   - By swapping immediately, `numbers[i]` always holds the minimum element
     found so far.
   - Once the inner loop completes, `numbers[i]` contains the absolute minimum
     of `numbers[i...n-1]`.

Step-by-Step Dry Run (numbers = [9, 52, 63, 5, 48, 5]):
-------------------------------------------------------
Pass 0 (i = 0, target sorted index 0):
- Compare 9 vs 52 -> no swap
- Compare 9 vs 63 -> no swap
- Compare 9 vs 5  -> 9 > 5  -> Swap! [5, 52, 63, 9, 48, 5]
- Compare 5 vs 48 -> no swap
- Compare 5 vs 5  -> no swap
- Array after Pass 0: [5 | 52, 63, 9, 48, 5]

Pass 1 (i = 1, target sorted index 1):
- Compare 52 vs 63 -> no swap
- Compare 52 vs 9  -> 52 > 9 -> Swap! [5, 9, 63, 52, 48, 5]
- Compare 9 vs 48  -> no swap
- Compare 9 vs 5   -> 9 > 5  -> Swap! [5, 5, 63, 52, 48, 9]
- Array after Pass 1: [5, 5 | 63, 52, 48, 9]

Pass 2 (i = 2, target sorted index 2):
- Compare 63 vs 52 -> Swap! [5, 5, 52, 63, 48, 9]
- Compare 52 vs 48 -> Swap! [5, 5, 48, 63, 52, 9]
- Compare 48 vs 9  -> Swap! [5, 5, 9, 63, 52, 48]
- Array after Pass 2: [5, 5, 9 | 63, 52, 48]

Pass 3 (i = 3, target sorted index 3):
- Compare 63 vs 52 -> Swap! [5, 5, 9, 52, 63, 48]
- Compare 52 vs 48 -> Swap! [5, 5, 9, 48, 63, 52]
- Array after Pass 3: [5, 5, 9, 48 | 63, 52]

Pass 4 (i = 4, target sorted index 4):
- Compare 63 vs 52 -> Swap! [5, 5, 9, 48, 52, 63]
- Array after Pass 4: [5, 5, 9, 48, 52 | 63]
Final Output: [5, 5, 9, 48, 52, 63]

Complexity Analysis:
--------------------
- Comparisons:
  - Pass 0: (n - 1) comparisons
  - Pass 1: (n - 2) comparisons
  - ...
  - Pass (n - 2): 1 comparison
  - Total comparisons = (n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2 = O(N^2).
- Time Complexity:
  - Best Case:    O(N^2) (always executes all comparisons regardless of initial order)
  - Average Case: O(N^2)
  - Worst Case:   O(N^2)
- Auxiliary Space: O(1) (In-place sorting algorithm; requires no extra memory).
- Stability: Unstable (Long-range swaps can alter relative order of duplicates).

DSA Optimization Note (Textbook Min-Index Selection Sort):
----------------------------------------------------------
In textbook Selection Sort, swaps inside the inner loop are deferred. Instead of
swapping immediately upon finding any smaller element, we track `min_idx`:
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_idx]:
                min_idx = j
        if min_idx != i:
            numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]
Benefit: Reduces total swaps from O(N^2) worst case to at most O(N) swaps
(at most 1 swap per outer pass). Useful when writing to memory is expensive.
"""


def selection_sort(numbers: list[int]) -> list[int]:
    """Sort a list of integers in ascending order using Selection Sort."""
    n = len(numbers)

    # Base Case / Guard Clause: 0 or 1 element is already sorted
    if n <= 1:
        return numbers

    # Outer loop: Advance the boundary of the sorted prefix [0...i-1]
    for i in range(n - 1):
        # Inner loop: Scan the unsorted suffix [i+1...n-1]
        for j in range(i + 1, n):
            # If current element is greater, swap immediately
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


# Example input list containing unsorted integers with duplicates
numbers = [9, 52, 63, 5, 48, 5]

# Execute selection sort and print the resulting sorted list
print(selection_sort(numbers))
