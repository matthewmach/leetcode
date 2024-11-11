"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Solution
- iterate though graph creating nodes
- iterate through graph linking nodes
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}
        stack = [node]
        while stack:
            cur = stack.pop()
            nodes[cur] = Node(cur.val, None)
            for n in cur.neighbors:
                if n != None and not n in nodes:
                    stack.append(n)
        
        visited = set()
        stack = [node]
        while stack:
            cur = stack.pop()
            if not cur in visited:
                visited.add(cur)
                newNode = nodes[cur]
                for n in cur.neighbors:
                    if not n in visited:
                        stack.append(n)
                    if newNode.neighbors:
                        newNode.neighbors.append(nodes[n])
                    else:
                        newNode.neighbors = [nodes[n]]
            
        return nodes[node]