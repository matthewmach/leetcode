"""
Input: array of integers, k
Output: kth largest element

Ideas:
    - keep a stack of size k and just maintain that by checking each element and adding each time
        - this is just a min heap !!!!
    - Time Complexity: worst case is O(nk), O(nlogk) if you implement binary search to find position in the stack
    O(nlogk) < O(nlogn) sorting

"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [nums[0]]
        heapq.heapify(heap)

        for num in nums[1:]:
            if len(heap) < k:
                heapq.heappush(heap,num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
                
        return heap[0]