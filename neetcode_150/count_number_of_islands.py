class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def helper(x, y, grid, counter) -> int:
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                if grid[x][y] == "1":
                    grid[x][y] = str(counter)
                    helper(x+1, y, grid, counter)
                    helper(x-1, y, grid, counter)
                    helper(x, y+1, grid, counter)
                    helper(x, y-1, grid, counter)
        counter = 2
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    helper(x, y, grid, counter)
                    counter += 1


        return counter - 2 