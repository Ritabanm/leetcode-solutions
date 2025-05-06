class Solution:
    def absDifference(self, nums,k):
        ans = 0
        nums.sort()
        for i in range(k):
            ans+=nums[~i]-nums[i]
        return ans