"""
Kadane's algorithm.
Nice solution: https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            if curSum < 0:
                curSum = 0

            curSum += n
            maxSum = max(curSum, maxSum)

        return maxSum
