class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        count = 1
        matrix = [[0] * n for i in range(n)]
        top, bottom = 0, n
        left, right = 0, n

        while top < bottom and left < right:
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            top += 1
            for i in range(top, bottom):
                matrix[i][right-1] = count
                count += 1
            right -= 1
            if not (top < bottom and left < right):
                break
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = count
                count += 1
            bottom -= 1
            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
        
        return matrix