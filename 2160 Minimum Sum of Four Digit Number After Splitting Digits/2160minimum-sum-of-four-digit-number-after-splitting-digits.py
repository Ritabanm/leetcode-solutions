class Solution:
    def minimumSum(self, num: int) -> int:
        digits= []
        for i in str(num):
            digits.append(i)
        digits.sort()

        return int(digits[0]+digits[2])+ int(digits[1]+digits[3])