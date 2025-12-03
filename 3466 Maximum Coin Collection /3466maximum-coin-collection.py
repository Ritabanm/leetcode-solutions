class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        lanes = [lane1, lane2]

        @cache
        def dfs(l, switch, mile):
            if mile == len(lane1):
                return 0
            
            m = lanes[l%2][mile]
            v = dfs(l, switch, mile + 1)
            v2 = 0
            if switch < 2:
                v2 = dfs(l + 1, switch + 1, mile + 1)
            return m + max(v, v2, 0)

        res = -inf
        for i in range(len(lane1)):
            v1 = dfs(0, 0, i)
            v2 = dfs(1, 1, i)

            res = max(v1, v2, res)
        return res