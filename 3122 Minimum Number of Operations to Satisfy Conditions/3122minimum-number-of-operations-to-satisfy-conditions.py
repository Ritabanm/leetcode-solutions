class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        @cache
        def calc(j, val):
            if j == len(grid[0]):
                return 0
            
            c = 0
            for i in range(len(grid)):
                if grid[i][j] != val:
                    c += 1
            
            ans = float('inf')
            
            for k in range(10):
                if k == val:
                    continue
                ans = min(ans, c + calc(j+1, k))
            
            return ans
        
        return min(calc(0, i) for i in range(10))