"""
Kadane's algorithm.
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