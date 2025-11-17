class Solution:
    def largestMerge(self, w1: str, w2: str) -> str:
        ans=[]
        m,n=len(w1),len(w2)
        i=j=0
        while i<m or j<n:
            if w1[i:]>w2[j:]:
                ans.append(w1[i])
                i+=1
            else:
                ans.append(w2[j])
                j+=1
        return ''.join(ans)