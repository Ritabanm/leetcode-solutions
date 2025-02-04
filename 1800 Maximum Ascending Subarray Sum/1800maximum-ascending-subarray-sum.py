class Solution:
    def maxAscendingSum(self, nums:List[int])-> int:

        result = 0
        cur_sum = nums[0]

        for i in range(1, len(nums)):

            if nums[i-1]<nums[i]:
                cur_sum += nums[i]
            else:
                result = max(result, cur_sum)
                cur_sum = nums[i]

        result = max(result, cur_sum)
        return result

        