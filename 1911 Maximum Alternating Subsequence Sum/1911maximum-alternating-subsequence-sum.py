class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        memory = dict()
        def dfs(i, even):

            if i == len(nums):
                return 0
            
            if (i,even) in memory:
                return memory[(i,even)]

            total = nums[i] if even else -1*nums[i]
            memory[(i,even)] = max(total + dfs(i+1, not even), dfs(i+1, even))

            return memory[(i,even)]

        return dfs(0, True)