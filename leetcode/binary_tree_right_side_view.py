# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Input: root
Output: right side view

Solution:
- bfs but you take the last element in the layer
"""
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([(root, 1)])
        out = []
        while queue:
            node = queue.pop()
            print (len(out), node[1])
            if not node[0]:
                continue

            if len(out) < node[1]:
                out.append(node[0].val)
            else:
                out[node[1]-1] = node[0].val

            queue.appendleft((node[0].left, node[1]+1))
            queue.appendleft((node[0].right, node[1]+1))
        
        return out