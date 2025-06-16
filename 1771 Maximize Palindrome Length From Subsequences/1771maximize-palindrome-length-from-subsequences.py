class Solution:

    def __init__(self):
        self.mem = {}

    def findMax(self, s, i, j):
        if i == j:
            return 1, i, j
        if i > j:
            return 0, i, j
        if (i, j) in self.mem:
            return self.mem[(i, j)]
        if s[i] == s[j]:
            ans, l, r = self.findMax(s, i + 1, j - 1)
            ans += 2
            l, r = i, j
        else:
            q1, l1, r1 = self.findMax(s, i, j - 1)
            q2, l2, r2 = self.findMax(s, i + 1, j)
            if q1 > q2:
                ans, l, r = q1, l1, r1
            else:
                ans, l, r = q2, l2, r2
        self.mem[(i, j)] = ans, l, r
        return ans, l, r
    
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n, m = len(word1), len(word2)
        self.findMax(s, 0, n + m - 1)
        ans = 0
        for i in range(n):
            for j in range(m):
                ln, l, r = self.findMax(s, i, n + j)
                if l <= n - 1 and r >= n:
                    ans = max(ans, ln)
        return ans
        