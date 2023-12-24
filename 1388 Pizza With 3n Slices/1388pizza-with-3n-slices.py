class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        @cache
        def fn(i, k, first): 
            """Return max sum of k pieces from slices[i:]."""
            if k == 0: return 0 
            if i >= len(slices) or first and i == len(slices)-1: return -inf 
            if i == 0: return max(fn(i+1, k, False), slices[i] + fn(i+2, k-1, True))
            return max(fn(i+1, k, first), slices[i] + fn(i+2, k-1, first))
        
        return fn(0, len(slices)//3, None)