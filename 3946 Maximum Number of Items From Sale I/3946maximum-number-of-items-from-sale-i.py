class Solution:
    
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)


        bonus = [0] * n

        for i in range(n):
            fi = items[i][0]
            for j in range(n):
                if i != j and items[j][0] % fi == 0:
                    bonus[i] += 1

        dp = [0] * (budget + 1)

        for i in range(n):
            cost = items[i][1]
            first_gain = 1 + bonus[i]

            ndp = dp[:]

            for b in range(cost, budget + 1):
                ndp[b] = max(
                    ndp[b],
                    dp[b - cost] + first_gain
                )

            for b in range(cost, budget + 1):
                ndp[b] = max(
                    ndp[b],
                    ndp[b - cost] + 1
                )

            dp = ndp

        return max(dp)
            
        