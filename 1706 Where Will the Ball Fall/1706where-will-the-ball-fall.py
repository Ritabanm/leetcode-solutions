class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:

        m,n = len(grid), len(grid[0])       # comments added nov 1 22 for @flufe (see below)
        N, ans = range(n), []
                              
        for pos in N:                       # for each ball in the top row...                         
            for row in grid:                #     for each row....

                direction = row[pos]        # +1 to the right, -1 to the left
                pos += row[pos]             # move the ball left or right
                                    
                if (pos not in N or         # if the ball runs into wall or...
                    row[pos] != direction): # ... if the ball runs into \/, then...
                    ans.append(-1)          # ...start the next ball. Otherwise, ball moves down a row
                    break                
            else:
                ans.append(pos)             # if tha ball does not fail, record its exit position
                       
        return ans                          # return the list of results