class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        two_color, three_color = 6, 6
        for _ in range(n - 1):
            two_color, three_color = (two_color * 3 + three_color * 2) % mod, (two_color * 2 + three_color * 2) % mod
        return (two_color + three_color) % mod