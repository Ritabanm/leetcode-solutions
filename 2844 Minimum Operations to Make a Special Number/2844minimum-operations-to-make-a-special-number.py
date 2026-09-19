class Solution:
    def minimumOperations(self, num: str) -> int:
        
        @cache
        def func(idx,val):
            
            if idx == len(num):
                if val != "" and int(val)%25 == 0:
                    
                    return 1
                return -10**20
            
            return max(1+func(idx+1,(val+num[idx])[-2:]),func(idx+1,val))
        
        
        m = func(0,"")
        if m < 0:
            return len(num)
        return len(num)-func(0,"")+1