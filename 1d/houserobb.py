class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0 

        # array = [rob1,rob2,n,n+1,....n+n]

        for n in nums:
            temp = max(rob2,rob1+n) #for this max function we are only alternating between first two possible outcomes,
                                    #ignore the first house if more money include if the prior has better alternate money
                                    #but it can be updated as it iterates thru rest of array where the magic of temp values come
            rob1 = rob2
            rob2 = temp

        return rob2  #this will always have the max value