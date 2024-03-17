"""
Use the built-in List method copy() when appending a combination into the result.
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(step, lower, combination):
            if step == k:
                result.append(combination.copy())
                return

            for v in range(lower, n + 1):
                combination[step] = v
                backtrack(step + 1, v + 1, combination)

        result = []
        backtrack(0, 1, [1] * k)
        return result
