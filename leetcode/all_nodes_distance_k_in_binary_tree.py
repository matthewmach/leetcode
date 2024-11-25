# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Solution:
- add parents to a hash map
- find the node as well
- traverse from the node and find all distance k

"""

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def dfs_parents(parent, node):
            if not node:
                return
            parents[node] = parent
            dfs_parents(node, node.left)
            dfs_parents(node, node.right)

        dfs_parents(None, root)
        out = []
        visited = set()
        def dfs_distance(node, distance):
            if not node or node in visited:
                return
            visited.add(node)
            if distance == k:
                out.append(node.val)
            else:
                dfs_distance(node.left, distance+1)
                dfs_distance(node.right, distance+1)
                dfs_distance(parents[node], distance+1)
        
        dfs_distance(target, 0)

        return out