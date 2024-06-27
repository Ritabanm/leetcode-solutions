class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def gcd(x, y):
            while x % y != 0: x, y = y, x % y
            return y
        gcds, cnt, ans = [gcd(num, k) for num in nums], defaultdict(int), 0
        for g in gcds: cnt[k // g] += 1
        for g in gcds:
            for f in cnt: ans += cnt[f] if not g % f else 0
            ans -= not g % (k // g) 
        return ans // 2