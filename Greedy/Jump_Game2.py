class Solution:
    def jump(self, nums: List[int]) -> int:
       JumpCounter = 0
       left,right = 0,0 #left pointer and the right pointer will be initialized as 0 and 1

       while right < len(nums) - 1:
            Farthest = 0
            for i in range (left,right+1):
                Farthest = max(Farthest,nums[i]+i)

            
            JumpCounter += 1
            left = right + 1 #next element after right
            right = Farthest #farthest element will stop after it reaches len limit
            
       return JumpCounter


        
        