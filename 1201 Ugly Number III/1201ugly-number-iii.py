class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def valid(bar):
            count = bar // a
            count += bar // b
            count += bar // c
            count -= bar // lcm(a,b)
            count -= bar // lcm(a,c)
            count -= bar // lcm(c,b)
            count += bar // lcm(a,b,c)
            return count >= n
        l = min(a,b,c)
        r = l * n
        res = l
        while l <= r:
            m =  l + (r - l) // 2
            if valid(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
            