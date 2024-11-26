"""
- edit in place
- recursive function for unrevealed sques
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
            movements = [(0,1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1,-1)]
            
            def numMines(x, y) -> int:
                out = 0
                for x_move, y_move in movements:
                    a, b = x + x_move, y + y_move
                    if 0 <= a < len(board) and 0 <= b < len(board[0]) and board[a][b] == "M":
                        out += 1 
                return out

            visited = set()
            def reveal(x, y):
                for x_move, y_move in movements:
                    a, b = x + x_move, y + y_move
                    if (a,b) not in visited and 0 <= a < len(board) and 0 <= b < len(board[0]):
                        visited.add((a,b))
                        if board[a][b] != "M":
                            check(a, b)
                            
            def check (a, b):
                mines = numMines(a, b)
                if mines > 0:
                    board[a][b] = str(mines)
                else:
                    board[a][b] = "B"
                    reveal(a, b)

            x, y = click
            if board[x][y] == "M":
                board[x][y] = "X"
            elif board[x][y] == "E":
                check(x, y)

            return board