class Solution:
    def missingElement(self, nums, k):
        n = len(nums)
        for i in range(1,n):
            missed_gap = nums[i]-nums[i-1]-1
            if missed_gap>=k:
                return nums[i-1]+k
            k -= missed_gap
        return nums[n-1]+k