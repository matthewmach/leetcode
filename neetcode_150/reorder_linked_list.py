#### To review
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        middle, last = head, head.next
        while last and last.next:
            middle = middle.next
            last = last.next.next

        # Reverse second half
        cur = middle.next
        prev = None
        middle.next = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        # Merge the two lists
        list1, list2 = head, prev
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1, list2 = tmp1, tmp2
