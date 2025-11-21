class Solution:
    def canWin(self, currentState):
        @lru_cache(None)
        def dfs(s):
            if "++" not in s: return False
            for i in range(len(s)-1):
                if s[i:i+2] == "++" and not dfs(s[:i] + "--" + s[i+2:]):
                    return True

            return False

        return dfs(currentState)

        
        

        

            

        

        

        

        

        