class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n #the dynamic prog table for counting greatest continuos subsequence

        for i in range (1,n): #since 0 is already 1 we know and we have to compare values by jth index later to figure out the trail
         for j in range (0,i): #ith index is the latter value we will compare with 
            if nums[i]>nums[j]: #establishes the sequence
                dp[i] = max(dp[i],dp[j]+1) #if the greater value already exists then take that max instead of resetting the count 
                                        #jth index comes in handy as the second loop is purely for tracking the best longest seq
                                        #till the ith index
        
        return max(dp)
        