class Solution:
    def minJumps(self, nums: List[int]) -> int:
        maxi=max(nums)+1
        n=len(nums)
        dic=defaultdict(list)
        prime=[i for i in range(maxi)]
        i=2

        #Finding Primes
        for p in range(i*i,maxi,i):
            prime[p]=i
        for i in range(3,ceil(math.sqrt(maxi)),2):
            if prime[i]==i:
                for p in range(i*i,maxi,i):
                    prime[p]=i

        #Finding Indices divisible by each Primes
        for i in range(n):
            num=nums[i]
            while num!=prime[num]:
                prnum=prime[num]
                dic[prime[num]].append(i)
                while num%prnum==0:
                    num//=prnum
            if num!=1:
                dic[num].append(i)
        
        jumpedPrimes=set()
        q=deque([(0,0)])
        vis=[False]*n
        vis[0]=True
        while q:
            i,steps=q.popleft()
            if i==n-1: return steps
            if i+1<n and not vis[i+1]:
                vis[i+1]=True
                q.append((i+1,steps+1))
            if i-1>=0 and not vis[i-1]:
                vis[i-1]=True
                q.append((i-1,steps+1))
            if prime[nums[i]]==nums[i] and nums[i] not in jumpedPrimes:
                jumpedPrimes.add(nums[i])
                for j in dic[nums[i]]:
                    if not vis[j]:
                        vis[j]=True
                        q.append((j,steps+1))