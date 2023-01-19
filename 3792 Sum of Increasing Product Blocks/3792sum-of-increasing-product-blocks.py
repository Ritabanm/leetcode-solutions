class Solution:
    MOD = 10**9 + 7

    def sumOfBlocks(self, n: int) -> int:
        MOD = self.MOD
        result = 0
        num = 1
        
        for i in range(1, n + 1):
            product = 1
            for _ in range(i):
                product = product * num % MOD
                num += 1
            result = (result + product) % MOD
        
        return result