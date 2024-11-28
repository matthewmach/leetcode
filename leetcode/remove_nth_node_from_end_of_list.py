# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- initial solution, keep n+1 queue of elements
- another idea, have a pointer that's n+1 away from first pointer
    - when faster pointer is at null, cull the point at the first node
    - both points start at a dummy node before head (so we have remove head easier)
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second = dummy

        for i in range(n+1):
            second = second.next
        
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dummy.next

    def queue(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        while node:
            if len(queue) == n+1:
                queue.popleft()
            queue.append(node)
            node = node.next

        if len(queue) == 1:
            return None
        elif len(queue) == 2:
            if n == 1:
                queue[0].next = None
            if n == 2:
                return queue[1]
        else:
            if len(queue) == n+1:
                queue[0].next = queue[2]
            else:
                return queue[1]
        return head