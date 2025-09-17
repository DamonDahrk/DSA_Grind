# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation: 
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

#use deque (double-ended queue) because it gives us O(1) operations from both ends

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        resultset = [] #we are going to adding the result set here for k length sliding window
        q = deque() #a decreasing stack  will store indices only 

        for right in range(len(nums)): #will happen as right stays in frame of the num list
            #if q exists and has a value
            while q and nums[q[-1]] < nums[right]: #while latest value is lesser then keep popping 
                q.pop()     #so we pop 
            q.append(right)

            #IMPORTANT Q ONLY STORES INDICES

            if q[0] < right - k + 1:
                q.popleft()
            #remove the old max value if the left window pointer i.e right-k+1 as changed

            if right + 1 >= k:
                #if the sliding window length has been exceeded or is atleast met
                resultset.append(nums[q[0]]) #q0 holds the index of max value
                #adding the max value for the correct case
            
        return resultset




        

        