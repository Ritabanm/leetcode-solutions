class Solution:
    def powerUpdate(self, nums: list[int], p: int, queries: list[list[int]]) -> list[int]:
        sl = SortedList(nums)
        mod = (10 ** 9) + 7
        ans = []
        for val, k in queries:
            sl.add(val)
            diff = len(sl) - k
            x = sl[diff]
            p = pow(p, x, mod)
            ans.append(p)
        return ans