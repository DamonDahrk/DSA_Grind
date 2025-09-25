# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

# Follow-up: Can you solve it without sorting?


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums = [-n for n in nums]
        heapq.heapify(nums) #maxheap

        while k>1:
            heapq.heappop(nums)
            k -= 1

        return -heapq.heappop(nums)    