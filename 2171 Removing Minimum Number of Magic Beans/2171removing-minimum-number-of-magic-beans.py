class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        s = sum(beans)
        l = len(beans)
        res = float('inf')

        for i in range(len(beans)):
            res = min(res, s - l * beans[i])
            l -= 1
            
        return res