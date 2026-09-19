# DSA Preparation Roadmap & Repository Progress

A progressive, structured roadmap to master Data Structures and Algorithms in Python, tracking completed modules and future milestones.

---

## 🧭 Repository Status Overview

- **[x] Star & Number Patterns**: 22 / 22 Completed ([`src/dsa/star_patterns/`](../src/dsa/star_patterns/README.md))
- **[x] Python Built-in Collections**: 5 / 5 Completed ([`src/dsa/collections/`](../src/dsa/collections/README.md))
- **[ ] Linear Data Structures**: Next Up (Arrays, Strings, Linked Lists, Stacks, Queues)
- **[ ] Non-Linear Data Structures**: Upcoming (Trees, BSTs, Heaps, Graphs, Tries, DSU)
- **[ ] Core Algorithmic Paradigms**: Upcoming (Sorting, Searching, Recursion & Backtracking, DP)
- **[ ] Interview Patterns**: Upcoming (Sliding Window, Two Pointers, Monotonic Stack, etc.)

---

## Phase 1: Foundations & Python Language Mechanics

### 1.1 Python Built-in Collections (`src/dsa/collections/`)
- [x] **Dynamic Arrays (`list.py`)**: Appending, pop, in-place Timsort, slicing, 2D grids
- [x] **Hash Maps (`dict.py`)**: Hash table mechanics, `.get()`, `.setdefault()`, view objects
- [x] **Hash Sets (`set.py`)**: Deduplication, $O(1)$ membership, Venn diagram operations
- [x] **Strings (`string.py`)**: Immutability, slicing, $O(n)$ `join` vs $O(n^2)$ loop concatenation, ASCII
- [x] **Tuples (`tuple.py`)**: Immutability, hashability, 2D coordinate keys for DP and graphs

### 1.2 Coordinate Geometry & Loop Intuition (`src/dsa/star_patterns/`)
- [x] **Patterns 1 to 6**: Square, right-angled triangles, numbered triangles, inverted forms
- [x] **Patterns 7 to 10**: Equilateral pyramids, inverted pyramids, diamond, half-diamond
- [x] **Patterns 11 to 16**: Binary triangle, number crowns/valleys, Floyd's triangle, alphabet triangles
- [x] **Patterns 17 to 22**: Palindrome pyramid, reverse alphabets, hollow diamond, butterfly, hollow square, concentric number spirals

### 1.3 Complexity Analysis (`notes/time_space_complexity.md`)
- [x] Big-O hierarchy ($O(1)$ through $O(n!)$)
- [x] CPython internal operational costs for all collections
- [x] 1-second online judge execution rules ($10^7$ operations in Python)

---

## Phase 2: Linear Data Structures

### 2.1 Arrays & Strings (`src/dsa/data_structures/arrays_and_strings/`)
- [ ] Prefix Sum arrays & Difference arrays
- [ ] Kadane's algorithm (Maximum Subarray Sum)
- [ ] Dutch National Flag algorithm (Sort 0s, 1s, 2s)
- [ ] Boyer-Moore Majority Voting algorithm

### 2.2 Linked Lists (`src/dsa/data_structures/linked_lists/`)
- [ ] Singly Linked List (insert, delete, search, reverse)
- [ ] Doubly Linked List & Circular Linked List
- [ ] Fast & Slow Pointers (Floyd's Tortoise & Hare cycle detection, middle node)
- [ ] In-place Linked List reversal & sublist reversal

### 2.3 Stacks & Queues (`src/dsa/data_structures/stacks_and_queues/`)
- [ ] Stack using list vs `collections.deque`
- [ ] Queue using `collections.deque`
- [ ] Monotonic Stack (Next Greater Element, Previous Smaller Element)
- [ ] Monotonic Queue (Sliding Window Maximum)
- [ ] Min Stack / Max Stack with $O(1)$ retrieval

---

## Phase 3: Non-Linear Data Structures

### 3.1 Trees & Binary Search Trees (`src/dsa/data_structures/trees/`)
- [ ] Binary Tree Traversals: In-order, Pre-order, Post-order (Recursive & Iterative)
- [ ] Level-Order Traversal (BFS) using deque
- [ ] Binary Search Tree (BST) insert, search, delete, validation
- [ ] Lowest Common Ancestor (LCA) in BT and BST
- [ ] Diameter, Height, and Balanced Binary Tree checks

### 3.2 Heaps & Priority Queues (`src/dsa/data_structures/heaps/`)
- [ ] Min-Heap & Max-Heap mechanics using Python's `heapq`
- [ ] Kth Largest / Smallest Element
- [ ] Two Heaps pattern (Find Median from Data Stream)

### 3.3 Hashing & Hash Tables (`src/dsa/data_structures/hashing/`)
- [ ] Collision resolution: Separate Chaining vs Open Addressing
- [ ] Custom Hash Map implementation from scratch

### 3.4 Disjoint Set Union (`src/dsa/data_structures/disjoint_set_union/`)
- [ ] Disjoint Set Union (DSU / Union-Find) with Path Compression and Union by Rank

### 3.5 Tries (`src/dsa/data_structures/tries/`)
- [ ] Prefix Tree (Trie) insert, search, and prefix matching
- [ ] Bitwise Trie (Maximum XOR of Two Numbers)

---

## Phase 4: Core Algorithmic Techniques

### 4.1 Searching & Sorting (`src/dsa/algorithms/`)
- [ ] Binary Search (classic, lower bound, upper bound, search on answer space)
- [ ] Sorting: Merge Sort, Quick Sort, Counting Sort
- [ ] Quickselect (finding Kth element in $O(n)$ average time)

### 4.2 Recursion & Backtracking
- [ ] Subsets & Subsequences
- [ ] Permutations & Combinations
- [ ] N-Queens, Sudoku Solver, Word Search

### 4.3 Graph Algorithms (`src/dsa/algorithms/graph_algorithms/`)
- [ ] Breadth-First Search (BFS) & Depth-First Search (DFS)
- [ ] Cycle Detection in Directed & Undirected Graphs
- [ ] Topological Sort (Kahn's BFS algorithm and DFS)
- [ ] Dijkstra's Shortest Path Algorithm (using `heapq`)
- [ ] Bellman-Ford & Floyd-Warshall Algorithms
- [ ] Minimum Spanning Tree: Kruskal's (with DSU) & Prim's

### 4.4 Dynamic Programming (`src/dsa/algorithms/dynamic_programming/`)
- [ ] 1D DP: Climbing Stairs, Fibonacci, House Robber
- [ ] 2D / Grid DP: Unique Paths, Minimum Path Sum
- [ ] 0/1 Knapsack & Unbounded Knapsack
- [ ] Longest Common Subsequence (LCS) & Edit Distance
- [ ] Longest Increasing Subsequence (LIS) ($O(n \log n)$ with binary search)
- [ ] Interval DP & Bitmask DP
