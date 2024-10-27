"""
input: binary tree
    - question is left prio'd over right what if you have two nodes of same veritcallity
output: list of list of vertical order traversal

solution:
    - keep counter from root, add to dict based on level
        - add elements to dict based on level
        - traverse left to right to prio left 
    - keep counter of max distance right and left from root
    - iterate through dict through right and left appending to list
    - Time complexity: O(n) + O(n) worst case = O(n)
    - Space complexity: O(n)


    - Problem: left is always priod but no sense of depth
        - priority queue instead of recursion
        - add to dict with depth and sort
            - easiest solution
"""
from collections import defaultdict


class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def veriticalOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []

        level_dict = defaultdict(list)
        limits = [0, 0]
        def traverse(node, level, depth): 
            if node != None:
                level_dict[level].append((node.val, depth))
                traverse(node.left, level-1, depth + 1)
                traverse(node.right, level + 1, depth +1)
                limits[1] = max(limits[1], level)
                limits[0] = min(limits[0], level)
        
        traverse(root, 0, 0)
        out = []
        for i in range(limits[0], limits[1]+1):
            level_dict[i].sort(key=lambda x: x[1])
            out.append([node[0] for node in level_dict[i]])

        return out