class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        mod = 10**9+7
        import math
        total_ways = math.comb(n-1,k-1)%mod
        odd_ways =0
        if (n-k)%2==0:
            sum_x = (n-k)//2
            odd_ways = math.comb(sum_x+k-1,k-1)%mod
        ans = (total_ways-odd_ways)%mod
        return ans