class Solution:
    def countTheNumOfKFreeSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mx = max(nums)
        data = defaultdict(int)
        nums.sort()
        for i in nums:
            data[i] = 1
        for i in range(n):
            mult = 1
            while nums[i] + mult * k in data and nums[i] + mult * k <= mx:
                data[nums[i]] += 1
                del data[nums[i] + mult * k]
                mult += 1

        product = 1
        for key in data:
            sz = data[key]
            dp = [0] * (sz + 1)
            dp[0] = 1
            dp[1] = 2
            for i in range(2, sz + 1):
                dp[i] = dp[i - 2] + dp[i - 1]
            product *= (dp[sz])
        return product


        