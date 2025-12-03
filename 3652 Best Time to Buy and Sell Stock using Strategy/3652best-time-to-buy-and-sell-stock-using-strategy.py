class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        n = len(prices)
        profit = sum(map(mul, prices, strategy))                # <-- 1)

        newProf = profit
        for idx in range(k):                                    # <-- 2)
            newProf-= strategy[idx] * prices[idx]
            if idx >= k // 2:
                newProf+= prices[idx]

        if newProf > profit: profit = newProf

        for idx in range(n - k):
            newProf-= (strategy[idx+k] - 1) * prices[idx+k]     # <-- 3a)
            newProf+= strategy[idx] * prices[idx]               # <-- 3b)
            newProf-= prices[idx + k // 2]                      # <-- 3c)

            if newProf > profit: profit = newProf

        return profit