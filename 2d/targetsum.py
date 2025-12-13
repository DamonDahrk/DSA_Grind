class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} #ith index of where we are at in the list, sum (the total number of ways to attain the target sum)

        def backtrack(i,totalsum):
            if i>= len(nums):
                return 1 if target == totalsum else 0
            #base case above for going out of bounds and add 1 way for reaching the sum
            if (i,totalsum) in dp:
                return dp[(i,totalsum)] #for similar result and place avoid recalculations 
            
            dp[(i,totalsum)] = backtrack(i+1,totalsum+nums[i]) + backtrack(i+1,totalsum-nums[i]) #now calc all possible
            #addition and substraction for every value in the array and their addition is the result right? cuz it has
            #all possible outcomes, only return for valid ways to match the target and thats the result
            return dp[(i,totalsum)]
        
        return backtrack(0,0)

        