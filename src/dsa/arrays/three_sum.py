"""Problem: 3Sum (LeetCode #15).

Given an integer array `numbers`, return all the triplets
`[numbers[i], numbers[j], numbers[k]]` such that `i != j`, `i != k`, and
`j != k`, and `numbers[i] + numbers[j] + numbers[k] == 0`.

The solution set must not contain duplicate triplets.

Examples:
    Input:  numbers = [2, -2, 0, 3, -3, 5]
    Output: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]

    Input:  numbers = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]

    Input:  numbers = [0, 1, 1]
    Output: []

    Input:  numbers = [0, 0, 0]
    Output: [[0, 0, 0]]

Algorithm Strategies:
---------------------
1. Brute Force (`threeSumBruteForce`):
   - Three nested loops checking every distinct triplet (i, j, k).
   - If numbers[i] + numbers[j] + numbers[k] == 0, record triplet.
   - Time Complexity: O(N^3).
   - Auxiliary Space: O(1) (excluding output list).

2. Better Approach - Two Sum Reduction (`threeSumTwoSumApproach`):
   - Reformulate a + b + c = 0 into b + c = -a.
   - Fix the first element a = numbers[i], then reduce the remaining problem
     to Two Sum with target = -a using a lookup container `seen`.
   - Time Complexity: O(N^2).
   - Auxiliary Space: O(N) to store seen elements per outer iteration.

3. Optimal Approach - Two Pointers (`threeSumTwoPointerApproach`):
   - Sort the array first: O(N log N).
   - Fix first element `numbers[i]`. If `numbers[i] == numbers[i - 1]`, skip to
     avoid duplicate triplets.
   - Use two converging pointers: `left = i + 1`, `right = len(numbers) - 1`.
   - Calculate `total = numbers[i] + numbers[left] + numbers[right]`:
     - If total == 0: Found a valid triplet! Append to result.
       Advance left and decrement right while skipping adjacent duplicates.
     - If total < 0: Sum is too small; increment `left += 1`.
     - If total > 0: Sum is too large; decrement `right -= 1`.
   - Time Complexity: O(N log N + N^2) = O(N^2).
   - Auxiliary Space: O(1) in-place pointers (excluding output list).

Step-by-Step Dry Run - Optimal (`numbers = [2, -2, 0, 3, -3, 5]`):
-------------------------------------------------------------------
1. Sort array: [-3, -2, 0, 2, 3, 5]
2. i = 0 (num = -3): left = 1 (-2), right = 5 (5)
   - total = -3 + (-2) + 5 = 0 -> Triplet: [-3, -2, 5]. right decrements to 4.
   - left = 1 (-2), right = 4 (3): total = -3 + (-2) + 3 = -2 < 0 -> left = 2.
   - left = 2 (0),  right = 4 (3): total = -3 + 0 + 3 = 0 -> Triplet: [-3, 0, 3].
     right decrements to 3.
   - left = 2 (0),  right = 3 (2): total = -3 + 0 + 2 = -1 < 0 -> left = 3.
   - left == right -> terminate inner loop.
3. i = 1 (num = -2): left = 2 (0), right = 5 (5)
   - total = -2 + 0 + 5 = 3 > 0 -> right = 4 (3).
   - total = -2 + 0 + 3 = 1 > 0 -> right = 3 (2).
   - total = -2 + 0 + 2 = 0     -> Triplet: [-2, 0, 2]. right = 2.
   - left == right -> terminate inner loop.
4. Subsequent iterations find no further zeroes.

Final Output: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]

Complexity Summary (Striver's DSA Hierarchy):
---------------------------------------------
1. Brute Force: O(N^3) time, O(1) auxiliary space.
2. Better (Hash Lookup): O(N^2) time, O(N) auxiliary space.
3. Optimal (Sorted Two Pointers): O(N^2) time, O(1) auxiliary space.
"""


class Solution:
    """Solution class providing 3Sum triplet finding algorithms."""

    def threeSumBruteForce(self, numbers: list):
        """Find triplets summing to 0 using three nested loops.

        Args:
            numbers: List of integers.

        Returns:
            List of triplets [a, b, c] summing to 0.
        """
        target = 0
        result = []

        # Three nested loops checking all possible triplet combinations
        for i in range(len(numbers) - 2):
            for j in range(i + 1, len(numbers) - 1):
                for k in range(j + 1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == target:
                        result.append([numbers[i], numbers[j], numbers[k]])

        return result

    def threeSumTwoSumApproach(self, numbers: list):
        """Find triplets summing to 0 by reducing to Two Sum (b + c = -a).

        Args:
            numbers: List of integers.

        Returns:
            List of triplets [a, b, c] summing to 0.
        """
        result = []

        # First step is to fix
        """a+b+c = 0 b+c =-a"""

        # Fix first element 'a' and search for pair 'b' and 'c'
        for i in range(len(numbers) - 2):
            target = -numbers[i]
            a = numbers[i]
            seen = []
            # Now find the other two elements
            for j in range(i + 1, len(numbers)):
                # find the complement
                b = numbers[j]
                c = target - numbers[j]

                # Check if complement was previously seen
                if c in seen:
                    result.append([a, b, c])

                seen.append(b)

        return result

    def threeSumTwoPointerApproach(self, numbers: list):
        """Find triplets summing to 0 using sorting and two converging pointers.

        Args:
            numbers: List of integers.

        Returns:
            List of unique triplets [a, b, c] summing to 0.
        """
        result = []

        # First sort the array in-place
        numbers.sort()

        # Fix the first element
        for i in range(len(numbers) - 2):
            left = i + 1
            right = len(numbers) - 1

            # Skip duplicate values for the first element to prevent duplicate triplets
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue

            # Two converging pointers searching for remaining sum
            while left < right:
                # find the total sum of the current triplet
                total = numbers[i] + numbers[left] + numbers[right]

                # Found valid triplet summing to zero
                if total == 0:
                    result.append([numbers[i], numbers[left], numbers[right]])

                    # Skip duplicate values for left and right pointers
                    while left < right and numbers[left] == numbers[left - 1]:
                        left += 1
                    while left < right and numbers[right] == numbers[right - 1]:
                        right -= 1

                # If sum is negative, advance left pointer to increase total
                if total < 0:
                    left+=1
                # If sum is positive (or zero post-match), decrement right pointer
                else:
                    right-=1

        return result


# Instantiate the solution class
solution = Solution()

# Example list of integers
numbers = [2, -2, 0, 3, -3, 5]

# Execute and print optimal two-pointer 3Sum results
# Expected: [[-3, -2, 5], [-3, 0, 3], [-2, 0, 2]]
print(solution.threeSumTwoPointerApproach(numbers=numbers))
