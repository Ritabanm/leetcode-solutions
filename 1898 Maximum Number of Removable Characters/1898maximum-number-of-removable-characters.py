class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        
        
        lst=list(s)
        
        def isSubsequence(x,y):
            it=iter(y)
            return all(ch in it for ch in x)
        
        
        def isValid(m):
            new=lst[:]
            for i in range(m):
                new[removable[i]]=""
                
            return isSubsequence(p,"".join(new))
        
        low=0
        high=len(removable)
        ans=-1
        
        while low<=high:
            
            mid=(low+high)//2
            
            if isValid(mid):
                low=mid+1
                ans=mid
            else:
                high=mid-1
        
        return ans
                    