class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        graph = [set() for i in range(n)]
        for a, b in edges:
            graph[a-1].add(b-1)
            graph[b-1].add(a-1)
        
        odd = 0
        oddVertices = []
        for i in range(n):
            if len(graph[i]) % 2 == 1:
                odd += 1
                oddVertices.append(i)
        if odd == 0:
            return True
        elif odd == 2:
            a, b = oddVertices
            for i in range(n):
                if i not in graph[a] and i not in graph[b]:
                    return True
        elif odd == 4:
            a, b, c, d = oddVertices
            if (b not in graph[a] and d not in graph[c]) or (c not in graph[a] and d not in graph[b]) or (d not in graph[a] and c not in graph[b]):
                return True
        return False
                
        