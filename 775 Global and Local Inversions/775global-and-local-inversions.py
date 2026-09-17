class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        floor = n
        for i in range(n-1, -1, -1):
            floor = min(floor, nums[i])
            if i>=2 and nums[i-2]>floor:
                return False
        return True