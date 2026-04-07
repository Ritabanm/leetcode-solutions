class Solution(object):
    def uniqueLetterString(self, S):
        N = len(S)
        index = collections.defaultdict(list)
        peek = collections.defaultdict(int)
        for i, c in enumerate(S):
            index[c].append(i)
        for c in index:
            index[c].extend([N, N])

        def get(c):
            return index[c][peek[c] + 1] - index[c][peek[c]]

        ans = 0
        cur = sum(get(c) for c in index)
        for i, c in enumerate(S):
            ans += cur
            oldv = get(c)
            peek[c] += 1
            cur += get(c) - oldv
        return ans % (10**9 + 7)