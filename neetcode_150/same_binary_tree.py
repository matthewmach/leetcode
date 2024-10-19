class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            if not q:
                return True
            else:
                return False
        elif not q:
            return False
        same = p.val == q.val
        same = same and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return same