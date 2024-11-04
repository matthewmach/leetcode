"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

"""
- Input: head of linked list
- Output: head of deep copied linked list

Sol:
- keep a dict of all the newly created nodes with the hash being the old node
- go through list once, creating a new node for each but not copying the links yet
- go through list again copying links
- O(n) O(n)

Optimal solution
- place the new nodes right after their respective old node
- iterate once to create the nodes
- iterate again to combine the nodes
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newNodes = {}
        newNodes[None] = None
        oldHead = head
        while oldHead:
            newNodes[oldHead] = Node(oldHead.val, oldHead.next, oldHead.random)
            oldHead = oldHead.next
        
        oldHead = head
        while oldHead:
            node = newNodes[oldHead]
            node.next = newNodes[node.next]
            node.random = newNodes[node.random]
            oldHead = oldHead.next

        return newNodes[head]