class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit2letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(step, chars):
            if step == len(digits):
                words.append("".join(chars))
                return

            for c in digit2letter[digits[step]]:
                chars[step] = c
                backtrack(step + 1, chars)

        if not digits:
            return []

        words = []
        chars = [""] * len(digits)
        backtrack(0, chars)
        return words
