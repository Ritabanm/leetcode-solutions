class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)
        res = score = 0

        def getScore(arr):
            m = len(arr)
            if m <= 1:
                return 0

            pref = [0] * m
            suff = [0] * m

            curr = 0
            for i in range(m):
                curr = math.gcd(curr, arr[i])
                pref[i] = curr

            curr = 0
            for i in range(m - 1, -1, -1):
                curr = math.gcd(curr, arr[i])
                suff[i] = curr

            splits = 0
            for i in range(m - 1):
                if pref[i] == suff[i + 1]:
                    splits += 1

            return splits

        res = getScore(nums)
        for j in range(0, n):
            t = nums[:j] + nums[j + 1:]
            res = max(res, getScore(t))

        return res