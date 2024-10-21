class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_m = [[0] * len(matrix) for i in range(len(matrix[0]))]
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                new_m[x][y] = matrix[y][x]
        return new_m