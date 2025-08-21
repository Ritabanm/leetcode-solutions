class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i in range(len(s)):
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
                
        ans = 0
        nums.sort()
        mod = 10 ** 9 + 7
        s = 0
        
        for i in range(len(nums)):
            ans += (nums[i] * i - s)
            s += nums[i]
            ans %= mod
            s %= mod
        
        return ans % mod