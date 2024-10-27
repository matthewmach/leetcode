"""
Input: n x n binary matrix named grid
Output: length of clear path or -1
    - clear path must be all 0s

Solution:
    - recursion
        - approx O(8n) as we have to backwards traverse
        - space complexity equal to max depth, equal to the length of longest clear path
        - can run into loops if zeroes are connected 
    - dp
        - O(n) if properly done
        - N^2 space complexity
        - check only cells above it for the min
            - have to update cells above it with it's value + 1
    - bfs
        - typical for shortest path problems 
        - can turn the grid into a graph with each zero as a node and each possible move as an edge
    - A* is a possible solution but is much more complicated than bfs 
"""

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        max_row, max_col = len(grid[0]), len(grid)
        def get_neighbors(row, col):
            directions = ((0, 1), (0, -1), (1, 0), (-1,0), (1, 1), (-1, 1), (1, -1), (-1, -1))
            out = []
            for dif in directions:
                if col + dif[0] >= 0 and col + dif[0] < max_col and row + dif[1] >= 0 and row + dif[1] < max_row:
                    if grid[col + dif[0]][row + dif[1]] == 0:
                        out.append((row + dif[1], col + dif[0]))
            return out                    

        if grid[0][0] != 0 or grid[max_col-1][max_row-1] != 0:
            return -1

        visited = set()
        queue = deque([(0, 0, 1)])
        visited.add((0, 0))
        while queue:
            row, col, distance = queue.popleft()
            if (row, col) == (max_row-1, max_col-1):
                return distance
            
            for neighbor in get_neighbors(row, col):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor[0], neighbor[1], distance + 1))

        return -1
