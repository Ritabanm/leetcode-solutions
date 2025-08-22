class Solution:
    def maximumSubtreeSize(self, edges, colors):
        n, graph, self.max_val = len(colors), defaultdict(list), 1

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def function(node,parent):
            if node is None:
                return []

            ans = [node]

            for neighbor in graph[node]:
                if neighbor != parent:
                    ans += function(neighbor,node)

            res = [colors[i] for i in ans]

            if len(set(res)) == 1:
                self.max_val = max(self.max_val,len(res))

            return ans 

        function(0,-1)

        return self.max_val 