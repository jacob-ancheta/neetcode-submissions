"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals:
            return True 
        for i in range(len(intervals)):
            if i == len(intervals) - 1:
                return True
            elif intervals[i].end > intervals[i + 1].start:
                return False