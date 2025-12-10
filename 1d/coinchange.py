class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort() #sort to asc to give the last dp[amount] away 

        dp = [0] * (amount+1) #including the dynamic prog table to include the zeroth outcome i.e 0 since we are looking for
                              #lowest possible coin change 

        for i in range (1,amount+1): #we are intrested in the occurence of amount 1 onwards 0 is already 0
            minCoinChange = float('inf') #max default value for now at start of every loop
            for coin in coins:
                difference = i - coin #how much money left over to match amount after using this currency now
                if difference < 0:
                    break #no need to continue processing for negative value as is not valid
                
                minCoinChange = min(dp[difference] + 1 ,minCoinChange) #dp[diff] is smart cuz it passively updates the dp table
                                                                       #as well as accounts for that currency used so add one
                                                                        #incase of exact match dp[0] helps out give 1
            dp[i] = minCoinChange  #update coin change in the dp table
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
                

        