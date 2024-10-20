'''
Idea: set all zero changed values into some value not 0 and change all of them after first passthrough
    - problem what value to set to? what if it's in the matrix already
    - can store locations but worst case is O(n) space
    - can't use int_max because of bounds
    - BIG IDEA: use first column and row to decide what rows and columns to zero out
        - still need to store if 0,0 has to be zeroed out

'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstRowZero = False
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    if y == 0:
                        firstRowZero = True
                    else:
                        matrix[0][x] = 0
                        matrix [y][0] = 0
        
        for y in range(1, len(matrix)):
            if matrix[y][0] == 0:
                for x in range(1, len(matrix[0])):
                    matrix[y][x] = 0

        for x in range(len(matrix[0])):
            if matrix[0][x] == 0:
                for y in range(1, len(matrix)):
                    matrix[y][x] = 0
        
        if firstRowZero:
            for x in range(len(matrix[0])):
                matrix[0][x] = 0