class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n==1:
            return []
        
        res = []
        def dfs(path = [], rest = 2, target = n):
            if len(path)>0:
                res.append(path + [target])
            
            for i in range(rest, int(math.sqrt(target))+1):
                if target%i==0:
                    dfs(path + [i], i, target//i)
        dfs()

        return res