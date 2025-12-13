class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = {} #we are gonna have key -> i, buying i.e ith index of the prices, state of buying or not
                #value -> max_value
         #i+1 -> skip the day or after buying 
         #i+2 -> after selling cannot buy next day i.e cool it

        def dfs(i,buying) :
            if i >= len(prices):
                return 0    
            #if we are out of bounds 

            if (i,buying) in dp:
                return dp[(i,buying)] #dont compute what already has been computed
            
            cooldown = dfs(i+1,buying) #skip the day keep bool as is

            if buying:
                buy = dfs(i+1,False) - prices[i] #we bought the stock so reduce the value 
                dp[(i,buying)] = max(buy,cooldown) #take the max value if buy or cooldown
            else:
                sell = dfs(i+2,True) + prices[i] #sold stocks buying is available after two days now, cannot buy before sell
                dp[(i,buying)] = max(sell,cooldown) #take the max value if sell or cooldown
            
            return dp[(i,buying)] #return the max value as result
        
        return dfs(0,True)
        