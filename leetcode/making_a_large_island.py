"""
- Idea:
    - iterate through each island in the grid, marking it with an island count and a size
        - can recursively go through this
        - replace the 1 with an island number (starting with -1)
        - add to a dict storing the space of the island 
    - either store all the empty spaces or iterate through the grid again
        - add all adjacent nodes of different island to get max size
    - O(n^2) + O(n^2) = O(n^2)
"""
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        count = -1
        max_island = 0
        size_dict = defaultdict(int)
        n = len(grid)
        def helper(x, y, count):
            if -1 < x < n and -1 < y < n and grid[x][y] == 1:
                grid[x][y] = count
                size_dict[count] += 1
                helper(x+1, y, count)
                helper(x-1, y, count)
                helper(x, y+1, count)
                helper(x, y-1, count)
        
        for y in range(n):
            for x in range(n):
                if grid[x][y] == 1:
                    helper(x, y, count)
                    max_island = max(max_island, size_dict[count])
                    count -= 1
        max_size = 0
        for y in range(n):
            for x in range(n):
                if grid[x][y] == 0:
                    to_merge = set()
                    if x > 0:
                        to_merge.add(grid[x-1][y])
                    if x < n-1:
                        to_merge.add(grid[x+1][y])
                    if y > 0:
                        to_merge.add(grid[x][y-1])
                    if y < n-1:
                        to_merge.add(grid[x][y+1])
                    island_size = 1
                    for element in to_merge:
                        island_size += size_dict[element]
                    max_size = max(max_size, island_size)
        
        return max(max_size, max_island)