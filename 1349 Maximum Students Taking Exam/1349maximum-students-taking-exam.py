class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        N = (1<<n)
        dp = [[-1]*N for i in range(m+1)]

        def getBits(x):
            res = 0
            while x:
                res += 1
                x = x & (x-1)
            return res

        def isValid(x):
            if (x & (x>>1)):
                return False
            return True

        for j in range(N):
            dp[0][j] = 0
        prev = 0
        ans = 0
        for i in range(1, m+1):
            mask = 0
            for j in range(n):
                if seats[i-1][j] == ".":
                    mask |= (1<<j)
        
            dp[i][0] = max(dp[i-1])
            submask = mask
            while submask > 0:
                if isValid(submask):
                    if dp[i-1][0] != -1:
                        dp[i][submask] = max(dp[i][submask], dp[i-1][0]+getBits(submask))
                        ans = max(ans, dp[i][submask])
                    curr = prev
                    while curr:
                        if not ((submask & (curr>>1)) or (submask & (curr<<1))):
                            if dp[i-1][curr] != -1:
                                dp[i][submask] = max(dp[i][submask], dp[i-1][curr]+getBits(submask))
                                ans = max(ans, dp[i][submask])
                        curr = (curr-1) & prev
                
                submask = (submask-1) & mask
            
            prev = mask
        return ans
            
                



        