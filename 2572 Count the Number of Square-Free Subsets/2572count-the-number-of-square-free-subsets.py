class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        squares = {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}
        nums = [x for x in nums if x not in squares]
        c, nums = collections.Counter(nums), sorted(set(nums))
        
        @cache
        def getBit(x):
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
            return sum([1 << i for i, p in enumerate(primes) if x % p == 0])
        
        def dfs(u, cnt, mask):
            subRes = cnt
            for v in range(u + 1, len(nums)):
                if mask & getBit(nums[v]) == 0:
                    choice = (2 ** c[nums[v]] - 1) if nums[v] == 1 else c[nums[v]]
                    subRes += dfs(v, cnt * choice, mask | getBit(nums[v]))
            return subRes    
        return (dfs(-1, 1, 0) - 1) % (10 ** 9 + 7)