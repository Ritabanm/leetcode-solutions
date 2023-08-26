class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx = [-float('inf'), -1]
        mn = [float('inf'), -1]
        n = len(nums)

        for i in range(n - indexDifference):
            if nums[i] > mx[0]:
                mx = [nums[i], i]
            if nums[i] < mn[0]:
                mn = [nums[i], i]
            j = i + indexDifference
            if abs(mx[0] - nums[j]) >= valueDifference:
                return [mx[1], j]
            if abs(mn[0] - nums[j]) >= valueDifference:
                return [mn[1],j]
        return [-1,-1]

        