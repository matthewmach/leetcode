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
    
    def optimal(self, list1:ListNode, list2:ListNode) -> ListNode():
        head = ListNode()
        node = head

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        # Observation: if one list is empty, then just insert the entirely of the other remaining list        
        node.next = list1 or list2

        return head.next