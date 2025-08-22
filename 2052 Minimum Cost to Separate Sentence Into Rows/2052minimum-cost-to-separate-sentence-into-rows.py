class Solution:
    def minimumCost(self, sentence: str, k: int) -> int:

        if k >= len(sentence): return 0 

        words = list(map(lambda x : len(x)+1, 
                         sentence.split()))[::-1]
        
        n, kk, ans = len(words), k - words[0], inf
        k+= 1
        
        @lru_cache(None)
        def dfs(i,space = k):

            space-= words[i]
            if i == n-1: return space*space

            return min(space*space + dfs(i+1), 
                       dfs(i+1,space) if space >= words[i+1] else inf)

        for idx in range(1,n):
            ans = min(ans, dfs(idx))
            kk-= words[idx]
            if kk < 0: break
              
        return ans