class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ans = 0
        n = len(nums)
        k = len(pattern)
        l = []
        for i in range(n-1):
            res = -1
            if nums[i+1]>nums[i]:
                res = 1
            elif nums[i+1]==nums[i]:
                res = 0
            l.append(res)
        for i in range(n-k):
            if l[i:i+k] == pattern:
                ans += 1
        return ans