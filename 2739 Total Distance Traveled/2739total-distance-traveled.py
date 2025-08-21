class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist, used = 0, 0
        while mainTank > 0:
            mainTank -= 1
            dist += 10
            used += 1
            if used % 5 == 0 and additionalTank > 0:
                additionalTank -= 1
                mainTank += 1
        return dist