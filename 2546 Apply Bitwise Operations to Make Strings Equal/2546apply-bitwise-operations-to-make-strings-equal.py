class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        return '1' in s and '1' in target or '1' not in target and '1' not in s