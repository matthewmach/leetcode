class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        row = 0

        while l <= r:
            m = l + ((r-l) // 2)
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
            else: 
                return True

        if l == len(matrix) or target < matrix[l][0]:
            row = r
        else:
            row = l
        
        l, r = 0, len(matrix[row])-1
        
        while l <= r:
            m = l + ((r-l) // 2)
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else: 
                return True
        return False