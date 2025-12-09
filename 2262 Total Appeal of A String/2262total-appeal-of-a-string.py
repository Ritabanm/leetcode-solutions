class Solution:
    def appealSum(self, s: str) -> int:
        last = collections.defaultdict(lambda: 0)
        curAppeal = totalAppeal = 0
        for i, c in enumerate(s):
            curAppeal += i + 1 - last[c]
            last[c] = i + 1
            totalAppeal += curAppeal
        
        return totalAppeal