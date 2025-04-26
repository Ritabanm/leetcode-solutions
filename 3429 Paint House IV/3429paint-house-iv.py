class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        prev = [[0] * 3 for _ in range(3)]
        curr = [[float("inf")] * 3 for _ in range(3)]

        for i in range(n // 2):
            for j in range(3):
                for k in range(3):
                    if j == k:
                        continue

                    curr[j][k] = (
                        cost[i][j]
                        + cost[n - 1 - i][k]
                        + min(
                            prev[l][m]
                            for l in range(3)
                            for m in range(3)
                            if l != m and l != j and m != k
                        )
                    )

            prev = curr
            curr = [[float("inf")] * 3 for _ in range(3)]

        return min(min(v) for v in prev)