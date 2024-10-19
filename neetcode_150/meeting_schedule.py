class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda x : x.start)

        end = 0
        for i in intervals:
            if i.start >= end:
                end = i.end
            else:
                return False
        return True