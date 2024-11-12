"""
Solution:
- swap top most digit with the biggest digit not above it
- one possibility is to keep a max heap and compare until the biggest digit isn't one of the first
- converting to string might make things easier
- problems with heap
    - when you want to replace a number, you should always take the greatest index
    - but when you want to pop a number, you should always take the smallest index

- another solution is greedy
- always store the greatest index of every occrance of a digit
- iterate through the digits and check if all the digits above it have a greater index
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        num = str(num)
        for i in range(len(num)):
            heapq.heappush(max_heap, (-int(num[i]), i))
        
        i = 0
        num = list(num)
        while len(max_heap) > 0:
            nxt = heapq.heappop(max_heap)
            if -nxt[0] > int(num[i]) and nxt[1] > i:
                same = heapq.heappop(max_heap)
                while same[0] == nxt[0]:
                    nxt = same
                    same = heapq.heappop(max_heap)
                
                tmp = num[i]
                num[i] = str(-nxt[0])
                num[nxt[1]] = tmp
                break
            i += 1

        return int("".join(num))