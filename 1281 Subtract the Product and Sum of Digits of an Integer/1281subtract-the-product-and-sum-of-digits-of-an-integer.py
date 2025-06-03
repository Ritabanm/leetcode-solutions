class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        l1 = [int(i) for i in str(n)]
        product = 1
        sum1 = 0
        for i in l1:
            product *= i
            sum1 += i
        return product-sum1