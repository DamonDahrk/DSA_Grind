#Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        #JUST PURE binary search is all you need for rotated sorted array as there will always be a sorted section somwhere

        left = 0   #first index
        right = len(nums) - 1 #last index

        while left<right: #if they are equal that means thats the min value
            mid = ((left+right)//2) #binary start

            if nums[mid]>nums[right]: #that middle point hit a bottom somewhere later so it must be in the later half
                left = mid + 1
            else:
                right = mid
        
        return nums[right] #doesnt matter as it will be left == right at the end