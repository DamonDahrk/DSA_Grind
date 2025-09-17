# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #SlidingWindow based solution,
        left,right = 0,1

        maxProfit  = 0 #this will be updated

        while right < (len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            #update profit for right higher than left 
            else:
                left = right 
                #if this isnt true then just right is now the new lowest value found and we
                #look for right for more profit
            right += 1 #right is incremented regardless to go through prices once to check all values
        return maxProfit


        