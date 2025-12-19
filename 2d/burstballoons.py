class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # assume the coins balloon be [4,2,3,7]

        nums = [1] + nums + [1] # we are adding the out of bounds value which will never be computed
        dp = {} #where we will be storing the key value pairs of baloons pairs and their max coins op
        
        # index 0 1 2 3 4 5
        # nums  1 4 2 3 7 1   (here we can see we added two padding of out of bounds value)

        def DFSbranch(l,r):
            if l>r:
                return 0 # we have reached the end of the index of balloons
            if (l,r) in dp:
                return dp[(l,r)] #cached value will be returned for o 1 
            
            dp[(l,r)] = 0 # intialize at zero for now

            for i in range (l,r+1): #r+1 because of the additonal out of bound values
                coins = nums[l-1] * nums[i] * nums[r+1]
                #here 
                #index  1 4 | 2 | 3 7 1
            #subarrays  l-1 | i | r+1    the formula is left*i*right by prob 
                coins += DFSbranch(l,i-1) + DFSbranch(i+1,r)
            # now add the other subarray completed solution  by changing the focus to them  (backtrack start)
                dp[(l,r)] = max(coins,dp[(l,r)]) #here we keep updating the values for the coins of last possible subarray sum
            return dp[(l,r)] 
        return DFSbranch(1,len(nums)-2)
        # we will be returning from index 1 (first real value) to real last value i.e 6-2 = 4 because there are four digits
        # we are using CACHE Not FOR LOOPS or array fancy stuff

        #time complexity for existed computed value is O(1) FOR unknown is n 3 
        