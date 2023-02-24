class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        max_pre = {}
        max_post = {}
        for idx in range(n):
            max_pre[idx] = -inf
            max_post[idx] = -inf

        for i in range(n-1):
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    max_pre[j] = max(max_pre[j], profits[i])
                    max_post[i] = max(max_post[i], profits[j])
        
        ans = -1
        for i, p in enumerate(profits):
            if max_pre[i] == -inf or max_post[i] == -inf:
                continue
            ans = max(ans, p + max_pre[i] + max_post[i])
        
        return ans