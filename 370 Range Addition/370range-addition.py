class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        
        for update in updates:
            begin, end, val = update
            
            res[begin] += val
            
            if end + 1 < len(res):
                res[end + 1] -= val
                
                
        for i in range(1, length):
            res[i] += res[i - 1]
            
        return res