class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        def fun(idx_parity):
            ct = Counter([v for i, v in enumerate(nums) if i & 1 == idx_parity])
            freq = [ct[i] for i in range(k)]
            # cost to get r == 0
            cost = 0
            for v in ct:
                cost += ct[v] * min(v, k - v)
            # prefix sum of frequency
            pf = list(accumulate(freq + freq))
            half = k // 2
            res = [[cost, 0], [inf, -1]]
            for i in range(1, k):
                # k = 5, [0 1 2 3 4]: [0 1 2 2 1] -> [1 0 1 2 2] (+1 -1 -1 == +1)
                # k = 6, [0 1 2 3 4 5]: [0 1 2 3 2 1] -> [1 0 1 2 3 2] (+1 -1 -1 -1 +1 +1)
                cost = cost \
                    - (pf[i + half - 1] - pf[i - 1]) \
                    + (pf[i + k - 1] - pf[i + half - (not k & 1)])
                if cost < res[0][0]:
                    res[1] = res[0][:]
                    res[0] = (cost, i)
                elif cost < res[1][0]:
                    res[1] = (cost, i)
            return res

        n = len(nums)
        nums = [v % k for v in nums]
        if n == 1: return 0
        cost_even = fun(0)
        cost_odd = fun(1)
        if cost_even[0][1] != cost_odd[0][1]:
            return cost_even[0][0] + cost_odd[0][0]
        else:
            return min(cost_even[0][0] + cost_odd[1][0], cost_even[1][0] + cost_odd[0][0])