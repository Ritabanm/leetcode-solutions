class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:

        deg = defaultdict(int)
        for u in edges : deg[u] += 1
        n = len(edges)
        
        # 1. FIND CYCLIC NODES
        
        # starting with nodes without in-edges
        Q = deque(u for u in range(n) if deg[u] == 0)
        
        # proceed until we're left with cyclic nodes
        while Q:
            for _ in range(len(Q)):
                u = Q.popleft()
                v = edges[u]
                deg[v] -= 1
                if deg[v] == 0:
                    Q.append(v)
        
        # 2. PROCESS CYCLES
        
        count = defaultdict(int)
        vis = set()
        
        # try starting cycle from each of the nodes
        # that were left after the previous step
        for u in filter(lambda u: deg[u] != 0, range(n)):
            if u in vis : continue
            
            # build the cycle
            cycle = []
            while u not in vis:
                cycle.append(u)
                vis.add(u)
                u = edges[u]
            
            # this is the answer for each of the cycle nodes
            for v in cycle : count[v] = len(cycle)

        # 3. PROCESS NON-CYCLIC NODES
        
        # increse path length by 1 or return the cycle 
        # length when encountered one of the cycle nodes
        @cache
        def dfs(v):
            if v in count : return count[v]
            return 1 + dfs(edges[v])
        
        # all results are now @cached, we have to collect them in order
        return [dfs(v) for v in range(n)]
        