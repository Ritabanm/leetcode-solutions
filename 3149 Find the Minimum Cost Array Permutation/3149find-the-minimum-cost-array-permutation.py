class Solution:
    def solve(self, last, mask, nums, dp, track):
        n = len(nums)
        if mask == (1 << n) - 1:
            return abs(last - nums[0])
        if dp[mask][last] != -1:
            return dp[mask][last]
        mini = float('inf')
        for i in range(n):
            if mask & (1 << i):
                continue
            val = abs(last - nums[i]) + self.solve(i, mask ^ (1 << i), nums, dp, track)
            if val < mini:
                mini = val
                dp[mask][last] = mini
                track[mask][last] = i
        return dp[mask][last]

    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [[-1] * n for _ in range(1 << n)]
        track = [[-1] * n for _ in range(1 << n)]
        self.solve(0, 1, nums, dp, track)
        ans = [0]
        mask, l = 1, 0
        for _ in range(1, n):
            lc = track[mask][l]
            mask |= (1 << lc)
            ans.append(lc)
            l = lc
        return ans