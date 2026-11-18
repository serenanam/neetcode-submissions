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
        for i in range(1, len(intervals)):
            e1 = intervals[i-1].end
            s2 = intervals[i].start
            if s2 < e1:
                return False
        return True

        #Time: O(nlogn) - sorting - O(nlogn), linear search - O(n)
        #Space: O(1)
