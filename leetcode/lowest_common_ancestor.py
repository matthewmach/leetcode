# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Input: root, p, q
Output: LCA

Solution
- Initial
    - find p and all nodes leading up to it from the root
        - dfs
    - find q and all the nodes leading up to it from the root
    - go down starting from the root until an element exists in the other set

    - O(n) + O(n) + O(n) worst case = O(n)

- recursion
    - 2 cases: nodes exist in the children of the lca, one node exists in the children of of the other
    - recursion, return true if node is p or q, mark point found with varible
    - if point found and true, then set the lca to that node
    - if left and right are true, set the lca to that node
        - note every node above it will not have true for both children and thus won't overwrite it
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        out = []

        def helper(node):
            if not node:
                return False
            
            left = helper(node.left)
            right = helper(node.right)
            found = (node == p or node == q)

            if (found and right) or (found and left) or (left and right):
                out.append(node)
            
            return found or left or right

        helper(root)
        return out[0]