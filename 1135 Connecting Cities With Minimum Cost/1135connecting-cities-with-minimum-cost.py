from collections import defaultdict
class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for x, y, cost in connections:
            adj_list[x].append((y, cost))
            adj_list[y].append((x, cost))

        seen = set()
       
        min_cost = 0
        pq = [(min_cost, 1)]
        
            
        while pq and len(seen) <= n:
            cost, node = heapq.heappop(pq)
            if node in seen:
                continue
            seen.add(node)
            min_cost += cost
            for adj_node, cost in adj_list[node]:
                if adj_node not in seen:
                    heapq.heappush(pq, (cost, adj_node))
        return -1 if len(seen) < n else min_cost
