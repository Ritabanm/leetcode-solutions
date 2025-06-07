class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        
        def dfs(root, grid, r, c,height):
            if root == None:
                return
            
            grid[r][c] = str(root.val)
            dfs(root.left, grid, r+1, c-2**(height-r-1), height)
            dfs(root.right, grid, r+1, c+2**(height-r-1), height)
        
        def maxheight(root, depth):
            if root == None:
                return depth
            
            return max(maxheight(root.left, depth+1),
            maxheight(root.right, depth+1))
        
        m = maxheight(root, 0)
        n = 2**m-1

        grid = [["" for _ in range(n)] for _ in range(m)]
        dfs(root, grid, 0, (n-1)//2, m-1)
        return grid
        