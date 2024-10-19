class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root) -> [int, bool]:
            if not root:
                return [0, True]
            left, right = helper(root.left), helper(root.right)
            return [max(left[0]+1, right[0]+1), abs(left[0]- right[0]) <= 1 and left[1] and right[1]]
        return helper(root)[1]