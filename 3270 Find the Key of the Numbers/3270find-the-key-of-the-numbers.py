class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        vals = [str(x).zfill(4) for x in (num1, num2, num3)]
        return int("".join(map(min, zip(*vals))))