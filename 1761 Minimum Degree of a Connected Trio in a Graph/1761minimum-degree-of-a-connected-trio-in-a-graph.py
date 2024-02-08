from collections import defaultdict
class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Create a defaultdict(set) to represent the graph
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        min_degree = float('inf')

        # Step 2: Iterate through all the nodes
        for i in range(1, n + 1):
            # Iterate through the neighbour
            for j in range(i + 1, n + 1):
                # Nodes i and j are not connected, so skip this pair
                if j not in graph[i]:
                    continue
                # Iterate through third node
                for k in range(j + 1, n + 1):
                    if k in graph[i] and k in graph[j]:  # Nodes i, j, and k are connected (form a trio)
                        # for the three nodes i,j,k we want edges that dont include i,j,k 
                        # ie: i-j, j-i, j-k, k-j, k-i, i-k
                        degree = len(graph[i]) + len(graph[j]) + len(graph[k]) - 6
                        min_degree = min(min_degree, degree)

        return min_degree if min_degree != float('inf') else -1
