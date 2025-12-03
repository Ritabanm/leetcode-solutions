class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        h = [(0,n)]
        for i in range(n-1,-1,-1):
            while h and h[0][1]>2*(i+1):
                heappop(h)
            res = h[0][0] + prices[i]
            heappush(h, (res,i))
        return res