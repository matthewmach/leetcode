"""
Input: List of intervals
Output: list of merged intervals

Solution:
- sort intervals by interval start
- keep track of last interval end
- if you're merging a current interval check if it needs to be merged
- time complexity: O(nlogn) 
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key = lambda x : x[0])
        out = []
        last_interval = intervals[0]
        for interval in intervals[1::]:
            if last_interval[1] >= interval[0]:
                last_interval[1] = max(last_interval[1], interval[1])
            else:
                out.append(last_interval)
                last_interval = interval
        
        out.append(last_interval)
        return out