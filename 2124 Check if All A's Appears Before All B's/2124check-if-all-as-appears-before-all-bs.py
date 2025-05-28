class Solution:
    def checkString(self, s: str) -> bool:
        found = False
        for c in s:
            if c=='b':
                found = True
            elif found:
                return False
        return True