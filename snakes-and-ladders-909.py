"""
This is an easy BFS traversal problem. The tricky problem is how to calculate
the coordinate of current cell on the board (Boustrophedon style).
"""

from collections import deque


class Solution:
    def getNext(self, board: list[list[int]], cur, last) -> int:
        if cur >= last:
            return last

        n = len(board)
        row = cur // n
        col = cur % n
        if row % 2 != 0:
            col = n - col - 1

        row = n - row - 1
        return board[row][col] - 1 if board[row][col] != -1 else cur

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        lastCell = len(board) ** 2 - 1
        cellQ, stepQ = deque(), deque()
        cellQ.append(0)
        stepQ.append(0)
        visited = {0}
        while len(cellQ):
            curCell = cellQ.popleft()
            curStep = stepQ.popleft() + 1
            if curCell + 6 >= lastCell:
                return curStep

            for i in range(6):
                nxtCell = self.getNext(board, curCell + i + 1, lastCell)
                if nxtCell in visited:
                    continue

                if nxtCell == lastCell:
                    return curStep

                visited.add(nxtCell)
                cellQ.append(nxtCell)
                stepQ.append(curStep)

        return -1
