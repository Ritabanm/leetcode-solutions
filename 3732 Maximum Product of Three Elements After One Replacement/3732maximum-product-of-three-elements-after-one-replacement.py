class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=-nums[i]
        nums.sort()
        return nums[-1]*nums[-2]*(10**5)