class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:

        m, n,  seen, ans = len(grid), len(grid[0]), set(), inf
        
        def backtrack(cnt: int)-> None:
            nonlocal ans, seen

            ones = [(i,j) for i, j in product(range(m),range(n)
                    ) if grid[i][j] and not {i,j+15}&seen]
            
            if not ones:
                ans = min(ans, cnt)
                
            for i, j in ones:

                seen|={i,j+15}
                backtrack(cnt+1)
                seen-= {i,j+15}

            return    
                
        backtrack(0)
        
        return ans