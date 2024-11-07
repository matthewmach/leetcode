"""
Solution:
- keep a max heap of the distances and points
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        heapq.heapify(closest)
        for p in points:
            distance = sqrt(pow(p[0], 2) + pow(p[1], 2))
            if len(closest) < k:
                heapq.heappush(closest, (-distance, p))
            elif -distance > closest[0][0]:
                heapq.heappushpop(closest, (-distance, p))

        out = []
        for p in closest:
            out.append(p[1])
        return out