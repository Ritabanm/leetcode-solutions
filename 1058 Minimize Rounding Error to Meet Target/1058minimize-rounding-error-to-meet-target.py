class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:
        err = []
        lo = hi = 0 
        for x in prices: 
            x = float(x)
            lo += floor(x)
            hi += ceil(x)
            if floor(x) < x < ceil(x): err.append(x - floor(x))
        if not lo <= target <= hi: return "-1" # impossible 
        
        err.sort()
        k = hi - target 
        return f"{len(err)-k+sum(err[:k])-sum(err[k:]):.3f}"