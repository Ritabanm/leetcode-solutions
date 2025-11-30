class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def generate_primes(n):
            prime = [True]*(n+1)
            prime[0] = prime[1] = False
            p = 2
            while p*p<=n:
                if prime[p]:
                    for num in range(p*p,n+1,p):
                        prime[num] = False               
                p+=1
        
            ans = []
            for i in range(2,n+1):
                if prime[i]:
                    ans.append(i)
            return ans
        
        prime = generate_primes(n)
        l,r=0,len(prime)-1
        ans =[]
        while(l<=r):
            if prime[l]+ prime[r] == n:
                ans.append([prime[l],prime[r]])
                l+=1
                r-=1
            elif prime[l]+ prime[r] <n:
                l+=1
            else:
                r-=1
        return ans