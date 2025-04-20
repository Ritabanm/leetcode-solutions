class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        res = 0
        p = (n+1)//2 # start of leaves level
        while p > 1:
            i = p
            while i < 2*p:
                res += abs(cost[i-1]-cost[i]) # equalize the children nodes
                cost[i//2 - 1] += max(cost[i-1], cost[i]) # add cost of chidren to parent
                i += 2 # move to next pair of left/right nodes
            p //= 2 # go one level up
        return res        