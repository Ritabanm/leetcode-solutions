class Solution:
    def numSubseq(self, nums:List[int], target: int):
        n=len(nums)
        mod = 10**9+7
        nums.sort()
        ans = 0
        for left in range(n):
            right = bisect.bisect_right(nums,target-nums[left])-1
            if right>=left:
                ans += pow(2, right-left, mod)
        return ans%mod