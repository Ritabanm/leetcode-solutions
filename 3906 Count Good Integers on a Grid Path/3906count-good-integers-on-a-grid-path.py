class Solution:
    def countGoodIntegersOnPath(self, l: int, r: int, directions: str) -> int:
        n = l-1
        k = len(str(n))
        strr = "0"*(16-k) + str(n)
        dp = [[[[-1 for _ in range(8)] for _ in range(11)] for _ in range(2)] for _ in range(17)]
        def dfs(pos,tight,last,pidx):
            if pos==16:
                return pidx==7 # 7 pidx are fully processed
            if dp[pos][tight][last][pidx]!=-1:
                return dp[pos][tight][last][pidx]
            if tight:
                limit = int(strr[pos])
            else:
                limit = 9
            res = 0
            for d in range(0,limit+1):
                ntight = (tight==1 and d==limit)
                npidx = pidx
                nlast = last
                if pidx<7 and pos==path[pidx]:
                    if d<last and last!=10:
                        continue
                    nlast = d
                    npidx +=1
                res+=dfs(pos+1,ntight,nlast,npidx)
            dp[pos][tight][last][pidx] = res
            return dp[pos][tight][last][pidx]
        path = [0]
        for i in directions:
            if i=='D':
                path.append(path[-1]+4)
            else:
                path.append(path[-1]+1)
        x1=  (dfs(0,1,10,0))
        n = r
        k = len(str(n))
        strr = "0"*(16-k) + str(n)
        path = [0]
        dp = [[[[-1 for _ in range(8)] for _ in range(11)] for _ in range(2)] for _ in range(17)]
        for i in directions:
            if i=='D':
                path.append(path[-1]+4)
            else:
                path.append(path[-1]+1)
        x2 = (dfs(0,1,10,0))
        return x2-x1