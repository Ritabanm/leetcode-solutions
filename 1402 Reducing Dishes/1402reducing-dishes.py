class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        cur, coefficient, res = 0, 0, 0
        for i in range(len(satisfaction)):
            cur += satisfaction[i]
            coefficient += cur
            res = max(res, coefficient)
        return res