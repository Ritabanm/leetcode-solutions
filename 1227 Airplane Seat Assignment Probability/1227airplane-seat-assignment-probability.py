import sys
sys.setrecursionlimit(10**6)

from functools import lru_cache

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        
        @lru_cache(None)
        def sn(k): 
            if k <= 1: return 1
            return (k+1)/k*sn(k-1)
        
        return sn(n-1)/n