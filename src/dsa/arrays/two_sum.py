"""Problem: Two Sum (LeetCode #1).

Given an array of integers `numbers` and an integer `target`, return indices
of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

Examples:
    Input:  numbers = [2, 7, 11, 15], target = 9
    Output: [0, 1] (or (0, 1))
    Explanation: numbers[0] + numbers[1] == 2 + 7 == 9.

    Input:  numbers = [1, 6, 2, 10, 3], target = 13
    Output: (3, 4)
    Explanation: numbers[3] + numbers[4] == 10 + 3 == 13.

    Input:  numbers = [3, 3], target = 6
    Output: [0, 1]

Algorithm Strategies:
---------------------
1. Brute Force (`twoSum`):
   - Check all pairs (i, j) using nested loops where i < j.
   - If numbers[i] + numbers[j] == target, return [i, j].
   - Time Complexity: O(N^2) comparisons.
   - Auxiliary Space: O(1) memory.

2. Optimal Hash Map Approach (`twoSumOptimal`):
   - Maintain a dictionary `seen` mapping `element_value -> index`.
   - In a single pass, for each element at index `i`:
     - Calculate required addend: `complement = target - numbers[i]`.
     - If `complement` is already in `seen`:
       A valid pair is found! Return `(seen[complement], i)`.
     - Otherwise, store current element: `seen[numbers[i]] = i`.
   - Time Complexity: O(N) average single pass.
   - Auxiliary Space: O(N) for hash table storage.

Step-by-Step Dry Run - Optimal (`numbers = [1, 6, 2, 10, 3], target = 13`):
--------------------------------------------------------------------------
Initial: seen = {}
- i = 0 (num = 1):  complement = 13 - 1 = 12. 12 not in seen -> seen[1] = 0
- i = 1 (num = 6):  complement = 13 - 6 = 7.  7 not in seen  -> seen[6] = 1
- i = 2 (num = 2):  complement = 13 - 2 = 11. 11 not in seen -> seen[2] = 2
- i = 3 (num = 10): complement = 13 - 10 = 3. 3 not in seen  -> seen[10] = 3
- i = 4 (num = 3):  complement = 13 - 3 = 10. 10 IN SEEN!
                    Return (seen[10], 4) = (3, 4)
Final Return: (3, 4)

Complexity Comparison (Striver's DSA Hierarchy):
------------------------------------------------
1. Brute Force:
   - Nested loops checking every pair: O(N^2) time, O(1) space.
2. Better (Two Pointers with Sorting):
   - Sort pairs of (value, index) and use two converging pointers.
   - Time: O(N log N), Auxiliary Space: O(N).
3. Optimal (Hash Map Single Pass - Current Implementation):
   - Instant complement lookup in dictionary.
   - Time: O(N), Auxiliary Space: O(N).
"""


class Solution:
    """Solution class providing two-sum target matching algorithms."""

    def twoSum(self, numbers, target):
        """Find indices of two numbers adding to target using brute force.

        Args:
            numbers: List of integers.
            target: Integer target sum.

        Returns:
            List containing the two indices [i, j].
        """
        # Outer loop iterates through each element up to the second-to-last
        for i in range(len(numbers) - 1):
            # Inner loop checks every subsequent element to form distinct pairs
            for j in range(i + 1, len(numbers)):
                # Verify if current pair sums up to the target value
                if numbers[i] + numbers[j] == target:
                    indexes = [i, j]
                    return indexes

    def twoSumOptimal(self, numbers, target):
        """Find indices of two numbers adding to target using a hash map.

        Args:
            numbers: List of integers.
            target: Integer target sum.

        Returns:
            Tuple containing the two indices (first_index, second_index).
        """
        # Hash map storing seen values as keys and their 0-based indices as values
        seen = {}

        # Single linear scan through numbers list
        for i in range(len(numbers)):
            # Calculate the required complement value that pairs with numbers[i]
            complement = target - numbers[i]

            # If complement exists in hash map, target pair is identified
            if complement in seen:
                return seen[complement], i

            # Store current value and index for subsequent elements to lookup
            seen[numbers[i]] = i


# Instantiate the solution class
solution = Solution()

# Example list of numbers and target sum
numbers = [1, 6, 2, 10, 3]

# Execute and print optimal two-sum indices (Expected output: (3, 4))
print(solution.twoSumOptimal(numbers=numbers, target=13))
