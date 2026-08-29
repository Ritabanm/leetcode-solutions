"""class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = sum(nums)-sum(set(nums))
        miss = len(nums)*(len(nums)+1)//2-sum(set(nums))
        return [dup, miss]"""

class Solution:
    def findErrorNums(self, nums):
        dup = sum(nums)-sum(set(nums))
        miss = len(nums)*(len(nums)+1)//2-sum(set(nums))
        return [dup, miss]