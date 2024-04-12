class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        return [ nums[idx-1]|nums[idx] for idx in range(1,len(nums))]