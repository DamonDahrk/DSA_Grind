# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
# If there is no day in the future where a warmer temperature will appear for the ith day, 
# set result[i] to 0 instead.



class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ResultSet = [0] * len(temperatures)
        #Here is the result of the temperature list to be displayed
        stack = [] #We are going to be computing our results here

        for i,t in enumerate(temperatures):
            #index and temp in the temp list given
            while stack and t > stack[-1][0]:
                #while stack exists and is not empty and the current temp is greater than the last element
                stackT, stackInd = stack.pop()
            #Store the values of stack in the index and colder temperature here is popped
                ResultSet[stackInd] =  i - stackInd
            #this updates the entire result for every pop and due to the fact that i-stack tracks the difference
            #we update the result accordingly
            #find the number of days it took b substracting the index
            stack.append([t,i])
        return ResultSet

        #O(n) complexity
        