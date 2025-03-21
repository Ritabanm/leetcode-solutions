from collections import defaultdict
class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        d = defaultdict(int)
        d[(0,0)] = 1
        zeros, ones = 0, 0
        res = 0
        for num in s:
            if num == '1':
                ones += 1
            else:
                zeros += 1
            q = min(zeros//num1, ones//num2)
            res += d[(zeros -q*num1, ones -q*num2)]
            d[(zeros -q*num1, ones -q*num2)] += 1
        return res

