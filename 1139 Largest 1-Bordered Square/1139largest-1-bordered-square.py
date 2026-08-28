class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        # want largest square subgrid: min(R,C) side length
        # max(R,C)-min(R,C)+1 different offsets in other direction

        # Reread problem, a lot easier than I thought (we're not counting
        # number of 1-bordered squares in the largest square) - we want
        # the size of the largest 1-bordered square

        # the grid already gives us the size of 1x1 squares
        # DP?
        #    for x 1 1 1 1 1
        #        1     1
        #        1     1
        #        1 1 1 1       4x4

        # if we knew
        #   x has 6 left and 4 down ones, including x
        #   So max grid size at x is 4x4
        #   We can look at right[x + (3,0)] -> get 4
        #   and look at down[x + (0,3)] -> get 4
        # so we have a 4x4

        # For a MxN grid, the max number of 1s at any cell would be O(M) down and O(N) right
        # for each one we'd do O(min(M,N)) ops
        # so if shorter axis is M and longer is N, then we'd do O(MN) iterations, and O(M) ops per iteration
        
        # Can we go faster? I don't think so, but I have no proof.

        # foo[r][c] is number of consec. 1s, including (r,c),  right/down starting at (r,c)
        right = [[0]*C for _ in range(R)]
        down = [[0]*C for _ in range(R)]

        for r in range(R):
            right[r][C-1] = grid[r][C-1]
            for c in range(C-2, -1, -1):
                if grid[r][c]:
                    right[r][c] = right[r][c+1] + 1
                # else: leave it zero

        for c in range(C):
            down[R-1][c] = grid[R-1][c]
            for r in range(R-2, -1, -1):
                if grid[r][c]:
                    down[r][c] = down[r+1][c] + 1

        L = min(R,C)
        best = 0
        for r in range(R):
            # break early if we can't improve on the best; new best would need row index >= r+(best+1)-1
            if r+best >= R: break
            for c in range(C-best):
                longest = min(down[r][c], right[r][c])
                # only candidates > best can change the answer
                for l in range(longest, best, -1):
                    if right[r+l-1][c] >= l and down[r][c+l-1] >= l:
                        best = l
                        break
        
        return best**2 # FIX: area, not side length