class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(index, target, numbers):
            if target == 0:
                result.append(numbers.copy())
                return

            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    return

                numbers.append(candidates[i])
                backtrack(i, target - candidates[i], numbers)
                numbers.pop()

        candidates.sort()
        result = []
        backtrack(0, target, [])
        return result
