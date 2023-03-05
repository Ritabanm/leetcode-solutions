class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        pn, pI , mn = 0,0, inf
        for i, num in enumerate(nums):
            if num==0:
                continue
            if pn == 3-num and i-pI<mn:
                mn = i-pI
            pn, pI = num, i
        return mn if mn!=inf else -1