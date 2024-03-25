"""
Solution 1:
    - Build heap.
    - Delete max (k - 1) time

Solution 2:
    - Min-heap

Solution 3:
    - Quick selection

Solution 2 and 3 are from:
https://leetcode.com/problems/kth-largest-element-in-an-array/solutions/3906260/100-3-approaches-video-heap-quickselect-sorting

Very detail explanation with lot of insight! Overall in the test dataset of Leetcode,
solution 2 gives the best result!
"""


class Solution1:
    def createHeap(self, nums: list[int], n: int):
        for i in range(n):
            parentIndex = (i - 1) // 2
            while nums[i] > nums[parentIndex] and parentIndex >= 0:
                nums[i], nums[parentIndex] = nums[parentIndex], nums[i]
                i, parentIndex = parentIndex, (parentIndex - 1) // 2

    def heapify(self, nums: list[int], i: int, n: int):
        l = 2 * i + 1
        r = 2 * i + 2
        m = i

        if l < n and nums[i] < nums[l]:
            m = l

        if r < n and nums[m] < nums[r]:
            m = r

        if m != i:
            nums[m], nums[i] = nums[i], nums[m]
            self.heapify(nums, m, n)

    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        self.createHeap(nums, n)
        kLargest = nums[0]
        while k > 1:
            nums[0] = nums[n - 1]
            n -= 1
            k -= 1
            self.heapify(nums, 0, n)
            kLargest = nums[0]

        return kLargest


import heapq


class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

        return heap[0]


import random


class Solution3:
    def findKthLargest(self, nums, k):
        left, right = 0, len(nums) - 1
        while True:
            pivot_index = random.randint(left, right)
            new_pivot_index = self.partition(nums, left, right, pivot_index)
            if new_pivot_index == len(nums) - k:
                return nums[new_pivot_index]
            elif new_pivot_index > len(nums) - k:
                right = new_pivot_index - 1
            else:
                left = new_pivot_index + 1

    def partition(self, nums, left, right, pivot_index):
        pivot = nums[pivot_index]
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        stored_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[stored_index] = nums[stored_index], nums[i]
                stored_index += 1
        nums[right], nums[stored_index] = nums[stored_index], nums[right]
        return stored_index
