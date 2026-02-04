
class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minp = float("inf")
        maxp = 0
        for i in range(len(prices)):
            if prices[i]<minp:
                minp = prices[i]
            elif prices[i]-minp>maxp:
                maxp = prices[i]-minp
        return maxp