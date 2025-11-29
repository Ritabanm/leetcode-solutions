class Solution:
    def minimumOR(self, grid: List[List[int]], maxBits = 17) -> int:

        def upDate(mask: int)-> int:            # <-- 3a)

            for row in grid:
                for num in row:
                    if mask|num == mask: break  # <-- 3b)
                else: return mask ^ (1 << k)    # <-- 3c)

            return mask


        mask = (1 << maxBits) - 1               # <-- 1)

        for k in range(maxBits - 1, -1, -1):    # <-- 2)
            mask = upDate(mask ^ (1 << k))

        return mask                             # <-- 4)