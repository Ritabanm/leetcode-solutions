class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)
        if n==0:
            return -1

        suf_min = [0]*n
        suf_min[-1] = nums[-1]

        for i in range(n-2,-1, -1):
            suf_min[i] = min(suf_min[i+1], nums[i])
        cur_max = -float('inf')
        for i in range(n):
            cur_max = max(cur_max, nums[i])
            if cur_max - suf_min[i]<=k:
                return i
        return -1