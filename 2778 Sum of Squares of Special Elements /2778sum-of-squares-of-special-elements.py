class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        tot =0
        n = len(nums)
        for i in range(1,n+1):
            if n%i==0:
                tot +=nums[i-1]**2
        return tot
        