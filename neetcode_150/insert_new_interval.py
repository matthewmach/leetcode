class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        done = False

        for i in range(len(intervals)):
            if done:
                out.append(intervals[i])
                continue

            if newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                out.append(intervals[i])
                done = True
            elif newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        if not done:
            out.append(newInterval)

        return out

    def clean(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                out.append(newInterval)
                return out + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                out.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # If it reaches here, it definitely hasn't appended the new interval
        out.append(newInterval)
        return out