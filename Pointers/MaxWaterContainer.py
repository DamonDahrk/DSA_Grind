# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container. Return the maximum amount of water 
# a container can store.

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxwater = 0 # we will fill this up with the true result
        left , right = 0 , len(heights) - 1 
        #start pointers for the both ends in the graph where we will keep getting area

        while(left<right):
            area = (right-left) * min(heights[left],heights[right]) 
            #      breadth      x    length (min cuz it cant go above out of bounds for max)
            maxwater = max(maxwater,area)
            #update the max water area
            if(heights[left]<heights[right]):
                left += 1 #increase left pointer for greater value for prolly bigger next height
            else:
                right -= 1 # no need checking for equal cuz it could be above or below
            
        return maxwater
        