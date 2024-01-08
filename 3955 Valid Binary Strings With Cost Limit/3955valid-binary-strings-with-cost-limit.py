class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans=[]

        def baktrack(i,n,k,sum,st,lst):
            if sum>k:
                return
            if i==n:
                ans.append(st)
                return
            
            if lst:
                baktrack(i+1,n,k,sum,st+'0',0)
            else:
                baktrack(i+1,n,k,sum,st+'0',0)
                baktrack(i+1,n,k,sum+i,st+'1',1)
            return 

        baktrack(0,n,k,0,'',0)
        return ans