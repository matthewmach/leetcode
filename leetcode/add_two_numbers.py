class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        cur = None
        while l1 or l2 or carry != 0:
            add = carry
            if l1:
                add += l1.val
                l1 = l1.next
            if l2:
                add += l2.val
                l2 = l2.next
            carry = add // 10
            new_node = ListNode(add % 10)
            if cur:
                cur.next = new_node
            else:
                head = new_node
            cur = new_node

        return head