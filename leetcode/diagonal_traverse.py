"""
Ideas: how do you determine what diagonal to go
    - end point is x = n-1, y = m-1
    - check if max exceeded first, if it is, then you have to move an extra 2 steps down
"""
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        out = []
        x, y = 0, 0
        rev = False
        while not (y == len(mat) -1 and x == len(mat[0])-1):
            print("|")
            print(x, y)
            out.append(mat[y][x])
            x += 1 if not rev else -1 
            y += -1 if not rev else 1
            print(x, y)
            if y < 0 or y == len(mat) or x < 0 or x == len(mat[0]):
                rev = not rev


            if y == len(mat):
                y = len(mat) -1
                x = min(len(mat[0])-1, x+2)
            if x == len(mat[0]):
                x = len(mat[0]) -1
                y = min(len(mat)-1, y+2)
            if x < 0:
                x = 0
            if y < 0:
                y = 0
                
        out.append(mat[y][x])
        return out