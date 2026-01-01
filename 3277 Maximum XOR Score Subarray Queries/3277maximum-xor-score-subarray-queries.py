class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        mx = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            mx[i][i] = f[i][i] = nums[i]
            for j in range(i + 1, n):
                f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                mx[i][j] = max(f[i][j], mx[i + 1][j], mx[i][j - 1])
        return [mx[l][r] for l, r in queries]