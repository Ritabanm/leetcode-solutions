class Solution:
    def movesToMakeZigzag(self, nums):
        nums = [float("inf")] + nums + [float("inf")]

        n, mv1, mv2 = len(nums), 0, 0

        for i in range(1,n-1,2):
            if nums[i] >= min(nums[i-1],nums[i+1]):
                mv1 += nums[i] - min(nums[i-1],nums[i+1]) + 1 

        for i in range(2,n-1,2):
            if nums[i] >= min(nums[i-1],nums[i+1]):
                mv2 += nums[i] - min(nums[i-1],nums[i+1]) + 1 

        return min(mv1,mv2)