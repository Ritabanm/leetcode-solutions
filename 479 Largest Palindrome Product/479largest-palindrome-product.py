class Solution:
    def largestPalindrome(self, n):
        if n == 1: return 9

        a = 1

        while a < 10**n:
            upper = 10**n-a
            lower = int(str(upper)[::-1])
            if a**2-lower*4 >= 0 and (a**2-lower*4)**0.5 == int((a**2-lower*4)**0.5):
                return (upper*10**n+lower)%1337
            a += 1

        





        

        