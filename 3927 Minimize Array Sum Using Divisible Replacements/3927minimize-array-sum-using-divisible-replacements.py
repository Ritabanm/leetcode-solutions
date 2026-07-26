class Solution:
    def minArraySum(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        m=nums[-1]
        d={}
        for i in nums:
            d[i]=True
        vis=[-1 for i in range(m+1)]
        for i in nums:
            if vis[i]!=-1:
                continue
            vis[i]=i
            j=2*i
            while j<=m:
                if vis[j]==-1:
                    vis[j]=i
                j += i
        s=0
        for i in nums:
            s += vis[i]
            
        return s
            