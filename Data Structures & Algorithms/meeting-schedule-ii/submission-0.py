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

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])
        count, maximum = 0, 0
        i, j = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                count += 1
                maximum = max(maximum, count)
                i += 1
            else:
                count -= 1
                j += 1
        return maximum
