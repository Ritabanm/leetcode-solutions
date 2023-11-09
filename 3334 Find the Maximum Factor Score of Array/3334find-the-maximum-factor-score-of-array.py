class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n, ctr = len(nums), Counter(nums)
        mx = gcd(*nums)*lcm(*nums)
        if n>1:
            for i in range(n):
                if ctr[nums[i]]>1: 
                    continue
                arr = nums[:i] + nums[i+1:]
                mx = max(mx, gcd(*arr)*lcm(*arr))
        return mx
        