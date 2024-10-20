class Solution:
    def recursive(self, m: int, n: int) -> int:
        grid = [[0] * n for i in range(m)]
        grid[0][0] = 1
        def helper (x, y, grid):
            if x+1 < len(grid):
                grid[x+1][y] += 1
                helper (x+1, y, grid)
            if y+1 < len(grid[0]):
                grid[x][y+1] += 1
                helper (x, y+1, grid)

        helper (0, 0, grid)
        print (grid)
        return grid[m-1][n-1]

    # DP Solution
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for x in range(m-1):
            newRow = [1] * n
            for y in range(1, n):
                newRow[y] = newRow[y-1] + row[y]
            row = newRow
        return row[-1]