class Solution:
    def minSensors(self, n: int, m: int, k: int) -> int:
        x = n//(1+2*k)
        y = m//(1+2*k)
        
        if (1+2*k) * x < n:
            x += 1
        
        if (1+2*k) * y < m:
            y += 1
        return x*y