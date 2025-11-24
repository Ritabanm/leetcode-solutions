class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        vals = list(map(int, str(n)))
        
        @cache
        def fn(i, m, on): 
            """Return count at index i with mask m and profile flag (True/False)"""
            ans = 0 
            if i == len(vals): return 1
            for v in range(vals[i] if on else 10 ): 
                if m & 1<<v == 0: 
                    if m or v: ans += fn(i+1, m ^ 1<<v, False)
                    else: ans += fn(i+1, m, False)
            if on and m & 1<<vals[i] == 0: ans += fn(i+1, m ^ 1<<vals[i], True)
            return ans 
        
        return fn(0, 0, True)-1