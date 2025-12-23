class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort() #SORT IS IMPORTANT For this problem
        result = 0 
        FirstEnd = intervals[0][1] #first end of the interval list [a,b]

        for start,end in intervals[1:] : #start after the first index
            if start >= FirstEnd: #if the first value a2 of [a2,b2] is > last b then its definitely not overlapping  then update the end
                FirstEnd = end
            else:
                result += 1
                FirstEnd = min(end,FirstEnd) #otherwise just skip the value and we are going to the next value to check . 

        return result