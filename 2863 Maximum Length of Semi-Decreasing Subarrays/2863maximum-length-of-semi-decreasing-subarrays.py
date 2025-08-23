class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
            
            n, ans = len(nums), 0
            pref = list(accumulate(nums, max))

            for right in range(n-1,-1,-1):
                if ans > right: break
                if nums[right] >= pref[-1]: continue

                left = bisect_left(pref, nums[right]+1)
                ans = max(ans, right-left+1)
                
            return ans