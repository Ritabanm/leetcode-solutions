import heapq
from collections import defaultdict as dd

class Solution:
    def findMaxPathScore(self, edges: list[list[int]], online: list[bool], k: int) -> int:
        # Build an adjacency list for a graph of online nodes
        g = dd(list)
        r = float('-inf')
        for u, v, c in edges:
            if online[u] and online[v]:
                g[u].append([v, c])
                r = max(r, c)
        
        n = len(online) - 1

        # Check if a path exists with all edge costs >= x and total cost <= k
        def validate(x):
            h = [[0, 0]]  # Min-heap for Dijkstra's: [cost, node]
            c = {0: 0}    # Min cost to reach each node
            
            while h:
                current_cost, node = heapq.heappop(h)
                
                if node == n:
                    return True
                
                if current_cost > c.get(node, float('inf')):
                    continue
                
                for neighbor, edge_cost in g[node]:
                    if edge_cost >= x:  # Check if edge cost meets the score criteria
                        new_cost = current_cost + edge_cost
                        if new_cost <= k and new_cost < c.get(neighbor, float('inf')):
                            c[neighbor] = new_cost
                            heapq.heappush(h, [new_cost, neighbor])
            return False

        # Use Dijkstra's to find a baseline path score for a lower bound
        l = float('-inf')
        ans = -1
        
        cost = dd(lambda: float('inf'))
        min_score = dd(lambda: float('-inf'))
        cost[0] = 0
        min_score[0] = float('inf')
        
        h = [[0, 0]]
        while h:
            current_cost, node = heapq.heappop(h)
            
            if current_cost > cost[node]:
                continue
            
            for nei, res in g[node]:
                if cost[nei] > current_cost + res and current_cost + res <= k:
                    cost[nei] = current_cost + res
                    min_score[nei] = min(min_score[node], res)
                    heapq.heappush(h, [cost[nei], nei])
        
        if n in min_score:
            l = min_score[n]
            ans = l

        # Binary search on the answer (the maximum score)
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans