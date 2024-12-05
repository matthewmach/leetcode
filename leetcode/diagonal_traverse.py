"""
Ideas: how do you determine what diagonal to go
    - end point is x = n-1, y = m-1
    - when reaching the endpoint of one axis, just increment the other by 1
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

    def clearer(self, mat: list[list[int]]) -> list[int]:
        out = []
        x, y = 0, 0
        m, n = len(mat), len(mat[0])
        direction = True
        for i in range(m * n):
            out.append(mat[y][x])
            if direction:
                if y == 0 and x != n-1:
                    direction = False
                    x += 1
                elif x == n-1:
                    direction = False
                    y += 1
                else:
                    y -= 1
                    x += 1
            else:
                if x == 0 and y != m-1:
                    direction = True
                    y += 1
                elif y == m - 1:
                    direction = True
                    x += 1
                else:
                    x -= 1
                    y += 1
        return out
