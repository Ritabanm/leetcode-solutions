class Solution:
    def countDistinct(self, n: int) -> int:
        l = len(str(n))
        ans = 0
        for i in range(1, l):
            ans += 9**i
        arr = list(str(n))
        for i, v in enumerate(arr):
            if v == "0":
                break
            ans += (int(v) - 1) * (9 ** (l - i - 1))
        if "0" not in arr:
            ans += 1
        return ans