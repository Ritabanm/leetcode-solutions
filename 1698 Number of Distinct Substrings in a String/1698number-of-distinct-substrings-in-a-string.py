class Solution:
    def countDistinct(self, s: str) -> int:
        root = {}
        ans = 0
        n = len(s)
        for i in range(n):
            curr = root
            for j in range(i,n):
                ch = s[j]
                if(ch not in curr):
                    curr[ch] = {}
                    ans+=1
                curr = curr[ch]
        return ans
