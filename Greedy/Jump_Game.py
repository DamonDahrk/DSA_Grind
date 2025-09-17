class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 0
        #maximum the frog can jump
        for i,jump in enumerate(nums):
    #making index value looping
            if(i>maxJump):
                return False
            #this means that no matter what the jump value is it can never go to next element
            #to reach the end
            maxJump = max(maxJump,jump+i)
            #updating the max jump to next element
            if maxJump >= (len(nums)-1):
                return True
            #if the jump can blow past the last element or reach it then its succesful
        return True
        

#         You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.