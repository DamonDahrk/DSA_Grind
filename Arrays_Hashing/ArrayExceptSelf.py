class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = [1] * len(nums)
        #first we are creating an array of results to multplied on
        # for list -> 1 2 5 3 if we want to ignore 5 then we need prefix product 2 and 
        # multiply that by postfix product 3 i.e  6 ignoring five now do that without
        #making post fix prefix stack to get o(1) and o n time complexity

        postfix=1
        prefix=1
        #initial values are 1 

        for i in range(len(nums)):
            result[i] = prefix #attaching postfix ghost stack here orderly to multiply
            prefix = prefix * nums[i] #it will update prefix and move on to next position
        
        for i in range(len(nums)-1,-1,-1): #backwards for postfix 
            result[i] = result[i] * postfix #to not overwrite prefix values compute here only
            postfix = postfix * nums[i] #getting postfix multiplication from behind

        #self values are effectively removed like this and result is stack for every missing ith element
        
        return result
