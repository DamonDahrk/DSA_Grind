class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0) # we are adding the last element i.e top which is out of bounds

        for i in range (len(cost)-3,-1,-1):
            #we are starting from - 3 because that is where we can backtrack right side dp and last true element will not have
            #a viable i+2 and we can have total min cost replace the array of cost as seen below for the On time complexity
            cost[i]  +=  min(cost[i+1], cost[i+2])
        
        return min(cost[0],cost[1])
        