class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        l = 1
        ans = 0
        for i in range(1,n):
            if prices[i] == prices[i-1]-1:
                l += 1
            else:
                ans += (l+1)*l//2
                l = 1

        ans += (l+1)*l//2
        return ans
