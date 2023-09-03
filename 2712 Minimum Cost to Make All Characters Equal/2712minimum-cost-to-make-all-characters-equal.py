class Solution:
    def minimumCost(self, s: str) -> int:
        n, ans =len(s),0
        for i in range(1,(n+1)//2):
            ans+=(s[i]!=s[i-1])*i
        for i in range((n+1)//2,n):
            ans+=(s[i]!=s[i-1])*(n-i)
        
        return ans