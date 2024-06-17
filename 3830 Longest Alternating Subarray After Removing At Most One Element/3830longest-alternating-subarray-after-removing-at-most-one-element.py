class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        Ld = [1] * n
        Li = [1] * n
        Rd = [1] * n
        Ri = [1] * n

        for i in range(1, n):
            Li[i] = (Ld[i-1]+1) if nums[i]>nums[i-1] else 1
            Ld[i] = (Li[i-1]+1) if nums[i]<nums[i-1] else 1
            
        for i in range(n-1, 0, -1):
            Ri[i-1] = (Rd[i]+1) if nums[i-1]>nums[i] else 1
            Rd[i-1] = (Ri[i]+1) if nums[i-1]<nums[i] else 1   

        ans = 0
        for i in range(n):
            ans = max(ans, Li[i]+Ri[i]-1, Rd[i]+Ld[i]-1)

        for i in range(1, n-1):
            ans = max(ans, 
                      Li[i-1]+Rd[i+1] if nums[i-1] > nums[i+1] else 0,
                      Ld[i-1]+Ri[i+1] if nums[i-1] < nums[i+1] else 0,
                      
                     )

        return ans