class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0 
        while len(s) > 2: 
            lo = s.find(s[-1])
            hi = s.rfind(s[0])
            if lo < len(s)-hi-1: 
                ans += lo 
                s = s[:lo] + s[lo+1:-1]
            else: 
                ans += len(s)-hi-1
                s = s[1:hi] + s[hi+1:]
        return ans