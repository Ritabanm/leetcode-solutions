class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        dp = ([math.inf] * n) + [0]
        for _ in range(k):
            for i in range(n):
                median = i
                change = False
                less = more = 0
                for j in range(i, n):
                    more += houses[j]
                    if change:
                        less += houses[median]
                        more -= houses[median]
                        median += 1
                        change = False
                    else:
                        change = True
                    m = median - i - (j - median + 1)
                    dist = m*houses[median] - less + more
                    dp[i] = min(dp[i], dp[j + 1] + dist)
        return dp[0]
                