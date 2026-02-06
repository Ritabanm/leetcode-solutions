class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        cnt, i = 1,0
        for j in range(n):
            while nums[j]>nums[i]*k:
                i+=1
            cnt = max(cnt, j-i+1)
        return n-cnt