class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = {}
        for x, y, z in allowed: mp.setdefault((x, y), set()).add(z)
            
        def fn(row): 
            """Return list of rows built from given row."""
            ans = [""]
            for x, y in zip(row, row[1:]):
                if (x, y) not in mp: return []
                ans = [xx + zz for xx in ans for zz in mp[x, y]]
            return ans 
        
        # dfs 
        stack = [bottom]
        while stack: 
            row = stack.pop()
            if len(row) == 1: return True 
            stack.extend(fn(row))
        return False 