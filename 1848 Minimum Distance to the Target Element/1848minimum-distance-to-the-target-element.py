class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if nums[start] == target:return 0
        i, j = start-1, start+1
        while j < len(nums) or i > -1:
            if i > -1:
                if nums[i] == target:
                    return start-i
                i -= 1
            if j < len(nums):
                if nums[j] == target:
                    return j-start
                j += 1