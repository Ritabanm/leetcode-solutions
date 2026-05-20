class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        sum_digit = 0

        for i in str(n):
            sum_digit += math.pow(int(i), k)
        
        return sum_digit ==n