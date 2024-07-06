class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        rows = []

        for i in range(m):
            rows+=nlargest(3, [(board[i][j], i, j) for j in range(n)])
        cols = []

        for j in range(n):
            cols +=nlargest(3, [(board[i][j], i, j) for i in range(m)])
        
        vals = nlargest(11, set(rows) & set(cols))

        res = float("-inf")

        for x, y, z in combinations(vals, 3):
            if len({x[1], y[1], z[1]})==3 and len({x[2], y[2], z[2]})==3:
                res = max(res, x[0] + y[0] + z[0])
        return res