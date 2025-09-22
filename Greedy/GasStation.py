
# There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

# gas[i] is the amount of gas at the ith station.
# cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
# You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

# It's guaranteed that at most one solution exists.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if(sum(gas)<sum(cost)):
            return -1 #if the cost is high no way we can compete a loop!!
        
        total = 0
        start = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])
        
        #we keep track of the total
            if total < 0:
                total = 0 #reset total as it reached negative then the path is not possible try the next index
                start = i+1
        
        #it has to be the first index because such a solution should exist once
        .
        return start
        