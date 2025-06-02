class Solution:
    def minFlipsMonoIncr(self, s):
        ans = 0
        num = 0
        for c in s:
            if c=='0':
                ans = min(num, ans+1)
            else:
                num+=1
        return ans