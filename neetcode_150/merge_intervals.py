class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = []

        cur = intervals[0] 
        for i in range(1, len(intervals)):
            if intervals[i][0] > cur[1]:
                out.append(cur)
                cur = intervals[i]
            else:
                cur = [cur[0], max(cur[1], intervals[i][1])]

        out.append(cur)
        return out       
                