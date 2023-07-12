class Solution:
    def countStableSubarrays(self, capacity: list[int]) -> int:
        n = len(capacity)
        prefix = [0]*(n+1)
        for i, x in enumerate(capacity,1):
            prefix[i] = prefix[i-1] + x
        ans = 0
        cnt = {}
        for r in range(2, n):
            l = r - 2
            cnt[(capacity[l], prefix[l+1])] = cnt.get((capacity[l], prefix[l+1]), 0) + 1
            ans += cnt.get((capacity[r], prefix[r] - capacity[r]), 0)
        return ans