class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        numsEven = sorted(x for x in nums if x % 2 == 0)
        targEven = sorted(x for x in target if x % 2 == 0)
        numsOdd = sorted(x for x in nums if x % 2)
        targOdd = sorted(x for x in target if x % 2)
        cnt = 0
        for n, t in zip(numsEven, targEven):
            if n > t:
                cnt += n - t
        for n, t in zip(numsOdd, targOdd):
            if n > t:
                cnt += n - t
        return cnt // 2