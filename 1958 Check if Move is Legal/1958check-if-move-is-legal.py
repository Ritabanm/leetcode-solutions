class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        nrows = len(board)
        ncols = len(board[0])

        directions = [
            [1, 0], [-1, 0], [0, 1], [0, -1],
            [1, 1], [-1, 1], [1, -1], [-1, -1]
        ]

        def dfs(r, c, l, dir):

            if r < 0 or r >= nrows or c < 0 or c >= ncols or board[r][c] == '.':
                return False


            if color == board[r][c] and l >= 3:
                return True

            if color == board[r][c] and l != 1:
                return False
            
            dr, dc = dir
            nr, nc = r + dr, c + dc

            return dfs(nr, nc, l + 1, dir)


        board[rMove][cMove] = color

        for dir in directions:
            if dfs(rMove, cMove, 1, dir):
                return True
        
        return False

        