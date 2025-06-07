class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def clearBit(x, k):
            return x ^ (1<<k)
        def checkBit(x, k):
            return x & (1<<k)
        @lru_cache(None)
        def dp(space_left, mask):
            if mask == 0: return 1
            if space_left == 0: return 1 + dp(sessionTime, mask)
            ans = math.inf
            for i in range(len(tasks)):
                if checkBit(mask, i):
                    flipped = clearBit(mask, i)
                    if space_left < tasks[i]: 
                        ans = min(ans, 1+dp(sessionTime - tasks[i], flipped))
                    else:
                        ans = min(ans, dp(space_left - tasks[i], flipped))
            return ans
        
        return dp(sessionTime, (1<<len(tasks)) - 1)