class Solution:
    def shortestDistance(self, grid:List[List[int]])-> int:
        rows = len(grid)
        cols = len(grid[0])
        dist_matrix = [[0]*cols for row in range(rows)]
        directions = [(1,0), (-1,0),(0,1), ((0,-1))]
        building = 1
        obstacle = 2
        empty_land = 0
        min_dis = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==building:
                    local_dist = float('inf')
                    queue = collections.deque([(row, col, 0)])
                    while queue:
                        cur_row, cur_col, distance = queue.popleft()
                        for row_inc, col_inc in directions:
                            new_row = cur_row+row_inc
                            new_col = cur_col + col_inc
                            if (0<=new_row<rows) and (0 <= new_col < cols) and grid[new_row][new_col]==empty_land:
                                grid[new_row][new_col]-=1
                                dist_matrix[new_row][new_col]+=distance+1
                                queue.append((new_row, new_col, distance+1))
                                local_dist = min(local_dist, dist_matrix[new_row][new_col])
                    empty_land-=1
                    min_dist = local_dist
        return min_dist if min_dist!=float('inf') else -1
        


