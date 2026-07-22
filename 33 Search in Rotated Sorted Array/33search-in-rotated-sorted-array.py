class Solution:
    def search(self,nums, target):
        n = len(nums)
        l = 0
        r = len(nums)-1
        while l<=r:
            m = l+(r-l)//2
            #Case 1:find target
            if nums[m]==target:
                return m
            
            #Case 2: subarray
            elif nums[m]>=nums[l]:
                if target>=nums[l] and target<nums[m]:
                    r = m-1
                else:
                    l=m+1
            else:
                if target<=nums[r] and target>nums[m]:
                    l = m+1
                else:
                    r = m-1
        return -1