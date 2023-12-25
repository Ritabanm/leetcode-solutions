class Solution:
    def makeStringGood(self, s: str) -> int:
        
        count=[0]*26
        for i in s:
            count[ord(i)-ord('a')]+=1
        @cache
        def f(i,target,deleted):
            if(i==26):
                return 0
            x=count[i]
            
            if(x==target or x==0):
                return f(i+1,target,0)
            if(x>target):
                #Adjusting to Target if has greater frequency
                delete=x-target+f(i+1,target,x-target)
                return delete
            else:
                need = target-x
                #Increasing frequency towards target
                insert = f(i+1,target,0)+need
                #Drop to zero
                delete = f(i+1,target,x)+x
                
                #Changing ch-1 character to ch  like deleting ch-1 character and incrementing ch character is far more better than converting ch-1 to ch
                change = f(i+1,target,0)+ (need-min(need,deleted))
           
                return min(insert,delete,change)

        mini=float('inf')
        for i in range(0,max(count)+1):
            mini=min(mini,f(0,i,0))

        return mini
        