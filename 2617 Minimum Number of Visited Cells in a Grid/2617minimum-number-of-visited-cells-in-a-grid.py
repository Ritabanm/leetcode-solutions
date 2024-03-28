class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        dp = [[float('inf')]*m for i in range(n)]
        row_stacks = [[n-1] for i in range(m)]
        col_stacks = [[m-1] for i in range(n)]
        dp[n-1][m-1] = 1
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if (i,j) == (n-1,m-1): continue
                last = -1
                while row_stacks[j] and row_stacks[j][-1]<=i+grid[i][j]:
                    last = row_stacks[j].pop()
                if last!=-1:
                    dp[i][j] = dp[last][j]+1
                    row_stacks[j].append(last)
                last = -1
                while col_stacks[i] and col_stacks[i][-1]<=j+grid[i][j]:
                    last = col_stacks[i].pop()
                if last!=-1:
                    dp[i][j] = min(dp[i][j],dp[i][last]+1)
                    col_stacks[i].append(last)
                while row_stacks[j] and dp[row_stacks[j][-1]][j] >= dp[i][j]:
                    row_stacks[j].pop()
                while col_stacks[i] and dp[i][col_stacks[i][-1]] >= dp[i][j]:
                    col_stacks[i].pop()
                row_stacks[j].append(i)
                col_stacks[i].append(j)
                
        return dp[0][0] if dp[0][0]<float('inf') else -1
                
        
        