class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        def get_sum(t: set[int], idx: set[int]) -> int:
            res = inf
            for i in range(1, len(t) + 1):
                for cmb in combinations(t, i):
                    lcm_cmb, id, res1 = lcm(*cmb), 0, inf
                    for i, n in enumerate(nums):
                        if i not in idx:
                            multiple = lcm_cmb * ((n - 1) // lcm_cmb + 1)
                            if res1 > multiple - n:
                                res1 = multiple - n
                                id = i
                    res = min(res, res1 + get_sum(t - set(cmb), idx.union((id,))))
            return 0 if res == inf else res
        return get_sum(set(target), set())