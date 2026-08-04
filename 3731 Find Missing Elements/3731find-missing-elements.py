"""class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        start,end = nums[0], nums[-1]
        s = set(nums)
        return [i for i in range(start,end+1) if i not in s]"""


class Solution:
    def findMissingElements(self, nums):
        if not nums:
            return []
        
        nums.sort()
        start, end = nums[0], nums[-1]
        s = set(nums)
        return [i for i in range(start, end +1) if i not in s]