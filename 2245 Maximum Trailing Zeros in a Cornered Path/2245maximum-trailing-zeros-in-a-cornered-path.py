class Solution:
    def maxTrailingZeros(self, grid: List[List[int]]) -> int:
        def check(grid, row_order=1, col_order=1):
            above = [[0, 0] for i in range(len(grid[0]))]
            ans = 0
            for row in grid[::row_order]:
                this_row = [0, 0]
                for i, v in enumerate(row[::col_order]):
                    c2 = c5 = 0
                    while v % 2 == 0:
                        c2 += 1
                        v /= 2
                    while v % 5 == 0:
                        c5 += 1
                        v /= 5
                    this_row[0] += c2
                    this_row[1] += c5
                    ans = max(ans, min(this_row[0] + above[i][0], this_row[1] + above[i][1]))
                    above[i][0] += c2
                    above[i][1] += c5
            return ans
        return max(check(grid, ro, co) for ro in [-1, 1] for co in [-1, 1])
        
        
        
        
        