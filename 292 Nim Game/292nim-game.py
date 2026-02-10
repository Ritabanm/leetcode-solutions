class Solution:
    def canWinNim(self, n: int) -> bool:
        count = 0
        while n>0:
            if n%4==0:
                return False
            elif n<=7:
                return True
            elif n>7:
                if n%4==1:
                    return True
                n-=1
                count+=1
                count+=1
                