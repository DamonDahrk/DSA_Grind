
# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #Here we have the stones where we are smashing the top two values and return the difference, the o/p will be
        #one or zero as per the problem easy way to get top two val is maxheap

        stones = [-n for n in stones] #convert the list to negative
        heapq.heapify(stones) #turn the string to minheap then top two vals is maxheap 

        while len(stones) > 1:
            first = heapq.heappop(stones) #largest val aka y
            second = heapq.heappop(stones) #second largest val aka x
            heapq.heappush(stones, first - second ) # since they are negative the result will be same diff as was positive 

        stones.append(0) #incase list is empty 
        return abs(stones[0]) #return the value left  abs since its negative


        