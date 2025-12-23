"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0   #no meetings even exist so no need

        intervals.sort(key=lambda x: x.start)       
        MinHeap = [] #minheap will always give us

        for interval in intervals:  #THIS STUPID PROGRAM HAS A STUPID CLASS THATS WHY EXTRA THREE LINES
            start = interval.start
            end = interval.end
            if MinHeap and start>=MinHeap[0]: #if a room even exists here and there is space for the next meeting start
                heapq.heappop(MinHeap) #space it in that particular day
            
            heapq.heappush(MinHeap,end) #enter the ending for the first meeting and the rest meetings so on..

            #NOT USE IN ELSE CASE because the reused ROOM STILL OCCUPIES A ROOM
            
        return len(MinHeap) #will give is the needed days
        