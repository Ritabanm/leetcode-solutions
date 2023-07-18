class Solution:
    def countPaths(self, n, edges):
        # Build graph
        dict1 = defaultdict(list)

        for i,j in edges:
            dict1[i].append(j)
            dict1[j].append(i)

        # Use sieve of Eratosthenes

        is_primes = [False]*2 + [True]*(n-1)

        for p in range(2,n+1):
            if is_primes[p]:
                for j in range(2*p,n+1,p):
                    is_primes[j] = False

        # DFS

        self.total = 0

        def dfs(start,end):
            ans = [1-is_primes[start],is_primes[start]]

            for neighbor in dict1[start]:
                if neighbor == end: continue
                non_prime_path, prime_path = dfs(neighbor,start)
                self.total += non_prime_path*ans[1] + prime_path*ans[0]

                if is_primes[start]:
                    ans[1] += non_prime_path
                else:
                    ans[0] += non_prime_path
                    ans[1] += prime_path

            return ans

        dfs(1,0)

        return self.total








        


        
        
        