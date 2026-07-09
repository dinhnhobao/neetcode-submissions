"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda interval: interval.start) # sort by start time and end time
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end: # overlap
                return False
        return True

