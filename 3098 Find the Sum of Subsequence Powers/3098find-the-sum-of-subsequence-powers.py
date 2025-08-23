class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        ans = 0
        @cache
        def dp(idx, min_diff, last_choose, left_k):
            if left_k == 0:
                if min_diff != inf:
                    return min_diff
                else:
                    return 0
            if idx == len(nums):
                return 0
            choose = dp(idx+1, min(min_diff, abs(last_choose-nums[idx])), nums[idx], left_k-1)
            not_choose = dp(idx+1, min_diff, last_choose, left_k)
            return (choose + not_choose) % MOD
        return dp(0, inf, inf, k)