# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Solution:
- create parent hashmap
- iterate though tree, set flag if p and q found

"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        found = [False, False]
        def helper(parent, node):
            if not node:
                return
            
            parents[node] = parent
            if node == p:
                found[0] = True
            elif node == q:
                found[1] = True

            helper(node, node.left)
            helper(node, node.right)
        
        helper(None, root)
        if not (found[0] and found[1]):
            return None
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q:
            if q in ancestors:
                return q
            q = parents[q]
        return root