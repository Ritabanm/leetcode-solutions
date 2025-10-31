class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0]*n
        l = 0
        r = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[l])<abs(nums[r]):
                sq = nums[r]
                r-=1
            else:
                sq = nums[l]
                l+=1
            res[i] = sq*sq
        return res