"""class Solution(object):
    def runningSum(self, nums):
        if not nums:
            return []
        run_sum = []
        cur_sum = 0
        for num in nums:
            cur_sum+=num
            run_sum.append(cur_sum)
        return run_sum"""
    
class Solution(object):
    def runningSum(self, nums):
        if not nums or len(nums)==0:
            return []
        
        run_sum = []
        cur_sum = 0
        for num in nums:
            cur_sum+=num
            run_sum.append(cur_sum)
        return run_sum