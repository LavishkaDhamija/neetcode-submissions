"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans = 0
        start = []
        end = []
        s = 0
        e = 0
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        start.sort()
        end.sort()
        rooms = 0
        max_rooms = 0
        for i in range(len(intervals)):
            if start[s] < end[e]:
                rooms += 1
                s += 1
                max_rooms = max(rooms,max_rooms)
            else:
                rooms -= 1
                e += 1
        return max_rooms


        


        


        