class Solution:
    def mirrorDistance(self, n: int) -> int:
        rev=0
        num = n
        while (num!=0):
            rev = rev*10 + (num%10)
            num = num//10
        return abs(n-rev)