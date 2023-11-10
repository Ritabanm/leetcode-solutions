class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        min_val = float("inf")
        for x in range(1,101):
            for y in range(1, 101):
                ans = sorted(abs(x-i) + abs(y-j) for i,j in points)
                min_val = min(min_val, ans[k-1])
        return min_val