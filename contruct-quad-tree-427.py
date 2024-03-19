# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> "Node":
        return self.build(grid, 0, 0, len(grid))

    def build(self, grid: list[list[int]], row: int, col: int, size: int) -> "Node":
        if size == 1:
            return Node(grid[row][col] == 1, True)

        if size == 2:
            ok = (
                grid[row][col] == grid[row + 1][col]
                and grid[row][col] == grid[row][col + 1]
                and grid[row][col] == grid[row + 1][col + 1]
            )
            if ok:
                return Node(grid[row][col] == 1, True)

            return Node(
                grid[row][col] == 1,
                False,
                Node(grid[row][col] == 1, True),
                Node(grid[row][col + 1] == 1, True),
                Node(grid[row + 1][col] == 1, True),
                Node(grid[row + 1][col + 1] == 1, True),
            )

        halfSize = size // 2
        topLeft = self.build(grid, row, col, halfSize)
        topRight = self.build(grid, row, col + halfSize, halfSize)
        bottomLeft = self.build(grid, row + halfSize, col, halfSize)
        bottomRight = self.build(grid, row + halfSize, col + halfSize, halfSize)

        sameValue = (
            topLeft.val == topRight.val
            and topRight.val == bottomLeft.val
            and bottomLeft.val == bottomRight.val
        )
        sameLeaf = (
            topLeft.isLeaf
            and topRight.isLeaf
            and bottomLeft.isLeaf
            and bottomRight.isLeaf
        )
        if sameValue and sameLeaf:
            return Node(topLeft.val, True)
        else:
            return Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)
