class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 :
            return False 
        #if its equal it cannot be odd in anyway

        dp = set() #making set is important because we cannot have duplicate values
                   # in set which will be imp to acccount for all value sums
        dp.add(0) # base value 0 added

        target = sum(nums) // 2 #we need to find a sum equal to have to have eq partition

        for i in range (len(nums)-1,-1,-1): #iterate from the back 
            nextDP = set() #new set to add the data to the main set
            for p in dp:
                nextDP.add(nums[i]+p) #add the sum
                nextDP.add(p) #dont add the sum
            dp = nextDP #it keeps updating and adding all the sums
            if target in dp:
                return True
        
        return False

        