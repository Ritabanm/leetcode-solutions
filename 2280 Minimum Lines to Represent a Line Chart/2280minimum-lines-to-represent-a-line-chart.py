from fractions import Fraction

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        slp = "X"
        counter = 0
        stockPrices.sort()
        def slope(x0:int,y0:int, x1:int,y1:int):
            return Fraction(y1 - y0, x1 - x0)
        
        for i in range(1, len(stockPrices)):
            cur_slope = slope(stockPrices[i - 1][0], stockPrices[i - 1][1], stockPrices[i][0], stockPrices[i][1])

            if cur_slope != slp:
                counter += 1
                slp = cur_slope
        
        return counter