"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        (0, 10)
        (10, 20)

        [10,20]
        [20,30]
        '''
        if not intervals:
            return 0

        timestamps = []
        for interval in intervals:
            timestamps.append((interval.start, 1))
            timestamps.append((interval.end, -1))
        
        timestamps = sorted(timestamps) # end will go first before start since -1 < 1
        count = 0
        maximum = 0
        for timestamp, delta in timestamps:
            count += delta
            maximum = max(maximum, count)
        return maximum

