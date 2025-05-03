class Solution:
    def minIncrements(self, s: str, start: int) -> int:
        n = len(s)
        
        ans = 0
        
        for i in range(n // 2):
            incs = abs(ord(s[(start+i)%n]) - ord(s[start-1-i]))
            ans += min(incs, 26 - incs)
            
        return ans
            
    def minOperations(self, s: str) -> int:
        return min(i + self.minIncrements(s, i) for i in range(len(s)))