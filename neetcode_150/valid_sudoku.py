class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2) * 3 = O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for x in range(9):
            for y in range(9):
                val = board[x][y]
                if val != ".":
                    if val in rows[x] or val in cols[y] or val in squares[(x//3, y//3)]:
                        return False
                    rows[x].add(val)
                    cols[y].add(val)
                    squares[(int(x/3), int(y/3))].add(val)
        return True