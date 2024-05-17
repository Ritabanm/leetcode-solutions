class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        histo = [[0] * n for _ in range(m)] #keeping track of counts

        #process the grid
        for i, row in enumerate(grid):
            prior = k
            for j, cell in enumerate(row) :
                if cell > k:
                    histo[i][j] = 0
                    prior = k
                elif cell > prior:
                    histo[i][j] = 1
                    prior = cell
                else: #cell <= prior:
                    histo[i][j] = histo[i][j-1] + 1 if j else 1
                    prior = cell
        
        #process each column
        total = 0
        for j in range(n):
            stack = []
            mytotal = 0
            for i in range(m):
                curr_val = histo[i][j]
                if curr_val == 0:
                    stack = []
                    mytotal = 0
                else:
                    height = 1
                    while stack and stack[-1][0] > curr_val:
                        w, h = stack[-1]
                        mytotal -= w*h
                        height += h
                        stack.pop()

                    stack.append((curr_val, height))
                    mytotal += (curr_val*height)

                #add up all the eligbile matrices
                total += mytotal

        return total


                

            