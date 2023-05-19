class Solution:
    def longestBalanced(self, s: str) -> int:
        r = 0
        for i in range(len(s)):
            f ={}
            for j in range(i, len(s)):
                f[s[j]] = f.get(s[j], 0)+1
                v = list(f.values())
                if min(v)==max(v):
                    r = max(r, j-i+1)
        return r