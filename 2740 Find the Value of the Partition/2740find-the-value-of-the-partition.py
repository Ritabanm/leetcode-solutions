class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[-1]
        for i in range(len(nums)-1):
            m = min(m, abs(nums[i]-nums[i+1]))
        return m