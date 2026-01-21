class Solution:
    def countNumbers(self, l: str, r: str, b: int) -> int:
        
        def convert(num, base):
            num = int(num)
            if num == 0:
                return '0'

            result = ""
            while num > 0:
                result = str(num % base) + result
                num //= base

            return result
        l =str(int(l)-1)
        l = convert(l,b)
        r = convert(r,b)
        @cache
        def dp(index,num,tight,limit,lowest):
            
            if index==len(num):
                
                return 1
            
            else:
                
                l = (int(num[index])+1) if tight else limit
                
                ans = 0 
                for x in range(lowest,l):
                    
                    ans+=dp(index+1,num,tight and int(num[index])==x,limit,x)
                return ans 
        return (dp(0,r,True,b,0)-dp(0,l,True,b,0))%(10**9+7)
                
                

                