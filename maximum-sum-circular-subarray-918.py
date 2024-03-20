"""
Can't solve by myself. We have A = B + C, where:

- A is the original array.
- B is the elements that make up Maximum Sub Array.
- C are the elements that make up Minimum Sub Array.

There are 2 cases:

- c .. c [b .. b] c..c (B divides C into 2 halves).
- b .. b [c .. c] b..b (C divides B into 2 halves).

Call S1 is the maxSum of case 1, S2 is the maxSum of case 2.
For S1 we use normal Kadane to calculate. For S2, we use similar
method but to calculate minSum. Then S2 = totalSum - minSum.
The result will be MAX(S1, S2). Both S1 and S2 can be retrieved in one loop.

Another important point is that A can be all negatives.
And in this case, S1 will be the minimum element in A (and also
less than zero). And S1 also the final result in this edge case.
(Easy to see that sum of any 2 elements will be less than the smallest element)

https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/3066058/c-easy-solution-with-explaination-in-o-n-time-complexity
"""


class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        maxSum = minSum = nums[0]
        curMax = curMin = 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
