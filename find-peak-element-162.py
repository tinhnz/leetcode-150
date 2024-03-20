class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            if right - left == 1:
                return right if nums[right] > nums[left] else left

            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                right = mid - 1
                continue

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
                continue

            return mid

        return left
