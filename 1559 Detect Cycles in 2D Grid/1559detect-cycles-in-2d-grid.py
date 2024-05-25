class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        numRows, numCols = len(grid), len(grid[0])

        visited = [[False for i in range(numCols)] for j in range(numRows)]

        dirs = [[-1,0], [1, 0], [0, -1], [0, 1]]
        flag = False

        def dfs(row, col, parent, symb):
            nonlocal flag
            visited[row][col] = True
            for d in dirs:
                newRow = row + d[0]
                newCol = col + d[1]

                if 0 <= newRow < numRows and 0 <= newCol < numCols:
                    if grid[newRow][newCol] == symb:
                        if (parent[0] != newRow or parent[1] != newCol) and visited[newRow][newCol] == True:
                            flag = True
                            return
                        if not visited[newRow][newCol]:
                            dfs(newRow, newCol,[row, col], symb)
        
        
        for i in range(numRows):
            for j in range(numCols):
                if not visited[i][j]:
                    dfs(i, j, [-1,-1], grid[i][j])

        return flag