class Solution:
    def minMoves(self, sx: int, sy: int, x: int, y: int) -> int:
        cnt = 0
        while x > sx or y > sy:
            cnt += 1

            if x < y or x == y and sx > sy:
                x, y, sx, sy = y, x, sy, sx

            if x >= 2 * y:
                if x % 2:
                    return -1
                x //= 2
            else:
                x -= y

        return cnt if x == sx and y == sy else -1