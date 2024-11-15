# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Solution:
- Initial idea, just do kN comparisions
- to speed up the comparisions, we can replace it with the heap
    - insert in heap is log k vs k comparisions
    - need to make heap node to define comparision in heap
    - just add the next node in the linked list into the heap
"""

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        head = ListNode(-1)
        current = head

        for l in lists:
            if l:
                heapq.heappush(heap, HeapNode(l))
        
        while heap:
            next_node = heapq.heappop(heap)
            current.next = next_node.node
            current = next_node.node

            if next_node.node.next:
                heapq.heappush(heap, HeapNode(next_node.node.next))

        return head.next