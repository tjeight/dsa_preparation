"""Problem: Majority Element (> N/2 times) (LeetCode #169).

Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears strictly more than
`⌊n / 2⌋` times. You may assume that the majority element always exists
in the array.

Examples:
    Input:  nums = [3, 2, 3]
    Output: 3 (n = 3, threshold = 1, appears 2 times)

    Input:  nums = [2, 2, 1, 1, 1, 2, 2]
    Output: 2 (n = 7, threshold = 3, appears 4 times)

    Input:  nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
    Output: 7 (n = 9, threshold = 4, appears 5 times)

Algorithm Strategies:
---------------------
1. Better Approach: Hash Map Frequency Counter (`findMajorityElement`)
   - Maintain a frequency dictionary `count`.
   - Increment count for each number encountered.
   - Early Exit: As soon as `count[num] > len(nums) // 2`, return `num`.
   - Time Complexity: O(N) average.
   - Auxiliary Space: O(N) to store frequencies of distinct elements.

2. Optimal Approach: Boyer-Moore Voting Algorithm (`findMajorityByBoyeMore`)
   - Proposed by Robert S. Boyer and J Strother Moore in 1981.
   - Core Intuition (Vote Cancellation):
     - The majority element occurs strictly more than all other elements combined.
     - Pair up different elements and cancel them out. Since the majority element
       count exceeds N/2, it will survive the cancellations.
   - Two State Variables:
     - `candidate`: Presumed majority element.
     - `count`: Net balance / vote count for `candidate`.
   - Algorithm Steps:
     - When `count == 0`, elect current `num` as the new `candidate`.
     - If current `num == candidate`, increment `count += 1`.
     - Else, decrement `count -= 1` (opposing vote).
   - Time Complexity: O(N) single pass.
   - Auxiliary Space: O(1) strictly scalar variables.

Step-by-Step Dry Run - Boyer-Moore (nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]):
-------------------------------------------------------------------------
N = 9, Threshold = 9 // 2 = 4 (majority requires >= 5 votes).
- Initial: count = 0, candidate = None
- num = 7: count was 0 -> candidate = 7; matches candidate -> count = 1
- num = 0: 0 != 7 (opposing vote) -> count = 0
- num = 0: count was 0 -> candidate = 0; matches candidate -> count = 1
- num = 1: 1 != 0 (opposing vote) -> count = 0
- num = 7: count was 0 -> candidate = 7; matches candidate -> count = 1
- num = 7: matches candidate -> count = 2
- num = 2: 2 != 7 (opposing vote) -> count = 1
- num = 7: matches candidate -> count = 2
- num = 7: matches candidate -> count = 3
Final Return: candidate = 7

Complexity Comparison (Striver's DSA Hierarchy):
------------------------------------------------
1. Brute Force:
   - Count frequencies using nested loops: O(N^2) time, O(1) space.
2. Better (Hash Map):
   - Frequency map with early exit: O(N) time, O(N) space.
3. Optimal (Boyer-Moore Voting):
   - In-place cancellation: O(N) time, O(1) space.
"""


class Solution:
    """Solution class providing majority element finding algorithms."""

    def findMajorityElement(self, nums1):
        """Find majority element using a hash map frequency counter.

        Args:
            nums1: List of integers containing a majority element.

        Returns:
            The integer element appearing strictly more than n // 2 times.
        """
        count = {}

        for num in nums1:
            count[num] = count.get(num, 0) + 1

            # Early exit: return as soon as frequency exceeds n // 2
            if count[num] > len(nums1) // 2:
                return num

    def findMajorityByBoyeMore(self, nums):
        """Find majority element using the Boyer-Moore Voting Algorithm.

        Args:
            nums: List of integers containing a majority element.

        Returns:
            The majority candidate that survived all pairwise cancellations.
        """
        count = 0
        candidate = None
        for num in nums:
            # When balance reaches 0, elect current element as new candidate
            if count == 0:
                candidate = num
            # Support or oppose the candidate
            if candidate == num:
                count+=1
            else :
                count-=1

        return candidate


# Instantiate the solution class
solution = Solution()

# Example input array (n = 9, majority element 7 appears 5 times)
nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]

# Execute and print results from both approaches (Expected output: 7 for both)
print(solution.findMajorityElement(nums1=nums))
print(solution.findMajorityByBoyeMore(nums=nums))
