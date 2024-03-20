class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def getValue(index: int, width: int) -> int:
            row = index // width
            col = index % width
            return matrix[row][col]

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            value = getValue(mid, n)
            if target > value:
                left = mid + 1
            elif target < value:
                right = mid - 1
            else:
                return True

        return False
