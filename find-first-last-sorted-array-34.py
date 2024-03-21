"""
Apply 2 binary search to find the left and right bounds of the range.
I have overthought for a better solution (using one loop or so). 2 * log(n)
is still log(n).
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search(leftBound: bool):
            left, right = 0, len(nums) - 1
            found = -1
            while left <= right:
                mid = (left + right) // 2
                if target < nums[mid]:
                    right = mid - 1
                    continue

                if target > nums[mid]:
                    left = mid + 1
                    continue

                found = mid
                if leftBound:
                    right = mid - 1
                else:
                    left = mid + 1

            return found

        l = search(True)
        return [l, search(False) if l != -1 else l]
