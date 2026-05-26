class Solution:
    def popcountDepth(self, n: int, k: int) -> int:

        def depth(num, n = 0):
            if num == 0: return -1
            while num > 1:
                n+= 1
                num = num.bit_count()
            return n

        def setBitCnt(cnt: int, res = 0)-> int:

            for leftBit in range(m-1, -1, -1):
                if not (n >> leftBit) & 1: continue
                res+= comb(leftBit, cnt)
                cnt-= 1
                if cnt < 0: return res

            return res + (cnt == 0)


        if k == 0: return int(n >= 1)

        ans, m = 0, n.bit_length()
        if k == 1: return m - 1

        for cnt in range(1, m + m): 
            if depth(cnt) == k - 1:
                ans+= setBitCnt(cnt)

        return ans