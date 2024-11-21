# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
- just count nodes
    - nvm need to check last layer
    - dict for each layer, with counter compare key to number 
    - need to check for far left
    - push nodes to dict first?
    - take note of what layers contain null
    - manually count last layer
"""
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        count_dict = defaultdict(list)
        null_dict = defaultdict(int)
        max_level = [0]
        def helper(node, level):
            count_dict[level].append(node)
            if not node:
                null_dict[level] = 1
                return
            max_level[0] = max(max_level[0], level)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)

        for level in range(0, max_level[0]):
            if level in null_dict:
                return False
        
        null_found = False
        for ele in count_dict[max_level[0]]:
            if not ele:
                null_found = True
            else:
                if null_found:
                    return False        
        return True