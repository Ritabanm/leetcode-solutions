from functools import lru_cache

class Solution:
    def countFancy(self, l: int, r: int) -> int:

        def is_good(x):
            s = str(x)
            if len(s) == 1:
                return True
            inc = all(s[i] > s[i-1] for i in range(1, len(s)))
            dec = all(s[i] < s[i-1] for i in range(1, len(s)))
            return inc or dec

        good_sums = {i for i in range(1, 145) if is_good(i)}

        def count(bound):
            digits = list(map(int, str(bound)))
            n = len(digits)

            @lru_cache(None)
            def dp(i, s, tight):
                if i == n:
                    return 1 if s in good_sums else 0

                limit = digits[i] if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ans += dp(i + 1, s + d, tight and d == limit)

                return ans

            return dp(0, 0, True)

        goods = set()
        for i in range(1, 10):
            goods.add(i)

        for mask in range(1 << 9):
            num = []
            for i in range(9):
                if mask & (1 << i):
                    num.append(str(i + 1))
            if num:
                goods.add(int("".join(num)))

        for mask in range(1 << 10):
            num = []
            for i in range(10):
                if mask & (1 << i):
                    num.append(str(9 - i))
            if num:
                goods.add(int("".join(num)))

        goods = sorted(goods)

        goods_in_range = [g for g in goods if l <= g <= r]

        overlap = sum(1 for g in goods_in_range if sum(map(int, str(g))) in good_sums)

        return count(r) - count(l - 1) + len(goods_in_range) - overlap