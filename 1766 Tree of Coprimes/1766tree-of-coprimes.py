class Solution:
    def getCoprimes(self, nums, edges):
        n, graph, parent = len(nums), defaultdict(list), defaultdict(int)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        stack = [(0,-1)]

        parent[0] = -1 

        while stack:
            node,p = stack.pop(0)

            for neighbor in graph[node]:
                if neighbor != p:
                    parent[neighbor] = node 
                    stack.append((neighbor,node))

        @lru_cache(None)
        def function(node,node_value):
            if node == -1:
                return -1 

            p = parent[node]

            if math.gcd(node_value,nums[p]) == 1:
                return p 

            return function(p,node_value)

        return [function(i,nums[i]) for i in range(n)]