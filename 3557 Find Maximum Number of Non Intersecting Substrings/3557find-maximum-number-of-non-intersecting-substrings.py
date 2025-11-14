class Solution:
    def maxSubstrings(self, word: str) -> int:

        ans = 0
        prev = defaultdict(int)          

        for idx, ch in enumerate(word):

            if ch not in prev:          # <-- 1
                prev[ch] = idx
                 
            elif idx >= prev[ch] + 3:   # <-- 2
                prev.clear()
                ans+= 1
                
        return ans