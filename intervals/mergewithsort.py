class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        n = len(intervals)

        if n == 0:
            return [] #empty interval list
        
        intervals.sort(key=lambda x:x[0])

        #sort on based of the first key and lambda is basically a small fnc without def
        merged = []
        i = 0

        while i<n:
            start = intervals[i][0]
            end = intervals[i][1]
            i += 1

            while i < n and intervals[i][0] <=end : #its in range atleast
                end = max(end,intervals[i][1])
                i += 1
            
            merged.append([start,end])
        
        return merged
            
