class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        MOD = 10**9 + 7

        
        '''
        n = 8
        sick = [2, 5]
        0 1 2 3 4 5 6 7

        _ _ I _ _ I _ _ 

        '''

        #factorials
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i    % MOD

        #print(fact)

        # n! / (r! * (n-r)!)
        def nCr(n_val, r_val):
            if r_val < 0 or r_val > n_val:
                return 0

            #return fact[n_val] // ( fact[r_val] * fact[n_val - r_val] )
            return fact[n_val] * pow(fact[r_val], MOD-2, MOD) % MOD * pow(fact[n_val - r_val], MOD-2, MOD) % MOD

        # sick.sort() <- it is given that it is already sorted
        res = 1 #number of infec sequences
        total_healthy = n - len(sick)
        
        # first segment (from o to first sick person)..... only 1 way
        if sick[0] > 0:
            gap = sick[0]
            res = res * nCr(total_healthy, gap)       % MOD
            total_healthy -= gap


        # sick = [2, 5]
        #   i     0. 1
        # middle segment (between 2 sick people)
        for i in range(1, len(sick)):
            gap = sick[i] - sick[i-1] - 1
            
            if gap > 0:
                res = res * nCr(total_healthy, gap)    % MOD
                res = res * (2**(gap - 1))             % MOD
                total_healthy -= gap


        # last segment (fron last sick to the end)
        if sick[-1] < n - 1:
            gap = n - sick[-1] - 1
            res = res * nCr(total_healthy, gap)          % MOD

        return res