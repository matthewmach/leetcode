from math import ceil

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def invert (x, y):
            return [y, len(matrix)-1-x]
        for x in range(len(matrix)-1):
            for y in range(x, len(matrix)-1-x):
                prev = matrix[x][y]
                for i in range(4):
                    inv = invert(x, y)
                    tmp = matrix[inv[0]][inv[1]]
                    matrix[inv[0]][inv[1]] = prev
                    prev = tmp
                    x, y = inv[0], inv[1]