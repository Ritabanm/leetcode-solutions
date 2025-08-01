class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        mod = 10**9+7
        if not 0<=k<=n-1:
            return 0
        return (2*math.comb(n-1,k))%mod