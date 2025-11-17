class Solution:
    def checkWays(self, pairs):
        nodes, graph, degree = set(), defaultdict(set), defaultdict(int)

        for i,j in pairs:
            nodes |= {i,j}
            graph[i].add(j)
            graph[j].add(i)
            degree[i] += 1
            degree[j] += 1

        if max(degree.values()) < len(nodes)-1: return 0

        for n in nodes:
            if degree[n] < len(nodes)-1:
                neighbor = set()
                for nn in graph[n]:
                    if degree[n] >= degree[nn]: neighbor |= graph[nn]
                if neighbor - {n} - graph[n]: return 0

        for n in nodes:
            if any(degree[n] == degree[nn] for nn in graph[n]): return 2

        return 1


        








        


        

