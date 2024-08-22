class Solution:
    def maxSum(self, nums: List[int]) -> int:
        max_num = max(nums)

        if max_num<0:
            return max_num
        
        max_sum = sum({num for num in nums if num>0})
        return max_sum