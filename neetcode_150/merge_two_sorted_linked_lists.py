# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2
        prevNode = None
        head = None

        while node1 != None or node2 != None:
            if node1 == None:
                newNode = node2
                node2 = node2.next
            elif node2 == None:
                newNode = node1
                node1 = node1.next
            else:
                if node1.val > node2.val:
                    newNode = node2
                    node2 = node2.next
                else:
                    newNode = node1
                    node1 = node1.next

            if prevNode != None:
                prevNode.next = newNode
            else:
                head = newNode

            prevNode = newNode

        return head