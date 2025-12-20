class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {} #we will be caching our unbounded distinct combination results, also as we go further into the branching we can 
                    #account for the possibilities as long as it is within the array and granted it matches the amount
        
        def dfs(i,a):
            if a == amount: 
                return 1  #a coin exist that exactly matches the amount 
            if a>amount:
                return 0 #if the amount exceeded stop and return 0 
            if i == len(coins):
                return 0 #ran out of coins case  
            
            if (i,a) in cache:
                return cache[(i,a)] #this is where the cache comes into play where it return an existing result and prevent
                                    #repeated calcs
            
            cache[(i,a)] = dfs(i,coins[i] + a) + dfs(i+1,a) # take amount then add to total a else just go to the next coin in case of ignore

            return cache[(i,a)]
        
        return dfs(0,0) #start at the first index of the array of coins and amount being 0 till matches our target amount 

        