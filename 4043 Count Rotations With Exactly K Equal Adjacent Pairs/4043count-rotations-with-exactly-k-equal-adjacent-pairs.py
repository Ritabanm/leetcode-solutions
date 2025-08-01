class Solution:
    def countRotations(self, s: str, k: int) -> int:
        count = 0
        for i in range(len(s)):
            r = s[i:]+s[:i]
            a = 0
            for j in range(len(r)-1):
                if r[j]==r[j+1]:
                    a+=1
            if a==k:
                count+=1
        return count