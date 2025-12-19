# XOR says that same bits result in 0 and different bits result in 1

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #technically if you add all the sum of range of nums and subtract the sum of range of array nums the result should be the missing num
        #result should start with last num because that is not included in the array.

        result = len(nums)

        for i in range(len(nums)):
            result += (i-nums[i]) #the number minus the array num 

        return result 
        