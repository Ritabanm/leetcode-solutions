from functools import lru_cache
class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        @lru_cache(maxsize=None)
        def dp(o: int, e: int, p: int) -> int:
            if o == 0 and e == 0:
                return 1
            if p:
                if o == 0:
                    return 0
                return o * dp(o - 1, e, 0)
            if e == 0:
                return 0
            return e * dp(o, e - 1, 1)
        oddCount = (n + 1) // 2
        evenCount = n // 2
        tot = 0
        for x in range(1, n + 1):
            if x & 1:
                tot += dp(oddCount - 1, evenCount, 0)
            else:
                tot += dp(oddCount, evenCount - 1, 1)
        if k > tot:
            return []
        nums = list(range(1, n + 1))
        ans = []
        o = oddCount
        e = evenCount
        for i in range(n):
            for j in range(len(nums)):
                x = nums[j]
                if i and (x & 1) == (ans[-1] & 1):
                    continue
                ways = dp(o - 1, e, 0) if (x & 1) else dp(o, e - 1, 1)
                if k > ways:
                    k -= ways
                else:
                    ans.append(x)
                    nums.pop(j)
                    if x & 1:
                        o -= 1
                    else:
                        e -= 1
                    break
        return ans