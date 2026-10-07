# Repository Progress Tracker

A living inventory of modules, topics, code files, and documentation in this repository.

Last Updated: September 2026

---

## 📊 Summary Dashboard

| Topic Category | Location | Files Count | Status | Notes / README |
| :--- | :--- | :---: | :---: | :--- |
| **Star & Number Patterns** | `src/dsa/star_patterns/` | 22 | ✅ Complete | [README.md](../src/dsa/star_patterns/README.md) |
| **Python Collections** | `src/dsa/collections/` | 5 | ✅ Complete | [README.md](../src/dsa/collections/README.md) |
| **Basic Mathematics** | `src/dsa/basic_math/` | 7 | ✅ Complete | [README.md](../src/dsa/basic_math/README.md) |
| **Recursion Foundations** | `src/dsa/recursion/` | 14 | 🟡 In Progress | [README.md](../src/dsa/recursion/README.md) |
| **Sorting Algorithms** | `src/dsa/algorithms/sorting/` | 10 | 🟡 In Progress | [README.md](../src/dsa/algorithms/sorting/README.md) |
| **Complexity Reference** | `notes/` | 1 | ✅ Complete | [time_space_complexity.md](time_space_complexity.md) |
| **Standard Library Cheatsheet** | `notes/` | 1 | ✅ Complete | [python_dsa_cheatsheet.md](python_dsa_cheatsheet.md) |
| **Problem Solving Patterns** | `notes/` | 1 | ✅ Complete | [problem_solving_patterns.md](problem_solving_patterns.md) |
| **Arrays** | `src/dsa/arrays/` | 3 | 🟡 In Progress | Linear search, largest & 2nd largest |
| **Searching Algorithms** | `src/dsa/algorithms/searching/` | 0 | ⏳ Upcoming | To be added when covered |
| **Linked Lists** | `src/dsa/data_structures/linked_lists/` | 0 | ⏳ Upcoming | To be added when covered |
| **Stacks & Queues** | `src/dsa/data_structures/stacks_and_queues/` | 0 | ⏳ Upcoming | To be added when covered |
| **Trees & BSTs** | `src/dsa/data_structures/trees/` | 0 | ⏳ Upcoming | To be added when covered |
| **Heaps & Priority Queues** | `src/dsa/data_structures/heaps/` | 0 | ⏳ Upcoming | To be added when covered |
| **Graphs** | `src/dsa/data_structures/graphs/` | 0 | ⏳ Upcoming | To be added when covered |
| **Dynamic Programming** | `src/dsa/algorithms/dynamic_programming/` | 0 | ⏳ Upcoming | To be added when covered |

---

## 📁 Detailed Breakdown of Completed Modules

### 1. Built-in Collections (`src/dsa/collections/`)
All five foundational data structures are documented with Big-O complexities and annotated examples:
- [x] [`list.py`](../src/dsa/collections/list.py): Dynamic array operations, in-place sorting, shallow slicing, list comprehensions, 2D matrices.
- [x] [`dict.py`](../src/dsa/collections/dict.py): Hash map mechanics, `get()`, `setdefault()`, `popitem()`, view objects, hash collisions.
- [x] [`set.py`](../src/dsa/collections/set.py): Hash set mechanics, deduplication, $O(1)$ lookups, `remove` vs `discard`, set arithmetic.
- [x] [`string.py`](../src/dsa/collections/string.py): Immutability, slicing, $O(n)$ `join()` vs $O(n^2)$ loop concatenation, ASCII encoding.
- [x] [`tuple.py`](../src/dsa/collections/tuple.py): Immutable sequences, single-element tuple syntax, packing/unpacking, hashable 2D coordinate keys for memoization.
- [x] [`README.md`](../src/dsa/collections/README.md): Cross-collection comparison matrix, decision flowchart, and Big-O lookup table.

### 2. Star & Number Patterns (`src/dsa/star_patterns/`)
All 22 Striver-style foundational pattern problems implemented and documented:
- [x] [`pattern1.py`](../src/dsa/star_patterns/pattern1.py) to [`pattern6.py`](../src/dsa/star_patterns/pattern6.py): Basic squares and right triangles.
- [x] [`pattern7.py`](../src/dsa/star_patterns/pattern7.py) to [`pattern10.py`](../src/dsa/star_patterns/pattern10.py): Full pyramids, inverted pyramids, diamonds, half-diamonds.
- [x] [`pattern11.py`](../src/dsa/star_patterns/pattern11.py) to [`pattern16.py`](../src/dsa/star_patterns/pattern16.py): Binary triangle, number valleys, Floyd's triangle, character triangles.
- [x] [`pattern17.py`](../src/dsa/star_patterns/pattern17.py) to [`pattern22.py`](../src/dsa/star_patterns/pattern22.py): Palindrome pyramid, reverse alphabets, hollow diamond, butterfly, hollow square, concentric number spirals.
- [x] [`README.md`](../src/dsa/star_patterns/README.md): The 4 Golden Rules of Pattern Solving and ASCII breakdowns for all 22 patterns.

### 3. Basic Mathematics (`src/dsa/basic_math/`)
Seven core number-theory algorithms implemented, verified, and documented:
- [x] [`count_digits.py`](../src/dsa/basic_math/count_digits.py): Iterative division vs logarithmic formula $\lfloor \log_{10} N \rfloor + 1$.
- [x] [`reverse_number.py`](../src/dsa/basic_math/reverse_number.py): Modulo digit extraction `% 10` and base-10 accumulation `rev * 10 + rem`.
- [x] [`palindrome_number.py`](../src/dsa/basic_math/palindrome_number.py): Integer symmetry verification, negative numbers, and trailing zeros.
- [x] [`gcd.py`](../src/dsa/basic_math/gcd.py): Euclidean Algorithm by modulo division $\gcd(b, a \pmod b)$ and LCM relation.
- [x] [`armstrong.py`](../src/dsa/basic_math/armstrong.py): Narcissistic number verification $\sum d_i^k = N$.
- [x] [`all_divisors.py`](../src/dsa/basic_math/all_divisors.py): Conjugate factor pairs up to $\lfloor\sqrt{N}\rfloor$ with deduplication.
- [x] [`prime.py`](../src/dsa/basic_math/prime.py): Primality trial division up to $\lfloor\sqrt{N}\rfloor$ with mathematical proof.
- [x] [`README.md`](../src/dsa/basic_math/README.md): Formula reference, comparison table, and problem breakdowns.

### 4. Recursion Fundamentals (`src/dsa/recursion/`)
- [x] [`print_n_times.py`](../src/dsa/recursion/print_n_times.py): The 3 pillars of recursion (base case, work, recursive call) and call stack trace.
- [x] [`print_name_n_times.py`](../src/dsa/recursion/print_name_n_times.py): Parameterized recursion tracking iteration counts.
- [x] [`print_1_to_n.py`](../src/dsa/recursion/print_1_to_n.py): Ascending print order via recursive counter.
- [x] [`print_n_to_1.py`](../src/dsa/recursion/print_n_to_1.py): Descending print countdown recursion.
- [x] [`sum_of_n.py`](../src/dsa/recursion/sum_of_n.py): Functional recursion returning accumulated subproblem sums $N + \text{sum}(N-1)$.
- [x] [`factorial.py`](../src/dsa/recursion/factorial.py): Functional multiplication recursion $N \times \text{fact}(N-1)$.
- [x] [`sum_of_array_elements.py`](../src/dsa/recursion/sum_of_array_elements.py): Array summation via tail slicing and pointer optimization.
- [x] [`reverse_string.py`](../src/dsa/recursion/reverse_string.py): String reversal via end-character extraction and recursion.
- [x] [`reverse_array.py`](../src/dsa/recursion/reverse_array.py): In-place array reversal using converging two-pointer swaps.
- [x] [`check_palindrome.py`](../src/dsa/recursion/check_palindrome.py): String palindrome check using reverse string comparison.
- [x] [`check_palindrome_two_pointer.py`](../src/dsa/recursion/check_palindrome_two_pointer.py): Palindrome check by recursive boundary comparison.
- [x] [`check_prime.py`](../src/dsa/recursion/check_prime.py): Primality verification via countdown trial division.
- [x] [`is_sorted.py`](../src/dsa/recursion/is_sorted.py): Array sort order verification via recursive tail slicing and pointer optimization.
- [x] [`sum_of_digits.py`](../src/dsa/recursion/sum_of_digits.py): Digit sum extraction via modulo and integer division functional recursion.
- [ ] Multiple recursive calls (Fibonacci numbers).
- [ ] Subsequences generation and backtracking.

### 5. Sorting Algorithms (`src/dsa/algorithms/sorting/`)
- Core Sorting Implementations:
  - [x] [`selection_sort.py`](../src/dsa/algorithms/sorting/selection_sort.py): In-place comparison sort via minimum element placement ($O(N^2)$ time, $O(1)$ space).
  - [x] [`bubble_sort.py`](../src/dsa/algorithms/sorting/bubble_sort.py): In-place adjacent comparison and bubbling up of maximum elements ($O(N^2)$ time, $O(1)$ space).
  - [x] [`insertion_sort.py`](../src/dsa/algorithms/sorting/insertion_sort.py): In-place incremental insertion with backward shifting ($O(N^2)$ worst, $O(N)$ best, $O(1)$ space).
  - [x] [`merge_sort.py`](../src/dsa/algorithms/sorting/merge_sort.py): Divide and conquer recursive array partitioning and two-pointer merging ($O(N \log N)$ time, $O(N)$ space).
  - [x] [`quick_sort.py`](../src/dsa/algorithms/sorting/quick_sort.py): Divide and conquer partition sorting via Lomuto pivot placement ($O(N \log N)$ average, $O(N^2)$ worst).
- Pseudocode & Algorithmic Reference Modules:
  - [x] [`selection_sort_pseudo_code.py`](../src/dsa/algorithms/sorting/selection_sort_pseudo_code.py): Formal textbook pseudocode, line-by-line analysis, and reference implementation.
  - [x] [`bubble_sort_pseudo_code.py`](../src/dsa/algorithms/sorting/bubble_sort_pseudo_code.py): Optimized pseudocode with early exit flag and line-by-line breakdown.
  - [x] [`insertion_sort_pseudo_code.py`](../src/dsa/algorithms/sorting/insertion_sort_pseudo_code.py): Standard CLRS pseudocode, shifting logic, and reference implementation.
  - [x] [`merge_sort_pseudo_code.py`](../src/dsa/algorithms/sorting/merge_sort_pseudo_code.py): Divide & conquer pseudocode with two-pointer merge subroutine.
  - [x] [`quick_sort_pseudo_code.py`](../src/dsa/algorithms/sorting/quick_sort_pseudo_code.py): Lomuto partitioning pseudocode and in-place divide & conquer breakdown.

### 6. Arrays & Linear Problems (`src/dsa/arrays/`)
- [x] [`linear_search.py`](../src/dsa/arrays/linear_search.py): Sequential search with early exit on target match ($O(N)$ worst, $O(1)$ best, $O(1)$ space).
- [x] [`largest_element.py`](../src/dsa/arrays/largest_element.py): Single-pass linear scan to determine array maximum ($O(N)$ time, $O(1)$ space).
- [x] [`second_largest_element.py`](../src/dsa/arrays/second_largest_element.py): Single-pass dual tracker finding second largest distinct value ($O(N)$ time, $O(1)$ space).
- [x] [`consecutive_ones.py`](../src/dsa/arrays/consecutive_ones.py): Single-pass linear scan counting maximum consecutive 1s with streak reset ($O(N)$ time, $O(1)$ space).
- [x] [`rotate_array_left_one.py`](../src/dsa/arrays/rotate_array_left_one.py): In-place left rotation by one position using element buffering and shift loop ($O(N)$ time, $O(1)$ space).
- [x] [`rotate_array_by_k_postions.py`](../src/dsa/arrays/rotate_array_by_k_postions.py): Left rotation by $k$ positions using modulo reduction and temporary slice buffer ($O(N)$ time, $O(k)$ space).
- [x] [`move_zeroes_to_end.py`](../src/dsa/arrays/move_zeroes_to_end.py): In-place two-pointer partition moving zeroes to array end while preserving element order ($O(N)$ time, $O(1)$ space).
- [x] [`remove_duplicates.py`](../src/dsa/arrays/remove_duplicates.py): In-place two-pointer deduplication of sorted array overwriting duplicates ($O(N)$ time, $O(1)$ space).
- [x] [`find_missing_number.py`](../src/dsa/arrays/find_missing_number.py): Gauss's summation formula determining missing element in $[0, n]$ ($O(N)$ time, $O(1)$ space).
- [x] [`union_array.py`](../src/dsa/arrays/union_array.py): Two-pointer linear merge of two sorted arrays with tail deduplication ($O(N + M)$ time, $O(1)$ auxiliary space).
- [x] [`intersection_of_arrays.py`](../src/dsa/arrays/intersection_of_arrays.py): Two-pointer linear scan finding common elements in sorted arrays ($O(N + M)$ time, $O(1)$ auxiliary space).
- [x] [`majority_element.py`](../src/dsa/arrays/majority_element.py): Majority element detection via Hash Map ($O(N)$ space) and Boyer-Moore Voting Algorithm ($O(1)$ space).
- [x] [`leaders.py`](../src/dsa/arrays/leaders.py): Optimal right-to-left linear scan tracking suffix maximum to identify leaders ($O(N)$ time, $O(1)$ auxiliary space).
- [x] [`sort_positive_and_negative.py`](../src/dsa/arrays/sort_positive_and_negative.py): Rearrange array in alternating positive and negative order using two-list segregation ($O(N)$ time, $O(N)$ space).
- [x] [`spiral_matrix.py`](../src/dsa/arrays/spiral_matrix.py): Clockwise spiral traversal of 2D matrix using 4-boundary shrinking loop ($O(M \times N)$ time, $O(1)$ auxiliary space).
- [x] [`pascal_triangle.py`](../src/dsa/arrays/pascal_triangle.py): Dynamic programming construction of Pascal's triangle row by row ($O(N^2)$ time, $O(N^2)$ space).
- [x] [`pascal_traingle_first_problem.py`](../src/dsa/arrays/pascal_traingle_first_problem.py): Pascal's Triangle Variation 1: Query element at $(r, c)$ using full row generation and 0-based indexing ($O(R^2)$ time, $O(R^2)$ space).
- [x] [`pascal_triangle_generate_nth_row.py`](../src/dsa/arrays/pascal_triangle_generate_nth_row.py): Pascal's Triangle Variation 2: Space-optimized iterative generation of $n$-th row ($O(R^2)$ time, $O(R)$ space).
- [x] [`rotate_matrix_by_90.py`](../src/dsa/arrays/rotate_matrix_by_90.py): In-place 90-degree clockwise matrix rotation via diagonal transposition and row reversal ($O(N^2)$ time, $O(1)$ space).
- [x] [`set_matrix_zeroes.py`](../src/dsa/arrays/set_matrix_zeroes.py): Set matrix zeroes using reference snapshot copy to prevent cascading zeroes ($O(M \times N \times (M + N))$ time, $O(M \times N)$ space).
- [x] [`two_sum.py`](../src/dsa/arrays/two_sum.py): Find two indices summing to target via Brute Force ($O(N^2)$ time) and Optimal Hash Map ($O(N)$ time, $O(N)$ space).
- [x] [`three_sum.py`](../src/dsa/arrays/three_sum.py): 3Sum unique triplets via Brute Force ($O(N^3)$), Hash Lookup ($O(N^2)$), and Sorted Two Pointers ($O(N^2)$ time, $O(1)$ space).
- [x] [`four_sum.py`](../src/dsa/arrays/four_sum.py): 4Sum unique quadruplets via sorting, two fixed pointer loops, and converging two pointers ($O(N^3)$ time, $O(1)$ space).

---

## 🎯 Next Recommended Steps
1. Complete Recursion Foundations:
   - Print 1 to N and N to 1
   - Sum of first N numbers & Factorial
   - Reverse an array / string using recursion
2. Implement Linear Data Structures:
   - Singly Linked List with node definition, insert, delete, and reverse.
   - Stack and Queue using `collections.deque`.
3. Start the Two Pointers pattern (`src/dsa/patterns/two_pointers/`):
   - Two Sum II (Sorted Array)
   - 3Sum
   - Container With Most Water
