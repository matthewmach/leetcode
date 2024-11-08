# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Solution:
- recursively iterate through the tree, adding elements to a dictionary based on column, add subtract column based on if you go left or right
    - have to deal with same positions,
    - add tuple to dictionary, resolve conflicts then
- runtime O(n) for initial dictionary, O(n) to resolve conflicts
"""
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_dict = defaultdict(list)
        col_dims = [0,0]
        def helper(node, row, column):
            if node:
                col_dict[column].append((row, node.val))
                col_dims[1] = max(col_dims[1], column)
                col_dims[0] = min(col_dims[0], column)
                helper(node.left, row+1, column-1)
                helper(node.right, row+1, column+1)
        
        helper(root, 0, 0)
        out = []
        for i in range(col_dims[0], col_dims[1]+1):
            out_col = []
            col = col_dict[i]
            last_row = 0
            col.sort()
            for val in col: 
                print (val)
                if last_row == val[0] and last_row != 0:
                    tmp = out_col[-1]
                    out_col[-1] = min(tmp, val[1])
                    out_col.append(max(tmp, val[1]))
                else:
                    out_col.append(val[1])
                    last_row = val[0]
            out.append(out_col)
        return out