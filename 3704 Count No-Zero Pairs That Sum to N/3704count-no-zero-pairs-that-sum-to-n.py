class Solution:
    def countNoZeroPairs(self, n: int) -> int:
        s = str(n)
        length = len(s)
        digits = [int(c) for c in s]

        cache = {}
        def dfs(pos, sa, sb):
            if pos == length:
                return [1 if sa == 1 and sb == 1 else 0, 0]
            key = (pos, sa, sb)
            if key in cache:
                return cache[key]

            res = [0, 0]
            a_min = 1 if sa == 1 else 0
            b_min = 1 if sb == 1 else 0

            for da in range(a_min, 10):
                nsa = 1 if sa == 1 or da > 0 else 0
                for db in range(b_min, 10):
                    nsb = 1 if sb == 1 or db > 0 else 0
                    lower = dfs(pos + 1, nsa, nsb)
                    for cin in range(2):
                        if lower[cin] == 0:
                            continue
                        total = da + db + cin
                        if total % 10 == digits[pos]:
                            cout = total // 10
                            res[cout] += lower[cin]
            cache[key] = res
            return res

        return dfs(0, 0, 0)[0]
                