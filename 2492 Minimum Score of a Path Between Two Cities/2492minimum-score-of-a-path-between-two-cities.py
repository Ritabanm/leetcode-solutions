class Solution:
    def bfs(self, n: int, adj: List[List[Tuple[int, int]]]) -> int:
        visited = [False] * (n+1)
        q = deque()
        answer = inf

        q.append(1)
        visited[1] = True

        while q:
            node = q.popleft()

            for edge in adj[node]:
                answer = min(answer, edge[1])
                if not visited[edge[0]]:
                    visited[edge[0]] = True
                    q.append(edge[0])

        return answer

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]

        for road in roads:
            adj[road[0]].append((road[1], road[2]))
            adj[road[1]].append((road[0], road[2]))

        return self.bfs(n, adj)