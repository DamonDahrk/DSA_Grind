
# You are given an array of non-negative integers height which represent an elevation map.
#  Each value height[i] represents the height of a bar, which has a width of 1.


class Solution:
    def trap(self, height: List[int]) -> int:
#The entire solution has to operate on the fact that min(l,r) - ih logic

        totalwater = 0
        #we are gonna keep adding our solution here
        l,r = 0,len(height)-1
        #two pointers from left end to right end
        leftmax,rightmax = height[l],height[r]

#again we meet in middle so l<r, check the heights and add or remove accordingly
        while l<r:
            if(leftmax<rightmax):
                l += 1
                leftmax = max(height[l],leftmax)
                #negative value wont be retrieved because hieght is tracked
                #max height between current height and previous
                #formula to find the water stored as below:a
                totalwater += leftmax - height[l]
            else:
                r -= 1 
                rightmax = max(height[r],rightmax)
                totalwater += rightmax - height[r]
        return totalwater

            
            
        