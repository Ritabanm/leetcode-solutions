class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        ans = -inf
        hp = [] 
        for xj, yj in points:
            while hp and xj - hp[0][1] > k: heappop(hp)
            if hp: 
                ans = max(ans, xj + yj - hp[0][0])
            heappush(hp, (xj-yj, xj))
        return ans 