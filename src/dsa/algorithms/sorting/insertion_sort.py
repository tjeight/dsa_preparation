"""Problem: Sort an Array Using Insertion Sort.

Insertion Sort is an intuitive, comparison-based in-place sorting algorithm
analogous to the way people sort playing cards in their hands.

The array is conceptually divided into two partitions:
1. Sorted sublist on the left (`numbers[0...i-1]`).
2. Unsorted sublist on the right (`numbers[i...length-1]`).

In each pass, the algorithm picks the next element (`key = numbers[i]`) from the
unsorted partition and scans backward through the sorted partition, shifting
larger elements one position to the right to make room, then places the key into
its correct sorted position.

Examples:
    [25, 9, 53, 62, 54, 45] -> [9, 25, 45, 53, 54, 62]
    [5, 4, 3, 2, 1]         -> [1, 2, 3, 4, 5]
    [1, 2, 3]               -> [1, 2, 3]
    [42]                    -> [42]
    []                      -> []

Algorithm Mechanics:
--------------------
1. Outer Loop (`i` from 1 to `length - 1`):
   - The first element `numbers[0]` is trivially sorted by itself.
   - At each iteration `i`, `key = numbers[i]` is selected to be inserted.
   - `j = i - 1` points to the last element of the sorted prefix.

2. Inner While Loop (`j >= 0 and numbers[j] > key`):
   - Compares the `key` backward with elements in the sorted prefix.
   - As long as `numbers[j] > key`, `numbers[j]` is shifted right to
     `numbers[j + 1]`.
   - Decrements `j` to examine the next element to the left.

3. Insertion (`numbers[j + 1] = key`):
   - Once an element `<= key` is found (or `j` drops to -1), the empty slot
     at `j + 1` receives the `key`.

Step-by-Step Dry Run (numbers = [25, 9, 53, 62, 54, 45], length = 6):
--------------------------------------------------------------------
Initial State: [25 | 9, 53, 62, 54, 45] (Index 0 is sorted sublist)

Pass 1 (i = 1, key = 9, j = 0):
- numbers[0] = 25 > 9 -> Shift 25 right: [25, 25, 53, 62, 54, 45], j = -1
- Loop ends (j < 0) -> Insert key at numbers[-1 + 1] = numbers[0] = 9
- Array after Pass 1: [9, 25 | 53, 62, 54, 45]

Pass 2 (i = 2, key = 53, j = 1):
- numbers[1] = 25 <= 53 -> Loop condition fails immediately (0 shifts)
- Insert key at numbers[1 + 1] = numbers[2] = 53
- Array after Pass 2: [9, 25, 53 | 62, 54, 45]

Pass 3 (i = 3, key = 62, j = 2):
- numbers[2] = 53 <= 62 -> Loop condition fails immediately (0 shifts)
- Insert key at numbers[2 + 1] = numbers[3] = 62
- Array after Pass 3: [9, 25, 53, 62 | 54, 45]

Pass 4 (i = 4, key = 54, j = 3):
- numbers[3] = 62 > 54 -> Shift 62 right: [9, 25, 53, 62, 62, 45], j = 2
- numbers[2] = 53 <= 54 -> Loop condition fails (1 shift total)
- Insert key at numbers[2 + 1] = numbers[3] = 54
- Array after Pass 4: [9, 25, 53, 54, 62 | 45]

Pass 5 (i = 5, key = 45, j = 4):
- numbers[4] = 62 > 45 -> Shift 62 right: j = 3
- numbers[3] = 54 > 45 -> Shift 54 right: j = 2
- numbers[2] = 53 > 45 -> Shift 53 right: j = 1
- numbers[1] = 25 <= 45 -> Loop condition fails (3 shifts total)
- Insert key at numbers[1 + 1] = numbers[2] = 45
- Array after Pass 5: [9, 25, 45, 53, 54, 62]
Final Output: [9, 25, 45, 53, 54, 62]

Complexity Analysis:
--------------------
- Time Complexity:
  - Best Case:    O(N) (Occurs when array is already sorted; inner loop breaks
                  in O(1) with 0 shifts per pass, total N - 1 comparisons).
  - Average Case: O(N^2) (Each element is compared/shifted past half the sorted
                  prefix on average: ~N^2 / 4 operations).
  - Worst Case:   O(N^2) (Occurs when array is reverse-sorted; every element
                  shifts through the entire sorted prefix: N(N - 1) / 2 ops).
- Auxiliary Space: O(1) (In-place sort modifying the array by reference).
- Stability: Stable (Strict inequality `numbers[j] > key` ensures equal elements
  are never shifted past each other, preserving their initial relative order).

Why Insertion Sort is Practical in Real-World Systems:
------------------------------------------------------
1. Adaptive: Operates in O(N) linear time on sorted or nearly sorted data.
2. Low Overhead: Has the smallest constant factor among sorting algorithms.
3. Hybrid Engines: Real-world sorting engines (Python's Timsort and C++'s
   Introsort) switch to Insertion Sort for small partitions (N < 64) because it
   outperforms QuickSort/MergeSort due to cache efficiency.
4. Online Algorithm: Can sort streaming data on-the-fly as elements arrive.
"""


def insertion_sort(numbers: list[int]) -> list[int]:
    """Sort a list of integers in ascending order using Insertion Sort."""
    # get the len of the numbers
    length: int = len(numbers)

    for i in range(1, length):
        # Always the ith index will be the key
        key = numbers[i]
        j = i - 1

        # the inner loop will find the exact index of the element in the sorted array
        # Shift elements greater than key one position to the right
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1

        # then put the key in its position
        numbers[j + 1] = key

    return numbers


# Example input list containing unsorted integers
numbers: list[int] = [25, 9, 53, 62, 54, 45]


# Execute insertion sort and print the resulting sorted list
print(insertion_sort(numbers=numbers))
