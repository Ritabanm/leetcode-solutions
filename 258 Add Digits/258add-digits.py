class Solution:
    def addDigits(self,num):
        while num>=10:
            num = sum(int(d) for d in str(num))
        return num
