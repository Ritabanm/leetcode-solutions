class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = length >= 10000 or width >= 10000 or height >= 10000 or mass >= 10000 or ((length * width) * height) >= (10 ** 9)
        heavy = mass >= 100
        if bulky and not heavy:
            return "Bulky"
        elif heavy and not bulky:
            return "Heavy"
        elif bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"