# You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

# Return the minimum integer k such that you can eat all the bananas within h hours.

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def MatchesHours(EatenBananas): #Checking eaten bananas (binary search soon)
            hours = 0       #hours to be updated should match our target H
            for Bananas in piles: #Bananas has to be eaten in full, partial has to be rounded up
                hours += ceil(Bananas/EatenBananas) #this is why we are using ceil to cover next
                                                     # hour
            
            return hours <= h #if hours is less than thats huge we can keep getting min hours
                              #it has be atleast equal if more then caught

        left,right = 1, max(piles)
        #left should be min bananas eaten i.e 1 and max should be the max value eaten as possible

        while left<right: #keep going till we exceed to find all possibilities via binary search
            mid = ((left+right)//2) #only return integer value
            if MatchesHours(mid):
                right = mid 
                #if found early than early half can have better solution or not
            else:
                left = mid + 1
                #HOURS are more so get the banana eating above so we can get down to less time
            
        return right 
        #by end left will be equal to right i.e have the perfect min k eaten for hours

        
        