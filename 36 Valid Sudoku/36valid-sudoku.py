class Solution:
    def isValidSudoku(self, board):
        n = 9
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        box = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                val = board[r][c]
                #if pos has #
                if val =='.':
                    continue
                #check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                #check col
                if val in cols[c]:
                    return False
                cols[c].add(val)

                #check box
                idx = (r//3)*3+c//3
                if val in box[idx]:
                    return False
                box[idx].add(val)
        return True