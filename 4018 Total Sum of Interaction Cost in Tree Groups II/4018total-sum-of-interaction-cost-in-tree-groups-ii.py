class Solution:

    def interactionCosts(self, n: int, edges: list[list[int]], group: list[int]) -> int:
        from collections import defaultdict
        import sys

     

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        group_nodes = defaultdict(list)
        for i, g in enumerate(group):
            group_nodes[g].append(i)

        # Precompute depths and binary lifting for LCA
        LOG = 18
        depth = [0] * n
        up = [[-1] * LOG for _ in range(n)]
        tin = [0] * n
        tout = [0] * n
        timer = 0

        def dfs(u, p, d):
            nonlocal timer
            tin[u] = timer = timer + 1
            depth[u] = d
            up[u][0] = p
            for i in range(1, LOG):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
                else:
                    up[u][i] = -1
            for v in adj[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = timer

        dfs(0, -1, 0)

        def is_ancestor(u, v):
            return tin[u] <= tin[v] and tout[u] >= tout[v]

        def get_lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v
            for i in range(LOG - 1, -1, -1):
                if up[u][i] != -1 and not is_ancestor(up[u][i], v):
                    u = up[u][i]
            return up[u][0]

        total_cost = 0

        for g, nodes in group_nodes.items():
            k = len(nodes)
            if k < 2:
                continue

            # Sort nodes by DFS entry time
            nodes.sort(key=lambda x: tin[x])

            # Build virtual tree using adjacent nodes and their LCAs
            v_set = set(nodes)
            for i in range(len(nodes) - 1):
                v_set.add(get_lca(nodes[i], nodes[i + 1]))

            vt_nodes = sorted(list(v_set), key=lambda x: tin[x])
            vt_adj = defaultdict(list)
            stack = []

            for u in vt_nodes:
                while stack and not is_ancestor(stack[-1], u):
                    stack.pop()
                if stack:
                    vt_adj[stack[-1]].append(u)
                stack.append(u)

            # Compute subtree sizes and contributions on the virtual tree
            group_set = set(nodes)

            def compute_vt(u):
                nonlocal total_cost
                sz = 1 if u in group_set else 0
                for v in vt_adj[u]:
                    child_sz = compute_vt(v)
                    edge_len = depth[v] - depth[u]
                    total_cost += child_sz * (k - child_sz) * edge_len
                    sz += child_sz
                return sz

            compute_vt(vt_nodes[0])

        return total_cost