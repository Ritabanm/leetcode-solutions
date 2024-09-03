class Solution:
    def canEat(self, candiesCount: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(candiesCount)
        prefix = [0] * (n + 1)
        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + candiesCount[i-1]
        ans = []
        for fav, day, cap in queries:
            countLessFav = prefix[fav]
            countFav = candiesCount[fav]
            earliestDay = countLessFav // cap
            latestDay = countLessFav + countFav - 1
            ans.append(earliestDay <= day <= latestDay)

        return ans