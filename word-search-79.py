class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def backtrack(index, row, col):
            if (
                row < 0
                or col < 0
                or row > len(board) - 1
                or col > len(board[0]) - 1
                or board[row][col] != word[index]
            ):
                return False

            if index == len(word) - 1:
                return True

            c = board[row][col]
            board[row][col] = "#"
            neighbors = [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1),
            ]
            for i, j in neighbors:
                if backtrack(index + 1, i, j):
                    return True

            board[row][col] = c
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True

        return False


"""
From https://leetcode.com/problems/word-search/solutions/3164340/solution
"""


class BestSolution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])

        if len(word) > R * C:
            return False

        count = Counter(sum(board, []))

        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        seen = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or word[i] != board[r][c]
                or (r, c) in seen
            ):
                return False

            seen.add((r, c))
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )
            seen.remove((r, c))  # backtracking

            return res

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False
