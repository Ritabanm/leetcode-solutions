class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        res = ''
        while h > 0 and v > 0:
            pre = comb(h + v - 1, v)
            
            if k <= pre:
                res += 'H'
                h -= 1
            else:
                res += 'V'
                v -= 1
                k -= pre

        if h == 0:
            res += 'V' * v
        if v == 0:
            res += 'H' * h
            
        return res