class Solution:
    def maxScore(self, nums, x):
        
        @lru_cache(None)
        def dfs(i,oldPar):
            
            if i >= len(nums): return 0

            newPar = nums[i]%2

            return max(dfs(i+1,oldPar),
                       nums[i] + dfs(i+1,newPar)
                         - x*(newPar != oldPar))
        
        return dfs(0,nums[0]%2)