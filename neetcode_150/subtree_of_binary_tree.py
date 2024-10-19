# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        equal = False


        def helper(root, subRoot) -> bool:
            if not root and not subRoot:
                return True
            elif root and subRoot and root.val == subRoot.val:
                return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
            else:
                return False            

        if root.val == subRoot.val:
            equal = helper(root, subRoot)

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return equal or left or right