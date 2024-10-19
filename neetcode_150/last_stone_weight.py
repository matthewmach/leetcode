class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        invStones = []
        for s in stones:
            invStones.append(-s)
        maxHeap = invStones
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = maxHeap[0]
            if second > first:
                heapq.heapreplace(maxHeap, first-second)
            else:
                heapq.heappop(maxHeap)
        maxHeap.append(0)
        return abs(maxHeap[0])