class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False
        used = [0 for i in range(26)]
        for i in range(len(s)):
            if s[i] != t[i]:
                curr = ord(t[i]) - ord(s[i])        
                if curr<0:
                    curr += 26
                if (used[curr]*26)+curr<=k:
                    used[curr] += 1
                else:
                    return False             
        return True

        