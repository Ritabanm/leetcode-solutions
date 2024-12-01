class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        min_cost = need1 * cost1 + need2 * cost2
        min_cost = min(min_cost, need1 * costBoth + max(0, (need2 - need1)) * cost2)
        min_cost = min(min_cost, need2 * costBoth + max(0, (need1 - need2)) * cost1)
        return min_cost