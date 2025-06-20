class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        # algorithm
        # construct the tree
        # traverse the tree preorder 
        # compare the results with nodes 

        n = len(nodes)
        graph = defaultdict(list)
        root = None
        for node, parent in nodes:
            graph[parent].append(node)
            if parent == -1:
                root = node
        
        preorder_nodes = []
        visited = set()
        def preorder(u, visited):
            if u in visited:
                return 
            preorder_nodes.append(u)
            visited.add(u)
            for v in graph[u]:
                preorder(v, visited)
        preorder(root, visited)

        nodes_flatten = [node for node, _ in nodes]
        return preorder_nodes == nodes_flatten
        