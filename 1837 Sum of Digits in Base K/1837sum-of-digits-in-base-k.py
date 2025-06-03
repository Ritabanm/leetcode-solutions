class Solution:
    def sumBase(self, n: int, k: int) -> int:
        output_sum =0
        while (n>0):
            rem = n%k
            output_sum = output_sum+rem
            n = int(n/k)
        return output_sum