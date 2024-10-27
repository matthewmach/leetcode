"""
Input: tree, p, q
Output: lca

Solution:
    - naive: backtrack until root 
        - find p and q
        - traverse p until root
        - traverse q until root / p visited
        - Time Complexity O(log n) * 2
            - twice to traverse up
        - Space complexity: O(log n) visited
    -     

"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        visited = set()
        parent = p
        while parent.parent != None:
            visited.add(parent)
            parent = parent.parent
        visited.add(parent)

        q_parent = q

        while q_parent != None:
            if q_parent in visited:
                return q_parent
            q_parent = q_parent.parent

        return Node(-1)              