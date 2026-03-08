class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:

        def geneNext(p):                # generate next array for pattern p
            m = len(p)
            next = [0] * m
            l = 0
            for r in range(1, m):
                while l > 0 and p[l] != p[r]:
                    l = next[l-1]
                if p[l] == p[r]:
                    l += 1
                next[r] = l
            return next

        def kmp(T, p, next):            # KMP find all occurances of pattern p in text T
            n, m = len(T), len(p)
            res = []
            i, j = 0, 0
            while i < n:
                if T[i] == p[j]:
                    i += 1
                    j += 1
                    if j == m:
                        res.append(i - j)
                        j = next[j - 1]
                else:
                    if j != 0:
                        j = next[j - 1]
                    else:
                        i += 1
            return res

        next = geneNext(pattern)

        m, n = len(grid), len(grid[0])
        hor = ''                            # horizontal string
        for row in grid:
            hor += ''.join(row)
        hindex = kmp(hor, pattern, next)    # all occurances of pattern in horizontal string
       
        ver = ''                            # vertical string
        for j in range(n):
            for i in range(m):
                ver += grid[i][j]
        vindex = kmp(ver, pattern, next)    # all occurances of pattern in horizontal string

        if not hindex or not vindex:        # edge case
            return 0

        lenp = len(pattern)
        ans = 0

        hset, vset = set(), set()           # cells covered by hindex and vindex
        for k in range(len(hindex)):
            if k > 0 and hindex[k] < hindex[k-1] + lenp:                # avoid duplicates
                for h in range(hindex[k-1] + lenp, hindex[k] + lenp):
                    i = h // n              # coordinate conversion for horizontal index h
                    j = h % n
                    hset.add((i, j))
            else:
                for h in range(hindex[k], hindex[k] + lenp):
                    i = h // n
                    j = h % n
                    hset.add((i, j))
        
        for k in range(len(vindex)):
            if k > 0 and vindex[k] < vindex[k-1] + lenp:
                for v in range(vindex[k-1] + lenp, vindex[k] + lenp):
                    j = v // m              # coordinate conversion for vertical index v
                    i = v % m
                    vset.add((i, j))
            else:
                for v in range(vindex[k], vindex[k] + lenp):
                    j = v // m
                    i = v % m
                    vset.add((i, j))
        return len(hset & vset)                     # common cells