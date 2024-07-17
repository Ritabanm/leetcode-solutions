class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:

        a, b, c = sorted(sides)                                 # <-- 1)
        if a + b <= c: return []
        
        angleA = degrees(acos((b * b + c * c - a * a)/(2*b*c))) # <-- 2)
        angleB = degrees(acos((a * a + c * c - b * b)/(2*a*c)))   

        return [angleA, angleB, 180 - angleA - angleB]          # <-- 3)
        