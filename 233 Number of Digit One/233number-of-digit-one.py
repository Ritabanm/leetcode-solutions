class Solution:
    def countDigitOne(self, n: int) -> int:
        return self._count_of_i(n ,1)

    def _count_of_i(self, n: int, i: int) -> int:
        count, x = 0, 1
        while x <= n:
            a, b = divmod(n, x * 10)
            count += a * x  # (i)
            k = i * x
            if b < k:
                b = 0  # (ii)
            else:
                b = min((b - k) + 1, x)  # (iii)
            count += b
            x *= 10

        return count