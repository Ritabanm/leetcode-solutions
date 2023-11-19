class Solution:
    def maxProduct(self, n: int) -> int:
        a = []
        while n>0:
            a.append(n%10)
            n = n//10
        a.sort(reverse = True)
        return a[0]*a[1]