"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""
Solution
- recursively place nodes in order to add to a list
- iterate through list to place links
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        order = []
        def helper(node):
            if not node:
                return

            helper(node.left)
            order.append(node)
            helper(node.right)
        
        helper(root)

        for i in range(len(order)):
            node = order[i]
            node.left = order[i-1]
            node.right = order[(i+1) % len(order)]
        
        return order[0]