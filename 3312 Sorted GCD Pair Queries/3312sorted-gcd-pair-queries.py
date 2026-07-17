class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        M = max(nums)
        
        count = [0 for _ in range(M+20)]
        for n in nums:
            x = 1
            while x*x <= n:
                if n%x==0:
                    count[x]+=1
                    if x*x!=n:
                        count[n//x]+=1 
                x+= 1
        
        dp = [0 for _ in range(M+1)] 
        for i in range(M, 0, -1):
            dp[i] = count[i]*(count[i]-1)//2
            #now subtract
            j = 2
            while i*j <= M:
                dp[i] -= dp[i*j]
                j+=1 
        gcds = [i for i in range(M+1) if dp[i]>0]
        sm = [dp[i] for i in range(M+1) if dp[i]>0]
        for i in range(1, len(sm)):
            sm[i] += sm[i-1]
        
        out = []
        for q in queries:
            i = bisect.bisect_left(sm, q+1)
            out.append(gcds[i])
        return out