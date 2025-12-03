class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        def dfs(curr: int, parent: int) -> int:
            size = 1
            for nbr in graph[curr]:
                if nbr != parent:
                    size += dfs(nbr, curr)
            subtree_size[curr] = size
            return size

        n = len(edges) + 1
        graph = defaultdict(list)
        subtree_size = [0] * n

        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dfs(0, -1)

        result = 0
        for i in range(n):
            is_good_node = True
            previous_size = -1
            for nbr in graph[i]:
                if subtree_size[nbr] < subtree_size[i]:
                    if previous_size == -1:
                        previous_size = subtree_size[nbr]
                    elif previous_size != subtree_size[nbr]:
                        is_good_node = False
                        break
            if is_good_node:
                result += 1

        return result