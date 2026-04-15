class Solution:
    inf = 10**5+7
    isprime = [1] * (inf+10)        # precalculating primes 
    isprime[0:2] = [0,0]

    # finding every primes till inf
    for i in range(2,inf+2):
        if isprime[i]:
            s = i + i
            while s < inf:
                isprime[s] = 0
                s += i

    nxtp = [-1] * (inf+1)           # nxtp[i] tells next prime for i
    nxt_prime = -1
    for i in reversed(range(0,inf+1)):
        nxtp[i] = nxt_prime
        if isprime[i] : nxt_prime = i
              
    def minOperations(self, nums: list[int]) -> int:

        res = 0
        for i,n in enumerate(nums): 
            # even
            if not i%2:
                # if not prime at even index
                if not self.isprime[n] : 
                    nxt = self.nxtp[n]          # get next prime after n
                    res += nxt-n
            # odd
            else:
                # if prime at odd index
                if self.isprime[n] :
                    curr = n
                    while self.isprime[curr]:     # find next non-prime after n (brute force)
                        curr += 1
                        res += 1
        return res