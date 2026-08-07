class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        mod = 1000000007
        
        @cache
        def dp(idx=0, gain=0, n=n):
            if idx == len(profit):
                return (gain == minProfit)
            
            ans = 0
            if n >= group[idx]:
                ans += dp(idx+1, min(gain+profit[idx], minProfit), n-group[idx]) 
                
            return (ans + dp(idx+1, gain, n))%mod
        
        dp.cache_clear()
        return dp()