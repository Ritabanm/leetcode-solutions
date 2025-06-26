class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits, num = [], n
        while num:
            num, digit = divmod(num, 10)
            digits.append(digit)
        return (n%((sum(digits) + prod(digits))) == 0)