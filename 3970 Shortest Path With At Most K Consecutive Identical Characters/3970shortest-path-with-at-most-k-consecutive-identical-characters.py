import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        # Build the directed graph
        adj = [[] for _ in range(n)]
        for f, t, w in edges:
            adj[f].append((t, w))
        
        # State in Dijkstra: (accumulated_cost, current_node, current_consecutive_count)
        # We start at node 0, with cost 0, and 1 consecutive character (the label of node 0)
        heap = [(0, 0, 1)]
        
        # Dictionary to memoize the minimum cost for a given state (node, consecutive_count)
        dist = {}
        
        while heap:
            cost, u, consec = heapq.heappop(heap)
            
            # If we reached the target node, return the cost (guaranteed to be minimum by Dijkstra)
            if u == n - 1:
                return cost
            
            # If we already visited this state with a lower or equal cost, skip
            if (u, consec) in dist:
                continue
            
            dist[(u, consec)] = cost
            
            # Explore neighbors
            for v, w in adj[u]:
                # Check if the neighbor's label matches the current node's label
                if labels[v] == labels[u]:
                    new_consec = consec + 1
                else:
                    new_consec = 1 # Reset the counter because the label changed
                
                # Only proceed if we don't exceed the limit K of consecutive identical characters
                if new_consec <= k and (v, new_consec) not in dist:
                    heapq.heappush(heap, (cost + w, v, new_consec))
        
        # If the heap empties and we haven't reached the target, no valid path exists
        return -1