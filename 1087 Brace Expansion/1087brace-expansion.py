class Solution:
    def expand(self, s: str) -> List[str]:
        s = s.replace('{', ' ').replace('}', ' ').split()
        res = []
        def dfs(idx, w):
            if idx == len(s):
                res.append(w)
                return
            for a in s[idx].split(','):
                dfs(idx + 1, w + a)
        dfs(0, '')
        res.sort()
        return res


       

   
       

        
        
                
                

        