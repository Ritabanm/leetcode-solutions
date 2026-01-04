class Solution:
    def numberOfChild(self, n: int, k: int) -> int:

        k%=  2*n -2

        return n-1 - abs(n-1 - k)