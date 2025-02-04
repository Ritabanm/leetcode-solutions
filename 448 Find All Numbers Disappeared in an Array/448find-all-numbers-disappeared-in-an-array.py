class Solution(object):
    def findDisappearedNumbers(self,nums):
        for i in range(len(nums)):
            new_index = abs(nums[i])-1
            if nums[new_index]>0:
                nums[new_index]*=-1
        result = []
        for i in range(1, len(nums)+1):
            if nums[i-1]>0:
                result.append(i)
        return result