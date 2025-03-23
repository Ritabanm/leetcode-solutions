class Solution:
    def countAsterisks(self, s: str) -> int:
        openBar = False
        cnt = 0
        for char in s:
            if char == '|':
                openBar = not openBar
            elif char == "*" and not openBar:
                cnt +=1
        return cnt