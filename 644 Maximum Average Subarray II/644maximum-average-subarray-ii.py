class Solution:
    def findMaxAverage(self, nums, k):
        n = len(nums)

        def function(x):
            total = 0 

            for i in range(k):
                total += nums[i]-x 

            if total >= 0:
                return True 

            prev_total, prev_min = 0, 0 

            for i in range(k,n):
                total += nums[i]-x 
                prev_total += nums[i-k]-x 
                prev_min = min(prev_min,prev_total)

                if total >= prev_min:
                    return True 

            return False 

        low, high = min(nums), max(nums)

        while high - low >= 10**-6:
            mid = (low+high)/2 

            if function(mid):
                low = mid 
            else:
                high = mid 

        return low 