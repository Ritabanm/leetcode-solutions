class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m,n=len(grid),len(grid[0])
        if (m+n-1)&1:
            return False
        @cache
        def dfs(i,j,k):
            if grid[i][j]=='(':
                k+=1
            else:
                if k>0:
                    k-=1
                else:
                    return False
            if i==m-1 and j==n-1:
                return k==0
            l=r=False
            if i+1<m:
                l=dfs(i+1,j,k)
            if j+1<n:
                r=dfs(i,j+1,k)
            return l|r
        return dfs(0,0,0)    