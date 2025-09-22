# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [2,-3,4,-2,2,1,-1,4]

# Output: 8



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        #Abuse the fact that you need maximum subarray sum

        maxSub = nums[0] #we will start with the first element then iterate through
        curSum = 0 #we keep adding here
        
        for n in nums:
            if curSum < 0:
                curSum = 0 #remove negative prefix
            curSum += n  #keep adding values here
            maxSub = max(maxSub,curSum) #always choose the max
        
        return maxSub

        