"""
Observation: always odd number of sprials, end sprial is the same axis as start
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)

        while left < right and top < bot:
            for i in range(left, right):
                out.append(matrix[top][i])
            top += 1
            for i in range(top, bot):
                out.append(matrix[i][right-1])
            right -= 1
            if not (left < right and top < bot):
                break
            for i in range(right -1, left-1, -1):
                out.append(matrix[bot-1][i])
            bot -= 1
            for i in range(bot -1, top-1, -1):
                out.append(matrix[i][left])
            left += 1
        
        return out
            