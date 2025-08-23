class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        res = 0
        for i in commands:
            if i == "RIGHT":
                res += 1
            elif i == "LEFT":
                res -= 1
            elif i == "DOWN":
                res += n
            else:
                res -= n
        return res