"""class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = prev = 0
        for hi, pct in brackets:
            hi = min(hi,income)
            ans+= (hi-prev)*pct/100
            prev = hi
        return ans"""

class Solution:
    def calculateTax(self, brackets, income):
        ans = 0
        prev = 0
        for hi, pct in brackets:
            hi= min(hi, income)
            ans+=(hi-prev)*pct/100
            prev = hi
        return ans