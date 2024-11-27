# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
a lot harder than normal
- need to also not that leaves aren't always on the last level
- just dfs 3 different ways for the left, leaves, and right
    - left append first
    - leaves append middle
    - right append last (appends backwards)
"""

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]

        level_dict = defaultdict(list)
        max_level = [0]
        leaves = []
        def dfs (node, level):
            if not node:
                return
            max_level[0] = max(max_level[0], level)
            level_dict[level].append(node)
            if not node.left and not node.right:
                leaves.append(node)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 0)
        out = [root.val]
        leftmost = []
        rightmost = []
        
        i = 1
        while i < max_level[0] and level_dict[i][0] != leaves[0]:    
            leftmost.append(level_dict[i][0].val)
            i += 1
        i = 1
        while i < max_level[0] and level_dict[i][-1] != leaves[-1]:    
            rightmost.append(level_dict[i][-1].val)
            i += 1
        rightmost = rightmost[::-1]

        leaves_val = []
        for leaf in leaves:
            leaves_val.append(leaf.val)
            
        if not root.left:
            return [root.val] + leaves_val + rightmost
        if not root.right:
            return [root.val] + leftmost + leaves_val        
        return out + leftmost + leaves_val + rightmost

    def optimal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        out = [root.val]
        
        def dfs_left(node):
            if not node or (not node.left and not node.right):
                return
            out.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)
        dfs_left(root.left)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and (not node.left and not node.right):
                out.append(node.val)
            dfs_leaves(node.right)
        dfs_leaves(root)

        def dfs_right(node):
            if not node or (not node.left and not node.right):
                return
            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            out.append(node.val)
        dfs_right(root.right)
        return out