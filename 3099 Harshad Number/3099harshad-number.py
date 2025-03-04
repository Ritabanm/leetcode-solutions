class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x:int)-> int:
        
        sum_num = 0
        temp = x
        while temp>0:
            sum_num += temp%10
            temp//=10
        if x% sum_num==0:
            return sum_num
        return -1