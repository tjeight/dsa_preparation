"""Problem: Sort an Array Using Merge Sort (Divide and Conquer).

Merge Sort is an efficient, general-purpose, comparison-based sorting algorithm
based on the Divide and Conquer paradigm. It divides the input array into two
halves, calls itself recursively for the two halves, and then merges the two
sorted halves into a single sorted array.

Examples:
    [2, 58, 69, 35, 12, 45] -> [2, 12, 35, 45, 58, 69]
    [5, 4, 3, 2, 1]         -> [1, 2, 3, 4, 5]
    [1, 2, 3]               -> [1, 2, 3]
    [42]                    -> [42]
    []                      -> []

Divide and Conquer Strategy:
----------------------------
1. Divide:
   - Find the midpoint `middle = len(numbers) // 2`.
   - Partition the array into two sublists: `left = numbers[:middle]` and
     `right = numbers[middle:]`.

2. Conquer (Recursive Calls):
   - Recursively sort the left sublist: `merge_sort(left)`.
   - Recursively sort the right sublist: `merge_sort(right)`.
   - Base Case: When a list has length <= 1, it is already sorted by definition.

3. Combine (Two-Pointer Merge):
   - Traverse both sorted sublists with index pointers `i` and `j`.
   - Compare `left[i]` and `right[j]`, appending the smaller value to `result`.
   - Append any remaining elements using `result.extend()`.

Step-by-Step Recursion Tree (numbers = [2, 58, 69, 35, 12, 45]):
----------------------------------------------------------------
Division Phase:
                     [2, 58, 69, 35, 12, 45]
                           /         \
                  [2, 58, 69]       [35, 12, 45]
                    /     \           /      \
                  [2]   [58, 69]    [35]   [12, 45]
                         /    \             /    \
                       [58]   [69]        [12]   [45]

Merge Phase (Bottom-Up):
- merge([58], [69])       -> [58, 69]
- merge([2], [58, 69])    -> [2, 58, 69]
- merge([12], [45])       -> [12, 45]
- merge([35], [12, 45])   -> [12, 35, 45]
- merge([2, 58, 69], [12, 35, 45]):
  - Compare 2 vs 12  -> take 2  (i=1, j=0)
  - Compare 58 vs 12 -> take 12 (i=1, j=1)
  - Compare 58 vs 35 -> take 35 (i=1, j=2)
  - Compare 58 vs 45 -> take 45 (i=1, j=3, right exhausted)
  - Extend remaining left: [58, 69]
  -> Final Sorted List: [2, 12, 35, 45, 58, 69]

Complexity Analysis:
--------------------
- Time Complexity:
  - Recurrence Relation: T(N) = 2T(N / 2) + O(N)
  - By the Master Theorem (Case 2: a = 2, b = 2, f(N) = O(N)):
    T(N) = O(N log2(N))
  - Best Case:    O(N log N)
  - Average Case: O(N log N)
  - Worst Case:   O(N log N)
  Unlike QuickSort, MergeSort guarantees O(N log N) performance on all inputs.
- Auxiliary Space: O(N)
  - Merging two subarrays requires an auxiliary list to store merged elements.
  - Call stack depth is bounded by O(log N) frames.
- Stability:
  - When comparing `left[i]` and `right[j]`, using `<` places right duplicates
    before left duplicates. Using `<=` makes MergeSort strictly stable.

Real-World Applications:
------------------------
1. External Sorting: Sorting large datasets that exceed RAM capacity (e.g.
   disk/tape-based database indexes) via k-way external merge sort.
2. Linked Lists: Optimal O(N log N) time and O(1) auxiliary space sort for
   singly linked lists (no random access required, LeetCode 148).
3. Foundation of Timsort: Python's `sorted()` and `list.sort()` use Timsort,
   which is a hybrid of Merge Sort and Insertion Sort.
"""


def divide_array(numbers: list[int]):
    """Divide a list into two roughly equal left and right sublists."""
    # step first is to find the middle element
    middle = len(numbers) // 2

    # seperate the left part and right part
    left: list[int] = numbers[:middle]
    right: list[int] = numbers[middle:]

    return left, right


def sort_array(left: list[int], right: list[int]):
    """Merge two sorted sublists into a single sorted list using two pointers."""
    # Create a new array to store the sort
    result: list[int] = []

    # initialize the numbers
    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        # Simple check
        if left[i] < right[j]:
            # append the left
            result.append(left[i])
            i = i + 1
        else:
            # append the right list
            result.append(right[j])
            j = j + 1

    # Append remaining elements from either list
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(numbers: list[int]) -> list[int]:
    """Recursively sort a list of integers in ascending order using Merge Sort."""
    # Base Case: Single element or empty list is already sorted
    if len(numbers) <= 1:
        return numbers

    # Divide step: Split list into left and right halves
    left, right = divide_array(numbers=numbers)

    # recursively sort
    left = merge_sort(left)
    right = merge_sort(right)

    # Combine step: Merge sorted halves
    return sort_array(left=left, right=right)


# Example input list containing unsorted integers
numbers: list[int] = [2, 58, 69, 35, 12, 45]

# Execute merge sort and print the resulting sorted list
print(merge_sort(numbers=numbers))
