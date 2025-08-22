class Solution:
    def subarraysWithMoreOnesThanZeroes(self, nums: List[int]) -> int:
        MOD = 10**9+7
        counter = Counter()
        counter[0] = 1
        nums = [0] + [i if i == 1 else -1 for i in nums]
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
        upper = 0 #number sequences that ends at current postions whose ones is greater than zeros
        res = 0
        for i in range(1, n):
            if nums[i] == nums[i-1] + 1:
                upper += counter[nums[i]-1]
            else:
                upper -= counter[nums[i]]
            res += upper
            counter[nums[i]] += 1
        return res%MOD
