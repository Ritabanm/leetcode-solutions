class Solution:
    def minimumSubstringsInPartition(self, s):
        n = len(s)

        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0 

            min_val, dict1 = float("inf"), defaultdict(int)

            for j in range(i,n):
                dict1[s[j]] += 1
                if len(set(dict1.values())) == 1:
                    min_val = min(min_val,1+dfs(j+1))

            return min_val 

        return dfs(0)