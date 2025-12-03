class Solution:
    def lexSmallest(self, s: str) -> str:
        ans = "z"+s
        for i in range(len(s)):
            if s[:i][::-1]+s[i:]<ans:
                ans = s[:i][::-1]+s[i:]
            if s[:i]+s[i:][::-1]<ans:
                ans = s[:i]+s[i:][::-1]
        return ans