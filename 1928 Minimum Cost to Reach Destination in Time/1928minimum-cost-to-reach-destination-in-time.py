class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        # a Fenwick tree per node, O(maxTime*n) memory
        n = len(passingFees)
        costTrees = [[math.inf]*(maxTime+2) for _ in range(n)]
        
        def minCost(u: int, t: int) -> float:
            """Returns the minimum cost over paths reaching u in time <= t"""
            t += 1 # since we want the min cost for time 0 as well
            ans = math.inf
            while t:
                ans = min(ans, costTrees[u][t])
                t &= t-1
            return ans

        def reduceCost(u: int, t: int, c: int) -> None:
            tree = costTrees[u]
            t += 1
            while t < maxTime+2:
                tree[t] = min(tree[t], c)
                t += t & -t

        # adjacency list, handle parallel edges by recording only the minimum-weight one
        adj = [defaultdict(lambda: math.inf) for _ in range(n)]
        for u, v, t in edges:
            if t > maxTime: continue

            adj[u][v] = min(adj[u][v], t)
            adj[v][u] = min(adj[v][u], t)

        pq = [(0, passingFees[0], 0)] # time, cost, u
        reduceCost(u=0, t=0, c=passingFees[0])
        while pq:
            t, c, u = heappop(pq)

            if c > minCost(u, t):
                continue # stale entry

            for v, dt in adj[u].items():
                tv = t+dt
                cv = c + passingFees[v]

                if tv > maxTime:
                    continue
                if cv >= minCost(v, tv): 
                    continue # already enqueued a cheaper path at least as fast

                # record that we have a new cheapest path to v, costing cv, so we don't later
                # push any paths with t' >= t and c' >= cv
                reduceCost(v, tv, cv)
                heappush(pq, (tv, cv, v))

        # explored all paths from 0 to all other nodes, in time order, ensuring cost
        # drops monotonically with time to its minimum value
        
        min_cost = min(costTrees[n-1])
        return min_cost if min_cost < math.inf else -1