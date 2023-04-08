class Solution:
    def separateDigits(self, nums):
        res = []
        for i in range(len(nums)-1,-1,-1):
            x = nums[i]
            while x>0:
                res.append(x%10)
                x//=10
        res.reverse()
        return res