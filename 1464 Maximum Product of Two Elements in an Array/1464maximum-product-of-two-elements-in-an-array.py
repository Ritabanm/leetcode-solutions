class Solution:
    def maxProduct(self, nums):
        big = 0
        secondbig = 0
        for num in nums:
            if num>big:
                secondbig = big
                big = num
            else:
                secondbig = max(secondbig,num)
        return (big-1)*(secondbig-1)