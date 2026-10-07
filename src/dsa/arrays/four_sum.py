"""Problem: 4Sum (LeetCode #18).

Given an array `numbers` of `n` integers and an integer `target`, return an array
of all the unique quadruplets `[numbers[a], numbers[b], numbers[c], numbers[d]]`
such that:
1. `0 <= a, b, c, d < n` are distinct indices.
2. `numbers[a] + numbers[b] + numbers[c] + numbers[d] == target`.
3. The solution set must not contain duplicate quadruplets.

Examples:
    Input:  numbers = [1, -2, 3, 5, 7, 9], target = 7
    Output: [[-2, 1, 3, 5]]
    Explanation: -2 + 1 + 3 + 5 == 7.

    Input:  numbers = [1, 0, -1, 0, -2, 2], target = 0
    Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    Input:  numbers = [2, 2, 2, 2, 2], target = 8
    Output: [[2, 2, 2, 2]]

Algorithm Strategy (Sorting + Two Fixed Loops + Two Pointers):
--------------------------------------------------------------
1. Sort Array:
   - Sort `numbers` in non-decreasing order: O(N log N).
   - Enables efficient duplicate skipping and monotonic two-pointer convergence.
2. First Fixed Loop (i from 0 to N - 4):
   - Fix first element `fixed = numbers[i]`.
   - Remaining target: `new_target = target - fixed`.
   - Deduplication: `if i > 0 and numbers[i] == numbers[i - 1]: continue`.
3. Second Fixed Loop (j from i + 1 to N - 3):
   - Fix second element `numbers[j]`.
   - Deduplication: `if j > i + 1 and numbers[j] == numbers[j - 1]: continue`.
4. Two Converging Pointers (left = j + 1, right = N - 1):
   - Calculate `total = numbers[j] + numbers[left] + numbers[right]`:
     - If `total == new_target`:
       Valid quadruplet found!
       Append `[fixed, numbers[j], numbers[left], numbers[right]]`.
       Advance `left += 1`, decrement `right -= 1`.
       Skip duplicate left values: `numbers[left] == numbers[left - 1]`.
       Skip duplicate right values: `numbers[right] == numbers[right + 1]`.
     - If `total < new_target`:
       Sum is too small; increment `left += 1`.
     - Else (`total > new_target`):
       Sum is too large; decrement `right -= 1`.
5. Return all collected unique quadruplets.

Step-by-Step Dry Run (numbers = [1, -2, 3, 5, 7, 9], target = 7):
-------------------------------------------------------------------
1. Sorted: [-2, 1, 3, 5, 7, 9], N = 6
2. i = 0 (fixed = -2), new_target = 7 - (-2) = 9
   - j = 1 (numbers[1] = 1):
     - left = 2 (3), right = 5 (9): total = 1+3+9 = 13 > 9 -> right = 4 (7)
     - left = 2 (3), right = 4 (7): total = 1+3+7 = 11 > 9 -> right = 3 (5)
     - left = 2 (3), right = 3 (5): total = 1+3+5 = 9 == 9 -> Match!
       Quadruplet: [-2, 1, 3, 5]
       left = 3, right = 2 -> pointers cross, terminate.
   - j = 2 (numbers[2] = 3): left = 3 (5), right = 5 (9)
     - total = 3+5+9 = 17 > 9 -> right = 4 (7)
     - total = 3+5+7 = 15 > 9 -> right = 3 (5)
     - pointers meet, terminate.
3. Subsequent fixed elements produce sums > 7.
Final Result: [[-2, 1, 3, 5]]

Complexity Analysis:
--------------------
- Time Complexity: O(N^3)
  - Sorting takes O(N log N).
  - Outer loop i runs O(N) times.
  - Inner loop j runs O(N) times.
  - Two-pointer while loop runs O(N) times for each pair (i, j).
  - Total Time: O(N log N + N * N * N) = O(N^3).
- Auxiliary Space: O(1) (excluding output list)
  - Modifies only pointer indices `i`, `j`, `left`, `right`.
  - In-place deduplication avoids extra hash set allocations.

Comparison of Approaches (Striver's DSA Hierarchy):
---------------------------------------------------
1. Brute Force (4 Nested Loops):
   - Check all 4-tuples, insert into set to deduplicate.
   - Time: O(N^4), Auxiliary Space: O(quadruplets).
2. Better Approach (3 Nested Loops + Hash Set):
   - Fix 3 elements, look up 4th in hash set.
   - Time: O(N^3), Auxiliary Space: O(N).
3. Optimal Approach (2 Nested Loops + Two Pointers - Current):
   - Fix 2 elements, search remaining 2 with converging two pointers.
   - In-place duplicate skipping.
   - Time: O(N^3), Auxiliary Space: O(1).
"""


class Solution:
    """Solution class providing 4Sum quadruplet finding algorithms."""

    def fourSum(self, numbers, target):
        """Find all unique quadruplets summing to target.

        Args:
            numbers: List of integers.
            target: Integer target sum.

        Returns:
            List of unique quadruplets [a, b, c, d] summing to target.
        """
        # Sort array in-place to enable two-pointer traversal and deduplication
        numbers.sort()
        result = []

        # First fixed pointer
        for i in range(len(numbers) - 3):
            # Skip duplicate first values
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            fixed = numbers[i]
            new_target = target - fixed

            # Second fixed pointer
            for j in range(i + 1, len(numbers) - 2):
                # Skip duplicate second values
                if j > i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                # Initialize two converging pointers for the remaining pair
                left = j + 1
                right = len(numbers) - 1

                while left < right:
                    total = numbers[j] + numbers[left] + numbers[right]

                    # Found valid quadruplet
                    if total == new_target:
                        result.append(
                            [fixed, numbers[j], numbers[left], numbers[right]]
                        )

                        # Move away from current pair
                        left += 1
                        right -= 1

                        # Skip duplicate left values
                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1

                        # Skip duplicate right values
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1

                    # Sum too small; advance left pointer
                    elif total < new_target:
                        left += 1

                    # Sum too large; decrement right pointer
                    else:
                        right -= 1

        return result


# Example list of numbers and target sum
numbers = [1, -2, 3, 5, 7, 9]
target = 7

# Instantiate the solution class
solution = Solution()

# Execute and print unique 4Sum quadruplets (Expected: [[-2, 1, 3, 5]])
print(solution.fourSum(numbers=numbers, target=target))
