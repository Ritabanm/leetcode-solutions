class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            k = i+2
            for j in range(i+1, len(nums)):
                while k < len(nums) and nums[i] + nums[j] > nums[k]: k += 1
                if j < k: ans += k-1-j
        return ans 