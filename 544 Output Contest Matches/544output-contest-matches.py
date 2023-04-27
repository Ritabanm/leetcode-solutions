class Solution:
    def findContestMatch(self, n: int) -> str:
        ans = [str(x) for x in range(1, n+1)]
        while len(ans) > 1: 
            n = len(ans)
            for i in range(n//2): 
                ans[i] = f"({ans[i]},{ans[n-i-1]})"
                ans.pop()
        return ans[0]