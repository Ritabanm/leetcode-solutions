class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sums = 0
        i = 0

        while n:
            last = n % 10
            sums += last

            if last != 0:
                x += last * 10**i
                i += 1

            n //= 10
        
        return x * sums