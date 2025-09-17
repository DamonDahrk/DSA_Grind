class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        SpeedPositionPairs = [[pos,speed] for pos,speed in zip(position,speed) ]
        #tuple pairs list, iterating through the two input lists

        stack = [] #stack where we will be updating the time and sending the len as result for cars

        for pos,speed in sorted(SpeedPositionPairs)[::-1]: #Reverse Sorted Pair of speed and pos
            stack.append((target-pos)/speed) #adding time distance by speed
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                #latest value is not greater than the one before it then it will collide/car fleet
                stack.pop() #remove that redundant value
        return (len(stack))

            
