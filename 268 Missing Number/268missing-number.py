class Solution:
    def missingNumber(self, nums):

        if not nums:
            return []
        
        n = len(nums)


        expected_sum = n*(n+1)//2
        current_sum = sum(nums)

        return expected_sum-current_sum

