class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
         
        start, end = newInterval #here it will be the start and end point of the newInterval range list

        n = len(intervals) #final point of the intervals
        result = [] #result range interval list that we will get 
        i = 0 #index that will be traversed through the list 

        while i<n and intervals[i][1] < start:
            result.append(intervals[i]) #every individual interval added before even the start of our target interval
            i += 1 
        
        #eg. [2,3] will be added before target [4,5] because its last value is before the first value of our target interval

        while i<n and intervals[i][0] <= end: #this means that the range atleast exist between start and end 
            start = min(start,intervals[i][0]) #update values accordingly for that
            end = max(end,intervals[i][1])
            i += 1
            #merging the left and right end

        result.append([start, end]) #add that new range to the result

        while i<n:  #the rest is naturally obviously after end range after our target so just add
            result.append(intervals[i])
            i +=1
        
        return result
   
