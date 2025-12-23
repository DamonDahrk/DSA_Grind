"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True   #no conflict because no meetings exist in the first place
        
        intervals.sort(key=lambda x:x.start) 

        FirstEnd = intervals[0].end # last value for the first meeting

        for i in range (1,len(intervals)): #start from the following meeting timings:
            start = intervals[i].start
            end = intervals[i].end 

            if start < FirstEnd:
                return False #conflict found because next meeting started before first one ended.
            
            FirstEnd = end #if no conflict found then just update the end to the next one
        
        return True #out of the loop proof this is valid
