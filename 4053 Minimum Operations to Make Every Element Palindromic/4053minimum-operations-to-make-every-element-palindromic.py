class Solution:
        vals=[]
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        for m in range(10):
                            x=(i*10**8)+(j*10**7)+(k*10**6)+(l*10**5)+(m*10**4)+(l*10**3)+(k*10**2)+(j*10**1)+i
                            vals.append(x)
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                            x=(i*10**7)+(j*10**6)+(k*10**5)+(l*10**4)+(l*10**3)+(k*10**2)+(j*10**1)+(i)
                            vals.append(x)
        for i in range(1,10):
            vals.append(i)
        for i in range(1,10):
                vals.append(11*i)
        for i in range(1,10):
            for j in range(10):
                vals.append(101*i+10*j)
        for i in range(1,10):
            for j in range(10):
                vals.append(1001*i+110*j)
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    vals.append(i*(1+10**4)+j*(10+10**3)+k*(10**2))
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    vals.append(i*(1+10**5)+j*(10+10**4)+k*((10**2)+(10**3)))
        for i in range(1,10):
            for j in range(10):
                for k in range(10):
                    for l in range(10):
                        x=i*(10**6+1)+j*(10+10**5)+k*((10**4)+(10**2))+l*(10**3)
                        vals.append(x)
        vals=list(set(vals))
        vals=[x for x in vals if x!=0]
        vals.sort()
        def minOperations(self, nums: list[int]) -> int:
         vals=self.vals
         odds=[x for x in vals if x%2]
         evens=[x for x in vals if x%2==0]
         def search(arr,k):
            low=0
            high = len(arr)-1
            ans=arr[0]
            while low<=high:
                mid= low + (high-low)//2
                if arr[mid]<=k:
                    ans=arr[mid]
                    low=mid+1
                else:
                    high=mid-1
            return ans
        
         n = len(nums)
         ans=0
         for i in range(n):
            if nums[i]%2:
                idx=bisect_left(odds,nums[i])
                val=search(odds,nums[i])
                if idx<len(odds) and odds[idx]<10**9:
                 ans+=min(nums[i]-val,odds[idx]-nums[i])//2
                else:
                    ans+=(nums[i]-val)//2
            else:
                idx=bisect_left(evens,nums[i])
                val=search(evens,nums[i])
                if idx<len(evens) and evens[idx]<10**9:
                 ans+=min(nums[i]-val,evens[idx]-nums[i])//2
                else:
                 ans+=(nums[i]-val)//2
         return ans