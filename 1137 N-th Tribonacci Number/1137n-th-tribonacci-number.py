class Solution:
    def tribonacci(self,n):
        t0,t1,t2 = 0,1,1
        if n==0:
            return t0
        elif n==1:
            return t1
        elif n==2:
            return t2
        for _ in range(3, n+1):
            t3 = t0+t1+t2
            t0,t1,t2 = t1,t2,t3
        return t2

