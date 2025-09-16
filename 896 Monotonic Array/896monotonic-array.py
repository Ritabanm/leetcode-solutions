class Solution:
    def isMonotonic(self,  nums):
        incr = decr = True

        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                incr = False
            if nums[i]>nums[i+1]:
                decr = False
        
        return incr or decr

        


        