class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0
        for c in s:
            if c == '*':
                if n: n -= 1
            elif c == '#':
                n += n
            elif c == '%':
                continue
            else:
                n += 1
        
        if k >= n: return '.'
        
        for c in reversed(s):
            if c == '*':
                n += 1
            elif c == '#':
                n //= 2
                if k >= n: k -= n
            elif c == '%':
                k = n - 1 - k
            else:
                if k == n - 1: return c
                n -= 1
        
        return '.'