class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        
        ans, power = 0,1
        for factor in range(9, 1, -1):
            while num % factor == 0:
                num /= factor
                ans = factor*power + ans
                power *= 10
        return int(ans) if num == 1 and -2**31<= ans<=2**31 - 1 else 0