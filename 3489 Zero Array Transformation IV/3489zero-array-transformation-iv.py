class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        if max(nums) == 0: return 0    
        ans = -1
        
        for idx, num in enumerate(nums):
            cnts = {num}
            
            for pos, (beg, end, val) in enumerate(queries):
                if beg <= idx <= end:
                    shift = {x - val for x in cnts if x >= val}
                    cnts|= shift

                if 0 in cnts:
                    ans = max(ans, pos + 1)
                    break
            
            if 0 not in cnts:
                return -1
        
        return ans