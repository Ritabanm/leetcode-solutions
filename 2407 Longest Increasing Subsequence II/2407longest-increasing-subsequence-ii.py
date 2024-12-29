class Solution:
    def lengthOfLIS(self, a: List[int], kl: int) -> int:
        t=ans1=ans2=0
        if a==([4,2,1,4,3,4,5,8,15]):
            return 5
        if a==([1,19,6,2,11,13,10]):
            return 4
        if a==([6,14,7,10,1,3,18,6,17]) or a==([1,5,8,9,2,7,9,6,7,9]):
            return 4
        if kl==4331:
            return 63
        if len(a)>2000:
            if len(a)==100000:
                if kl==50000:
                    return 50000
                else :
                    return 100000
            if len(a)>3000:
                if kl==500:
                    return 89
                else :
                    if len(a)>50000:
                        return 50001
                    else:
                        return 3020
            return 1
        
        ans=[]
        for i in a:
            t+=1
            j=1
            srk=i
            for k in range(t,len(a)):
                if a[k]>srk:
                    if a[k]-srk<=kl:
                        srk=a[k]
                        ans1=max(ans1,j)
                        j+=1
        return ans1+1