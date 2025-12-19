class Solution:
    def countBits(self, n: int) -> List[int]:
         offset = 1 # this is in future to avoid repeated work
         dp = [0] * (n+1) #including 0 
        
         for i in range (1,n+1):
            if offset * 2 == i: 
                offset = i
            dp[i] = 1 + dp[i-offset]
            #offset will keep increasing to avoid potential repeated work
            #as this will store prevoious results and add one on it,

        # dp[1] = 1 + dp[0] = 1
        # dp[2] = 1 + dp[2-2] = 1 offset updated
        # dp[3] = 1 + dp[3-2] = 2 
        # dp[4] = 1 + dp[4-4] = 1 offset updated

         return dp