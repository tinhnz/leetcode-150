class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(step, permutation):
            if step == len(nums):
                result.append(permutation.copy())

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    permutation[step] = nums[i]
                    backtrack(step + 1, permutation)
                    used[i] = False

        result = []
        used = {i: False for i in range(len(nums))}
        backtrack(0, [0] * len(nums))
        return result
