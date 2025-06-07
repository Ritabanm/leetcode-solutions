class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        maxPre = nums[0]
        minNums = nums[-1]
        minPost = [0]*(n-1)
        for i in range(n-2, 0, -1):
            minPost[i] = minNums
            if nums[i] < minNums:
                minNums = nums[i]
        for i in range(1, n-1):
            if nums[i] > maxPre and nums[i] < minPost[i]:
                ans += 2
            elif nums[i] > nums[i-1] and nums[i] < nums[i+1]:
                ans += 1
            if nums[i] > maxPre:
                maxPre = nums[i]
        return ans