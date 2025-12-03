class Solution:
    def longestCommonPrefix(self, s: str, t: str) -> int:
        j = 0
        for i in range(len(s)):
            if j<len(t) and s[i]==t[j]:
                j+=1
            elif i==j:
                continue
            else:
                break
        return j