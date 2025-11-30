class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        
        if k % 2 == 1:
            additional = k // 2
        else:
            additional = k // 2 - 1
            
        if additional >= n:
            additional = 0
            
        delta = n - (k - additional) + 1
        
        return n * (n + 1) // 2 + additional * delta