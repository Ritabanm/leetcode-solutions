from math import gcd

class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n = len(nums)

        def score(skip):
            # build prefix and suffix gcd skipping index `skip`
            pre = [0] * (n + 1)
            suf = [0] * (n + 1)
            for i in range(1, n + 1):
                if i - 1 == skip:
                    pre[i] = pre[i - 1]
                else:
                    pre[i] = gcd(pre[i - 1], nums[i - 1])
            for i in range(n - 1, -1, -1):
                if i == skip:
                    suf[i] = suf[i + 1]
                else:
                    suf[i] = gcd(suf[i + 1], nums[i])
            cnt = 0
            for i in range(n - 1):
                if i == skip:
                    continue
                if pre[i + 1] == suf[i + 1]:
                    cnt += 1
            return cnt

        candidates = set()
        candidates.add(-1)  # remove nothing

        # prefix gcd breakpoints
        premain = [0] * (n + 1)
        for i in range(1, n + 1):
            premain[i] = gcd(premain[i - 1], nums[i - 1])
        for i in range(1, n + 1):
            if premain[i] != premain[i - 1]:
                candidates.add(i - 1)

        # suffix gcd breakpoints
        sufmain = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sufmain[i] = gcd(sufmain[i + 1], nums[i])
        for i in range(n):
            if sufmain[i] != sufmain[i + 1]:
                candidates.add(i)

        candidates.add(0)
        candidates.add(n - 1)

        ans = 0
        for skip in candidates:
            ans = max(ans, score(skip))
        return ans