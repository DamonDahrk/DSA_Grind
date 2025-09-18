class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #FIRST lets find the min in the sorted rotated array

        left,right = 0, len(nums) - 1

        while left<right:
            mid = ((left+right)//2)
            if nums[mid]>nums[right]:
                left = mid + 1
            else:
                right = mid
        
        mid_index = left
            
        #by the end of this left and right should have the same min index 

        if nums[mid_index] == target:
            return mid_index #return if the target was the min value of the array
        
        if 0 == mid_index : #this means the array is sorted as it is the min value at first
            left,right = 0, len(nums) - 1
        elif nums[0] <= target <= nums[mid_index - 1]: #is thr target in the first half 
                                                              #before min index
            left,right = 0 , mid_index-1 
        else:
            left,right = mid_index , len(nums) - 1
        
        #traditional binary search

        while left<=right:
            mid = ((left+right)//2)
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid + 1 #target is bigger
            else:
                right = mid - 1 #target is smaller
        
        return -1 #the value dont match and it doesnt exist


        