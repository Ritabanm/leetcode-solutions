class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(1, len(s)):
            diff = abs(int(s[i]) - int(s[i - 1]))
            if diff > 2:
                return False
        return True