class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1, s2 = sorted(s1), sorted(s2)
        if all(x>=y for x,y in zip(s1, s2)):
            return True
        if all(y>=x for x,y in zip(s1, s2)):
            return True
        return False