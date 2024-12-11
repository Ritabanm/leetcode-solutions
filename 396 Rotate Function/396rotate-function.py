class Solution:
    def maxRotateFunction(self,nums):
        n = len(nums)
        total = sum(nums)
        f = [0]*n
        for i,v in enumerate(nums):
            f[0]+=v*i
        for i in range(1,n):
            f[i]=f[i-1]+total-n*nums[n-i]
        return max(f)
"""class Solut0ion:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        F = [0]*n
        for i,v in enumerate(nums):
            F[0]+= v*i
        for i in range(1, n):
            F[i]=F[i-1]+total-n*nums[n-i]
        return max(F)"""