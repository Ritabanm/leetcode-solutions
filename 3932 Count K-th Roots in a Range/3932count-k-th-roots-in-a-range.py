import math

class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        st = math.ceil(l ** (1.0 / k) - 1e-9)
        end = math.floor(r ** (1.0 / k) + 1e-9)
        return max(0, end - st + 1)