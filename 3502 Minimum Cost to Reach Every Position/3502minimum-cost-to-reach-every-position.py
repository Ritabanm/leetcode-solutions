class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        stack = [cost[0]]
        res = [cost[0]]
        for i in range(1, len(cost)):
            if stack[-1]<cost[i]:
                res.append(stack[-1])
            else:
                res.append(cost[i])
                stack.append(cost[i])
        return res