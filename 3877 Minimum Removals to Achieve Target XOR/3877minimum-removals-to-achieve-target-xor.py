class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(ind, curXOR):
            if ind >= n:
                return 0 if curXOR == target else float('-inf')

            take = dfs(ind + 1, curXOR ^ nums[ind]) + 1
            skip = dfs(ind + 1, curXOR)

            return max(take, skip)

        maxi = dfs(0, 0)

        if maxi == float('-inf'):
            return -1

        return n - maxi