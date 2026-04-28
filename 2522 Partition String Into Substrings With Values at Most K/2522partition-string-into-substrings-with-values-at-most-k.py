class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        if k < 10: return len(s) if k >= int(max(s)) else -1
        
        k, ans = str(k), 0
        digits = len(k)

        while s:
            s = s[digits:] if s[:digits] <= k else s[digits-1:]
            ans+= 1

        return ans