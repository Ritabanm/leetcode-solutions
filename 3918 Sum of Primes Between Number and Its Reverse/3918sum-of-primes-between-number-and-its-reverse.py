class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r_n=int(str(n)[::-1])
        s=0
        min_n=min(n,r_n)
        max_n=max(n,r_n)
        def isprime(i):
            if i==1:
                return False
            if i==2 or i==3:
                return True
            for j in range(2,i):
                if i%j==0:
                    return False  
            return True

        for i in range(min_n, max_n+1):
            if isprime(i):
                s+=i
        return s       

            
               
                           
       



