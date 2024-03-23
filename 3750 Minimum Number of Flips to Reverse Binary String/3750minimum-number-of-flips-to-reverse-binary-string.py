class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        r = s[::-1]
        return sum(c1 != c2 for c1, c2 in zip(s,r))