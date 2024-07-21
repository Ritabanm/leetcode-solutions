def isNondecreasing(nums):
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                return False
        return True

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while not isNondecreasing(nums):
            n = len(nums)
            idx = 0
            minsum = 100000
            for i in range(0, n-1):
                if nums[i] + nums[i+1] < minsum:
                    minsum = nums[i] + nums[i+1]
                    idx = i

            nums[idx] = nums[idx] + nums[idx+1]
            del nums[idx+1]
            ans+=1

        return ans
        # Time O(n^2)
        # Space O(1)