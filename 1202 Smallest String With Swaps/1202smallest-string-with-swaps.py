from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # build adjacency list
        adj = defaultdict(set)

        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
        
        # initializations
        n = len(s)
        visited = [False for _ in range(n)]
        ans = [c for c in s]

        # dfs helper
        def dfs(node, indices, characters):
            characters.append(s[node])
            indices.append(node)
            visited[node] = True

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, indices, characters)

        for i in range(n):
            if not visited[i]:
                self.indices = []
                self.characters = []
                dfs(i, self.indices, self.characters)

                self.characters.sort()
                self.indices.sort()

                for j in range(len(self.indices)):
                    ans[self.indices[j]] = self.characters[j]
        
        return ''.join(ans)

                