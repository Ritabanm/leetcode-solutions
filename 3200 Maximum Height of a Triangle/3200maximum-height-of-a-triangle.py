class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:

        if red < blue: red, blue = blue, red    # <-- 1)

        n = isqrt(blue)                         #
        rows = 2*n - 1                          # <-- 2)
        blue-= n*n                              # 

        red-= n*n - n                           # <-- 3)
       
        if red >= 2*n:                          #
            rows+= 1                            # <-- 4)
            red-= 2*n                           # 

        if red > n and blue >= n:               # <-- 5)
            rows+= 1                            #
            
        return rows
        