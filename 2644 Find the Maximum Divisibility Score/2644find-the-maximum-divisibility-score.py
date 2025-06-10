class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = 0 
        count = -1
        for d in divisors:
            curr = sum(1 for i in nums if i%d == 0)
            if curr > count:
                count = curr
                res = d
            elif curr == count:
                res = min(res, d)
        return res