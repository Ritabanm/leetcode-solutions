class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        seen = {}
        for x, y in points: seen.setdefault(y, set()).add(x)
        
        ans = set()
        for k in seen: 
            avg = sum(seen[k])/len(seen[k])
            for x in seen[k]:
                if 2*avg - x not in seen[k]: return False 
            ans.add(avg)
        return len(ans) == 1