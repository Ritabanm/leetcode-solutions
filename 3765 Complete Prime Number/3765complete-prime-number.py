class Solution:
    def completePrime(self, num):
        cur = str(num)
        size = len(cur)

        def isPrime(val):
            if val<2:
                return False
            for j in range(2, int(val**0.5)+1):
                if val%j==0:
                    return False
            return True
        if size==1 and isPrime(num):
            return True
        
        now=""
        for i in range(size):
            now+=cur[i]
            if not isPrime(int(now)):
                return False
        now =""
        for i in range(size-1, -1, -1):
            now = str(cur[i]) + now
            if not (isPrime(int(now))):
                return False
        return True