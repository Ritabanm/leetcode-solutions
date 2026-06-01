"""class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost = sorted(cost, reverse = True)
        i = 0
        output = 0
        while i<len(cost):
            output+= cost[i] if i==len(cost)-1 else cost[i]+cost[i+1]
            i+=3
        return output"""

class Solution:
    def minimumCost(self, cost):
        cost = sorted(cost, reverse = True)
        i = 0
        o = 0
        while i<len(cost):
            o+= cost[i] if i==len(cost)-1 else cost[i]+cost[i+1]
            i+=3
        return o
