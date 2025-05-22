class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        n, m = len(mat), len(mat[0])
        dfs = [0 for i in range(2)]
        dfs[0] |= 1 << 0
        for i in range(0, n):
            s = set(mat[i])
            dfs[(i + 1) % 2] = 0
            for x in s:
                    dfs[(i + 1)%2] |= dfs[i%2] << x

        ret = float('inf')
        for i in range(0, 4902):
            if dfs[n%2] & (1 << i):
                if(abs(i - target) > ret): break
                ret = min(ret, abs(i - target))
        return ret
        