# Observation: you have to remove an interval for each one that starts before another ends
#             - keeping current min end is enough as one of them as to be removed, remove the bigger one
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        out = 0
        cur_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= cur_end:
                cur_end = end
            else:
                out += 1
                cur_end = min(cur_end, end)
        return out