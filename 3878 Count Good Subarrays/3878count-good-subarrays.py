class Solution:
    def countGoodSubarrays(self, nums: list[int]) -> int:

        n = len(nums)
        ri = [[]]*n
        tp = [n]*30
        for i in range(n-1, -1, -1):
            ri[i] = tp[:]
            x = nums[i]
            j = 0
            while x:
                if x&1: tp[j] = i
                x >>= 1
                j += 1

        le = [[]] * n
        tp = [-1] * 30
        for i in range(n):
            le[i] = tp[:]
            x = nums[i]
            j = 0
            while x:
                if x & 1: tp[j] = i
                x >>= 1
                j += 1

        # print(le, ri)
        mp = {}
        res = 0
        for i in range(n):
            l, r = -1, n
            for j in range(30):
                if 1<<j&nums[i]: continue
                l = max(l, le[i][j])
                r = min(r, ri[i][j])
            if nums[i] in mp: l = max(l, mp[nums[i]])
            a, b = r-i, i-l
            # if nums[i] in mp and mp[nums[i]] == r: continue
            mp[nums[i]] = i
            res += a*b
        return res