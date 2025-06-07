class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        ans = len(nums)
        i = 0
        j = (length + 1) // 2

        while i < length // 2 and j < length:
            if nums[i] < nums[j]:
                ans -= 2
            i += 1
            j += 1

        return ans