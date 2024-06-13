class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        nodes = list(range(n + 1))

        def find_root(node):
            if nodes[node] != node:
                nodes[node] = find_root(nodes[node])
            return nodes[node]

        for i in range(threshold + 1, n // 2 + 1):
            for j in range(2 * i, n + 1, i):
                nodes[find_root(j)] = find_root(i)

        return [find_root(i) == find_root(j) for i, j in queries]