"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

"""
Solution
- bfs append next element in stack if same levle, null if not 
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([(root,0)])
        while queue:
            node, level = queue.popleft()
            if node:
                if queue:
                    next_node, next_level = queue[0]
                    if next_level == level:
                        node.next = next_node
                    else:
                        node.next = None
                else:
                    node.next = None
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
        return root