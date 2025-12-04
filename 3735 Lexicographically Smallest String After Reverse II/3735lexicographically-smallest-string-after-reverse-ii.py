class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        smallest = min(s)
        res = s

        for i, ch in enumerate(s):
            if ch == smallest:
                candidate = s[:i+1][::-1] + s[i+1:]
                res = min(res, candidate)

        for k in range(1, n + 1):
            candidate = s[:n-k] + s[n-k:][::-1]
            res = min(res, candidate)

        return res