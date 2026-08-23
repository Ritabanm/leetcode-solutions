class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        m = len(station)
        
        if n == 1:
            return 0

        left = [-1] * n
        for i in range(n):
            left[i] = station.find(skill[i], left[i - 1] + 1)

        right = [m] * (n + 1)
        for i in range(n - 1, -1, -1):
            right[i] = station.rfind(skill[i], 0, right[i + 1])

        ans = 1
        for i in range(n - 1):
            ans = max(ans, right[i + 1] - left[i])

        return ans