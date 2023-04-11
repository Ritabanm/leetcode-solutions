"""class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            number = n
            product = 1
            while number:
                product *= number % 10
                number //= 10
            if product % t == 0:
                return n
            n += 1"""

class Solution:
    def smallestNumber(self, n, t):
        while True:
            number = n
            product = 1
            while number:
                product*=number%10
                number//=10
            if product%t==0:
                return n
            n+=1