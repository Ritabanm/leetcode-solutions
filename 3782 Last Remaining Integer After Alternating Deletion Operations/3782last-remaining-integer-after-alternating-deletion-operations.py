class Solution:
    def lastInteger(self, n: int) -> int:
 
        left, rght, step, leftToRght = 1, n, 1, True  # <-- 1)

        while n > 1:                                  # <-- 2)
            if n%2 == 0:
                if leftToRght: 
                    rght-= step
                else: 
                    left+= step
            step*= 2
            n = (n+1)//2
            leftToRght^= True

        return left                                  # <-- 3)