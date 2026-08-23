class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        maxi = max(lights)
        res = 0

        for t in arrivalTime:
            r = t % period

            if r >= maxi:
                res = max(res, period - r)

        return res