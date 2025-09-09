class Solution:
    def minTotalDistance(self, grid:List[List[int]])->int:
        m, n = len(grid), len(grid[0])
        homes_x = [0 for i in range(m)]
        homes_y = [0 for i in range(n)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    homes_x[i]+=1
                    homes_y[j]+=1
        def findMinDistance(leng, homes):
            res = float('inf')
            for x in range(leng):
                distance = 0
                for i in range(len(homes)):
                    distance+=abs(x-i)*homes[i]
                res = min(res, distance)
            return res
        res_x = findMinDistance(m, homes_x)
        res_y = findMinDistance(n, homes_y)
        return int(res_x+res_y)