class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        def getMinSuffix(w1, w2):
            n = min(len(w1), len(w2))
            for i in range(n, 0, -1):
                if w1[-i:] == w2[:i]:
                    return w2[i:]
            return w2

        n = len(words)
        suffix = defaultdict(dict)
        for i in range(n):
            for j in range(n):
                suffix[i][j] = getMinSuffix(words[i], words[j])
        dp = [['']*n for _ in range(1<<n)]
        for i in range(1, 1<<n):
            indexes = [j for j in range(n) if i&(1<<j)]
            for j in indexes:
                i2 = i&~(1<<j)
                strs = [dp[i2][j2]+suffix[j2][j] for j2 in indexes if j2 != j]
                dp[i][j] = min(strs, key=len) if strs else words[j]
        return min(dp[-1], key=len)