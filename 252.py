"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, ints: List[Interval]) -> bool:

        ints.sort(key=lambda x: (x.start,x.end))

        pend=-1
        for i in ints:
            if pend<=i.start: pend=i.end
            else: return False

        return True