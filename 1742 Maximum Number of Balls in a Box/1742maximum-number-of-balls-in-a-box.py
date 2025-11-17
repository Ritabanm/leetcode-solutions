class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mapp = {}
        num = 0
        tmp = 0
        maxx = float('-inf')

        for i in range(lowLimit, highLimit + 1):
            num = i
            tmp = 0
            while num > 0:
                tmp += num % 10
                num //= 10
            mapp[tmp] = mapp.get(tmp, 0) + 1
            maxx = max(maxx, mapp[tmp])

        return maxx