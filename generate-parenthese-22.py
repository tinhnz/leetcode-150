"""
Quite difficult to figure out the conditions in the recursive loop.
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(l, r, p):
            if l == r and l == 0:
                result.append("".join(p))

            if r < l:
                return

            if l > 0:
                p.append("(")
                backtrack(l - 1, r, p)
                p.pop()

            if r > 0:
                p.append(")")
                backtrack(l, r - 1, p)
                p.pop()

        result = []
        backtrack(n, n, [])
        return result
