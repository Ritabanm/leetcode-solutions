class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        n = len(nextVisit)
        dp = [[0]*2 for i in range(n)]
        dp[0][0]=0
        dp[0][1]=1
        
        for i in range(1,n):
            dp[i][0]=dp[i-1][1]+1
            dp[i][1]=(2*dp[i][0]-(dp[min(nextVisit[i], i)][0])+1)%(10**9+7)
        return dp[n-1][0]%(10**9+7)