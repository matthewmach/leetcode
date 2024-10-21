class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        out = []
        for x in range(length-2):
            tmp = []
            for y in range(length-2):
                tmp.append(
                    max(
                        grid[x][y], grid[x][y+1], grid[x][y+2],
                        grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2],
                        grid[x+2][y], grid[x+2][y+1], grid[x+2][y+2],
                    )
                ) 
            out.append(tmp)
        return out