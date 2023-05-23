class Solution:
    def minCost(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        n=len(nums)

        close=[0]*n
        for i in range(n):
            if i==0 :
                close[i]=1
            elif i==n-1:
                close[i]=n-2
            else:
                if abs(nums[i]-nums[i-1])<abs(nums[i]-nums[i+1]):
                    close[i]=i-1
                elif abs(nums[i]-nums[i-1])>abs(nums[i]-nums[i+1]):
                    close[i]=i+1
                else:
                    close[i]=i-1

        ltr=[0]*n

        rtl=[0]*n

        for i in range(1,n):
            if i==close[i-1]:
                ltr[i]=ltr[i-1]+1
            else:
                ltr[i]=ltr[i-1]+abs(nums[i]-nums[i-1])
        for i in range(n-2,-1,-1):
            if i==close[i+1]:
                rtl[i]=rtl[i+1]+1
            else:
                rtl[i]=rtl[i+1]+abs(nums[i]-nums[i+1])
        ans=[]
        for l,r in queries:

            if l<r:
                ans.append(ltr[r]-ltr[l])
            else:
                ans.append(rtl[r]-rtl[l])
        return ans

        
            
                