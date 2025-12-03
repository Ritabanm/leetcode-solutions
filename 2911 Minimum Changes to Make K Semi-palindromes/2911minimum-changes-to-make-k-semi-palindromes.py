class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        factors = [[] for _ in range(n + 1)]  # ignore self
        for i in range(1, n + 1):
            for j in range(2 * i, n + 1, i):
                factors[j].append(i)

        def hamming(s1, s2) -> int:
            return sum(1 for c1, c2 in zip(s1, s2) if c1 != c2)

        def minimumChangesSubstring(l: int, r: int) -> int:
            if r < l:
                return n

            return min((
                sum(
                    hamming(s[l + remainder:r + 1:d], ''.join(reversed(s[l + remainder:r + 1:d]))) // 2
                    for remainder in range(d)
                )
                for d in factors[r - l + 1]
            ), default=n)

        minimumChangesCache = [[minimumChangesSubstring(i, j) for j in range(n)] for i in range(n)]

        # dp
        cache = [[n] * (k + 1) for _ in range(n + 1)]
        cache[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                si = i - 1
                cache[i][j] = min((cache[b][j - 1] + minimumChangesCache[b][si] for b in range(si)), default=n)
        
        return cache[n][k]