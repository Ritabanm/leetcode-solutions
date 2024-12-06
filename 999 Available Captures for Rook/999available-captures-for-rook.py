class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        n = 8
        for i in range(n):  # find rook location
            for j in range(n):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        
        res = 0
        for i in range(x-1, -1, -1):  # check north
            if board[i][y] == 'p':
                res += 1
                break
            if board[i][y] == 'B':
                break
        
        for i in range(x+1, n):  # check south
            if board[i][y] == 'p':
                res += 1
                break
            if board[i][y] == 'B':
                break
        
        for j in range(y-1, -1, -1):  # check west
            if board[x][j] == 'p':
                res += 1
                break
            if board[x][j] == 'B':
                break
        
        for j in range(y+1, n):  # check east
            if board[x][j] == 'p':
                res += 1
                break
            if board[x][j] == 'B':
                break
        
        return res