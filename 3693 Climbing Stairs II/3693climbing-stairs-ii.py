class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        b1 = b2 = b3 = 0
        for stepCost in costs:
            minCost = min(b1+1, b2+4,b3+9)
            b1,b2,b3 = stepCost + minCost, b1, b2
        return b1