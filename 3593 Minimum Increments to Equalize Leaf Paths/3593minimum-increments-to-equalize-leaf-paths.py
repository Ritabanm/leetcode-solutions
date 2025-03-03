class TreeNode:
    def __init__(self, val: int, cost: int):
        self.val = val
        self.cost = cost
        self.children = []

class Solution:
    def helper(self, node: TreeNode) -> int:
        if not node.children:
            return node.cost

        child_costs = []
        for child in node.children:
            total = self.helper(child)
            child_costs.append(total)

        max_path = max(child_costs)

        for c in child_costs:
            if c < max_path:
                self.count += 1  

        return node.cost + max_path

    def buildTree(self, n: int, edges: List[List[int]], cost: List[int]) -> TreeNode:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        nodes = [TreeNode(i, cost[i]) for i in range(n)]
        root = nodes[0]
        visited = [False] * n
        visited[0] = True
        queue = deque([0])

        while queue:
            u = queue.popleft()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    nodes[u].children.append(nodes[v])
                    queue.append(v)

        return root

    def minIncrease(self, n: int, edges: List[List[int]], cost: List[int]) -> int:
        root = self.buildTree(n, edges, cost)
        self.count = 0
        self.helper(root)
        return self.count