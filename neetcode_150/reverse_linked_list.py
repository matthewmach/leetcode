# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prevNode = None
        while node != None:
            newNode = ListNode(node.val, prevNode)
            prevNode = newNode
            node = node.next

        return prevNode