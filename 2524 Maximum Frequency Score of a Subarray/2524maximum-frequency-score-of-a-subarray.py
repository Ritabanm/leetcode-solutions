from collections import Counter
class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        counter = Counter(nums[:k])
        res = 0
        MOD = 10**9 + 7
        for c in counter:
            res = (res + pow(c, counter[c], MOD)) % MOD
        cur = res
        for i in range(k, len(nums)):
            v = nums[i]
            cur = (cur - pow(nums[i-k], counter[nums[i-k]], MOD)) % MOD
            counter[nums[i-k]] -= 1 
            if counter[nums[i-k]]:
                cur = (cur + pow(nums[i-k], counter[nums[i-k]], MOD)) % MOD
            if counter[v]:
                cur = (cur - pow(v, counter[v], MOD)) % MOD
            counter[v] += 1 
            cur = (cur + pow(v, counter[v], MOD)) % MOD  
            res = max(res, cur)
        return res