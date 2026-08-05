class Solution:
    def minCostClimbingStairs(self, cost):
        #Edge: if cost is empty list.
        if not cost:
            return 0
        
        #Cost of last 2 steps.
        prev = cost[0]
        curr = cost[1]

        """
        Algorithm:
        1. Check each step from step 2 to end of list.
        2. next step = cost at current + min cost to prev.
        3. return min cost.
        """

        for i in range(2, len(cost)):
            ns = cost[i]+min(prev, curr)
            prev, curr = curr, ns
        return min(prev,curr)


        #Time: O(n), Space: O(1)

        