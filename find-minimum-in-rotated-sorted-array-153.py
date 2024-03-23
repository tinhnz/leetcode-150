class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2

            if nums[left] <= nums[mid] and nums[mid] <= nums[right]:
                return nums[left]

            if nums[left] > nums[mid]:
                left += 1
                right = mid
            else:
                left = mid + 1

        return nums[left]
