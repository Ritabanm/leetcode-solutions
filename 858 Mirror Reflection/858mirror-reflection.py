class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        from math import gcd
        lcm = p * q // gcd(p, q)
        m = lcm // q   # vertical steps (wall side)
        n = lcm // p   # horizontal steps (height)

        if m % 2 == 0:   # left wall
            return 2     # only receptor on left wall at top is 2
        if n % 2 == 0:   # right wall, bottom
            return 0
        return 1         # right wall, top
