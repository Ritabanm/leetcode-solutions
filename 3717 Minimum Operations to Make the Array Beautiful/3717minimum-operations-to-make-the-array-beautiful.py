class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @cache
        def go(prev, idx):
            if idx == len(nums):
                return 0
            if nums[idx] <= prev:
                return prev - nums[idx] + go(prev, idx+1)
            res = inf
            for i in range(51):
                if prev * i < nums[idx]: continue
                diff = prev * i - nums[idx]
                res = min(res, go(prev * i, idx+1) + diff)
            return res

        return go(nums[0], 1)
