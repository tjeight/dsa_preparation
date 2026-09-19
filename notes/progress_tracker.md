# Repository Progress Tracker

A living inventory of modules, topics, code files, and documentation in this repository.

Last Updated: September 2026

---

## 📊 Summary Dashboard

| Topic Category | Location | Files Count | Status | Notes / README |
| :--- | :--- | :---: | :---: | :--- |
| **Star & Number Patterns** | `src/dsa/star_patterns/` | 22 | ✅ Complete | [README.md](../src/dsa/star_patterns/README.md) |
| **Python Collections** | `src/dsa/collections/` | 5 | ✅ Complete | [README.md](../src/dsa/collections/README.md) |
| **Complexity Reference** | `notes/` | 1 | ✅ Complete | [time_space_complexity.md](time_space_complexity.md) |
| **Standard Library Cheatsheet** | `notes/` | 1 | ✅ Complete | [python_dsa_cheatsheet.md](python_dsa_cheatsheet.md) |
| **Problem Solving Patterns** | `notes/` | 1 | ✅ Complete | [problem_solving_patterns.md](problem_solving_patterns.md) |
| **Arrays & Strings** | `src/dsa/data_structures/arrays_and_strings/` | 0 | ⏳ Ready | Folder initialized |
| **Linked Lists** | `src/dsa/data_structures/linked_lists/` | 0 | ⏳ Ready | Folder initialized |
| **Stacks & Queues** | `src/dsa/data_structures/stacks_and_queues/` | 0 | ⏳ Ready | Folder initialized |
| **Trees & BSTs** | `src/dsa/data_structures/trees/` | 0 | ⏳ Ready | Folder initialized |
| **Heaps & Priority Queues** | `src/dsa/data_structures/heaps/` | 0 | ⏳ Ready | Folder initialized |
| **Graphs** | `src/dsa/data_structures/graphs/` | 0 | ⏳ Ready | Folder initialized |
| **Sorting Algorithms** | `src/dsa/algorithms/sorting/` | 0 | ⏳ Ready | Folder initialized |
| **Searching Algorithms** | `src/dsa/algorithms/searching/` | 0 | ⏳ Ready | Folder initialized |
| **Dynamic Programming** | `src/dsa/algorithms/dynamic_programming/` | 0 | ⏳ Ready | Folder initialized |

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

---

## 🎯 Next Recommended Steps
1. Implement Linear Data Structures:
   - Singly Linked List with node definition, insert, delete, and reverse.
   - Stack and Queue using `collections.deque`.
2. Start the Two Pointers pattern (`src/dsa/patterns/two_pointers/`):
   - Two Sum II (Sorted Array)
   - 3Sum
   - Container With Most Water
