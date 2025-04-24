from math import gcd

class Solution:
    def minStable(self, nums: list[int], maxC: int) -> int:
        n = len(nums)
        st = [[0]*n for _ in range((n+1).bit_length())]
        for i in range(n):
            st[0][i] = nums[i]
        idx = 1
        while (1 << idx) <= n:
            length = 1 << (idx-1)
            for i in range(n - (1<<idx) + 1):
                st[idx][i] = gcd(st[idx-1][i], st[idx-1][i+length])
            idx += 1
        sp = [0]*(n+2)
        for i in range(2, n+2):
            sp[i] = sp[i//2] + 1

        def rangeGCD(l, r):
            idx = sp[r-l+1]
            return gcd(st[idx][l], st[idx][r-(1<<idx)+1])

        def can(k):
            length = k+1
            if length > n:
                return True
            used = 0
            last = -1
            for i in range(n - length + 1):
                if rangeGCD(i, i+length-1) > 1:
                    if i > last:
                        used += 1
                        if used > maxC:
                            return False
                        last = i+length-1
            return True

        mini = n
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                mini = mid
                right = mid - 1
            else:
                left = mid + 1
        return mini