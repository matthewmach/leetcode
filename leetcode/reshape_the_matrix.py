class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat

        new_m = [[0] * c for i in range(r)]
        mat_width = len(mat[0])
        count = 0
        while count < r*c:
            print (count)
            new_m[count // c][count % c] = mat[count // mat_width][count % mat_width]
            count += 1
        return new_m