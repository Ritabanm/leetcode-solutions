from functools import cache
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cost1, cost2 = max([cost1,cost2]), min(cost1,cost2)
        count = 0
        while total >= 0:
            count += total // cost2 +1
            total -= cost1
        return count