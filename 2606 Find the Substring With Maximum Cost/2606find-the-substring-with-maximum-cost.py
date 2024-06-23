class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        nums = []
        c = {i: idx for idx, i in enumerate(chars)}
        
        for i in s:
            if i in c:
                nums.append(vals[c[i]])
            else:
                nums.append(ord(i) - ord('a') + 1)
        
        res =0
        total = 0
        
        for i in nums:
            total += i
            res = max(res, total)
            
            if total < 0:
                total = 0
                
        return res           