from collections import defaultdict
class Solution:
    def countPalindromes(self, s: str) -> int:
        if len(s) < 5:
            return 0
        
        n = len(s)
        # initialize dp arrrays
        pre, counts = [defaultdict(int) for _ in range(n)], defaultdict(int)

        counts[s[0]] += 1
    
        # count ab patterns
        for i in range(2, n):
            pre[i] = pre[i-1].copy()
            for key in counts.keys():
                pattern = (key, s[i-1])
                pre[i][pattern] += counts[key]
            counts[s[i-1]] += 1

        # dp arrays for ba appearances
        suf, counts = [defaultdict(int) for _ in range(n)], defaultdict(int)
        counts[s[-1]] += 1
        # count ba pattern
        for i in range(n-3, 0, -1):
            suf[i] = suf[i+1].copy()
            for key in counts.keys():
                pattern = (key, s[i+1])
                suf[i][pattern] += counts[key]
            counts[s[i+1]] += 1

        count = 0
        # multiply ab with ba to get counts at each iter
        for i in range(n):
            for key in pre[i]:
                count += pre[i][key] * suf[i][key]
        # mod
        return count % (10**9 + 7)
