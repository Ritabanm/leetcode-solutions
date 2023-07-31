class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        p = [i for i in range(n)]
        def find(x):
            if x!=p[x]:
                p[x] = find(p[x])
            return p[x]
        res = []
        for u,v in requests:
            pu,pv = sorted([find(u),find(v)])
            possible = True
            for a,b in restrictions:
                pa,pb = sorted([find(a),find(b)])
                if (pa,pb) in [(pu,pv),(pu,pu),(pv,pv)]:
                    possible = False
                    break
            res.append(possible)
            if possible: p[pv] = pu
        return res