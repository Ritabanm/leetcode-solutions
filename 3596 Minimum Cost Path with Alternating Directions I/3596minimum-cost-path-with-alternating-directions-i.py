class Solution:
    def minCost(self, m: int, n: int) -> int:
        sm = m+n
        if sm==3:
            return 3
        if sm==2:
            return 1
        return -1