class Solution:
    def maximumCost(self, n, highways, k):
        graph = defaultdict(list)

        for i,j,c in highways:
            graph[i].append((j,c))
            graph[j].append((i,c))

        @lru_cache(None)
        def function(cur,length,mask):
            if length == 0:
                return 0 

            max_val = -1 

            for neighbor,cost in graph[cur]:
                if not mask&(1<<neighbor) and function(neighbor,length-1,mask|(1<<neighbor)) != -1:
                    max_val = max(max_val,cost+function(neighbor,length-1,mask|(1<<neighbor)))

            return max_val

        return max([function(i,k,1<<i) for i in range(n)])