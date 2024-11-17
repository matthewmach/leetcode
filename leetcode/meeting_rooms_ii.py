"""
Solution:
- count max number of overlaps
- sol 1:
    - sort, keep min heap of tails, pop all tails that are less than head
- sol 2:
    - two arrays of start and end times
    - overlap is how many start times come within the end time
"""

class Solution:
    def heap(self, intervals: List[List[int]]) -> int:
        heap = []
        heapq.heapify(heap)
        max_overlap = 0
        intervals.sort()
        for i in intervals:
            while heap and heap[0] <= i[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1])
            max_overlap = max(max_overlap, len(heap))

        return max_overlap

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times, end_times = [], []
        for i in intervals:
            start_times.append(i[0])
            end_times.append(i[1])
        
        start_times.sort()
        end_times.sort()

        start_i, end_i = 0, 0
        overlap = 0
        max_overlap = 0
        while start_i < len(start_times):
            if start_times[start_i] < end_times[end_i]:
                start_i += 1
                overlap += 1
            else:
                end_i += 1
                max_overlap = max(overlap, max_overlap)
                overlap -= 1
        
        return max(overlap, max_overlap)