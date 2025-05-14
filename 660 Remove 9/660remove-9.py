class Solution:
    def newInteger(self, n: int) -> int:
        ans = ''
        while n:
            ans = str(n%9) + ans
            n //= 9
        return int(ans)