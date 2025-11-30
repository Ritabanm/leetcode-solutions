from collections import Counter
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        counter = [0]*32
        for num in nums:
            for i in range(32):
                counter[i] += num & 1
                num = num >> 1
        res = 0
        for j, num in enumerate(nums):
            tmp = num
            for i in range(32):
                counter[i] -= tmp & 1
                tmp = tmp >> 1
            tmpres = 0
            for i in range(32):
                tmpres += (counter[i] > 0)*(1<<i)
            tmpres = tmpres | (num << k)
            res = max(res, tmpres)
            tmp = num
            for i in range(32):
                counter[i] += tmp & 1
                tmp = tmp >> 1
        return res