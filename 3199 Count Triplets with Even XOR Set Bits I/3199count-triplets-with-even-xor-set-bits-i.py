class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        ab = []
        res = 0
        for i in a:
            for j in b:
                ab.append(i ^ j)
        for i in ab:
            for j in c:
                if bin(i ^ j)[2:].count("1") % 2 == 0:
                    res += 1
        return res