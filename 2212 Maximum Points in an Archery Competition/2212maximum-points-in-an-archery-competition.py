class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:

        def impl(i0, arrows):
            if i0 == -1:
                return 0, 0
            mask1 = 0
            shot = -1
            if arrows - aliceArrows[i0] - 1 >= 0:
                mask1, shot = impl(i0-1, arrows - aliceArrows[i0] - 1)
                shot += i0
                mask1 |= (1 << i0)
            mask0, no_shot = impl(i0-1, arrows)
            mask = mask1 if shot > no_shot else mask0

            return mask, max(shot, no_shot)

        mask, score = impl(11, numArrows)
        result = [0] * 12
        for i in range(12):
            if mask & (1 << i):
                result[i] = aliceArrows[i] + 1

        result[0] = numArrows - sum(result[1:])

        return result