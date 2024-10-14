class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        m,n = len(board), len(board[0])
        data = [[] for _ in range(n)]
        for i,r in enumerate(board):
            h=[]
            for j,v in enumerate(r):
                if len(h)==3: heappushpop(h, (v,i,j))
                else: heappush(h, (v,i,j))
            for it in h:
                j = it[2]
                if len(data[j])==3: heappushpop(data[j], it)
                else: heappush(data[j], it)
        h = []
        for r in data:
            for it in r:
                if len(h)==11: heappushpop(h, it)
                else: heappush(h, it)
        res = -math.inf
        for x,y,z in combinations(h, 3):
            if len({x[1], y[1], z[1]}) == 3 and len({x[2],y[2],z[2]}) == 3:
                res=max(res, x[0]+y[0]+z[0])
        return res
        

        