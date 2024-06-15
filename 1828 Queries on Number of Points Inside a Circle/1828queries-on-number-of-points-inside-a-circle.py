from typing import List

class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in queries:
            r2 = r * r
            cnt = 0
            for px, py in points:
                dx = px - x
                dy = py - y
                if dx*dx + dy*dy <= r2:
                    cnt += 1
            ans.append(cnt)
        return ans
