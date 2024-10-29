class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=[abs(i) for i in nums]
        nums.sort(reverse=True)
        k=len(nums)
        k1=0
        if k%2==0:
            k1=(k//2)-1
        else:
            k1=k//2
        s=0
        for i in range(len(nums)):
            if i<=k1:
                s+=(nums[i]*nums[i])
            else:
                s-=(nums[i]*nums[i])
        return s