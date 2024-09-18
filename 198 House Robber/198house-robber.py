class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        maxRobbed = [None for _ in range(len(nums)+1)]
        N = len(nums)

        maxRobbed[N], maxRobbed[N-1] = 0, nums[N-1]

        for i in range(N-2, -1,-1):
            maxRobbed[i] = max(maxRobbed[i+1], maxRobbed[i+2] + nums[i])
        
        return maxRobbed[0]
        